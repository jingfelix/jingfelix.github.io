class HtmlDom:
    """
    represent an html dom element
    """

    def __init__(
        self,
        element: str = "",
        content: str = "",
        _class: str = "",
        _id: str = "",
    ):
        self.element: str = element
        self.content: str = content
        self.children: list = []
        self._class: str = _class
        self._id: str = _id

    def addChildren(self, child) -> None:
        self.children.append(child)

    def addChildrenList(self, children: list) -> None:
        self.children.extend(children)

    def toString(self) -> str:
        _content: str = self.content

        if self.children != []:
            for child in self.children:
                _content += child.toString()

        if self.element == "":
            return _content
        else:
            return (
                '<{element} class="{_class}" id="{_id}">{content}</{element}>'.format(
                    element=self.element,
                    content=_content,
                    _class=self._class,
                    _id=self._id,
                )
            )

    def find(self, element: str) -> list:
        return [child for child in self.children if child.element == element]

    def __str__(self):
        return self.toString()


class HtmlDomA(HtmlDom):
    """
    represents <a> element
    """

    def __init__(
        self,
        element: str = "a",
        content: str = "",
        _class: str = "",
        _id: str = "",
        href: str = "",
    ):
        super().__init__(element, content, _class, _id)
        self.href = href

    def toString(self):
        return "<a href='{href}' class='{_class}' id='{_id}'>{content}</a>".format(
            href=self.href, content=self.content, _class=self._class, _id=self._id
        )

    def __str__(self):
        return self.toString()
