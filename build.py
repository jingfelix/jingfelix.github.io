try:
    from htmlobj import *
    from pathlib import Path
    import mistune
    import copy
    import json
except ImportError:
    print("ImportError: Missing one or more modules.")
    exit(1)


def viewPageIndex(article_path: str) -> str:
    p = Path(article_path)

    if p.is_file():
        return None

    main: HtmlDom = HtmlDom()
    div: HtmlDom = HtmlDom(
        element="div", _class="mdui-col-xs-12 mdui-typo-subheading para"
    )
    i: HtmlDom = HtmlDom(
        element="i", _class="mdui-icon material-icons", content="chevron_right"
    )
    em: HtmlDom = HtmlDom(element="em")
    a: HtmlDomA = HtmlDomA()

    em.addChildren(a)
    div.addChildrenList([i, em])

    for name in list(p.glob("*.md")):
        name = (
            str(name).replace(".md", "").replace(str(article_path), "").replace("/", "").replace("\\", "")
        )
        # TODO: 修改name变量使其不包含路径

        _div = copy.deepcopy(div)
        _a = (_div.find("em")[0]).find("a")[0]
        _a.content = name

        # TODO: important, an undefined father path should be used here.
        _a.href = "/articles/" + name + ".html"

        main.addChildren(_div)

    return main.toString()


def viewPagePost(article_path: str, template_file_path: str, pic_dic: dict) -> bool:

    p = Path(article_path)

    # get template html content
    with open(template_file_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    # get article content
    for name in list(p.glob("*.md")):
        name = str(
            str(name).replace(".md", "").replace(str(article_path), "").replace("/", "").replace("\\", "")
        )

        if name in pic_dic:
            photo_to_replace = pic_dic[name]
        else:
            photo_to_replace = "https://api.vvhan.com/api/bing?type=sj"

        with open(article_path + "/" + name + ".md", "r", encoding="utf-8") as md_file:
            markdown_content = md_file.read()

            # convert markdown to html
            markdown_to_replace = mistune.html(markdown_content)

        with open(article_path + "/" + name + ".html", "w", encoding="utf-8") as html_file:
            html_file.write(
                template_content.replace("<!--MARKDOWN-->", markdown_to_replace)
                .replace("<!--TITLE-->", name)
                .replace("<!--MAINPHOTO-->", photo_to_replace)
            )
    return True


def main():

    current_path = Path.cwd()
    article_path = current_path / "articles"
    template_file_path = current_path / "templates" / "template.html"

    with open(template_file_path, "r", encoding="utf-8") as f:
        template_file_content = f.read()

    content_to_replace = viewPageIndex(article_path)
    new_index = (
        template_file_content.replace("<!--CONTENT-->", content_to_replace)
        .replace("<!--TITLE-->", "归档")
        .replace(
            "<!--MAINPHOTO-->",
            "https://pic3.zhimg.com/50/v2-f8b5afa8767a3c1b2bd126f8ba1b42b6_r.jpg",
        )
    )

    with open(current_path / "index.html", "w", encoding="utf-8") as f:
        f.write(new_index)

    with open(current_path / "pic.json", "r", encoding="utf-8") as f:
        pic_dic = json.load(f)

    with open(article_path / "关于.md", "r", encoding="utf-8") as f1:
        with open(current_path / "README.md", "w+", encoding="utf-8") as f2:
            f2.write(f1.read())

    if viewPagePost(str(article_path), str(template_file_path), pic_dic) is True:
        print("Build success.")
    else:
        print("Build failed.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Build interrupted.")
        exit(1)
