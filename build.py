# import
from articles import pson
from shutil import copy
# config
baseHtmlPath = './static/base.html'
articleDirPath = './articles/'
indexPath = 'index.html'
aboutPath = 'about.html'
readmePath = 'README.md'
url = r'https://jingfelix.github.io'


# read base.html
with open(baseHtmlPath, mode='r', encoding='utf-8') as b:
    base = b.read()

# build articles from draft(json.html)
for key in pson.keys():
    with open((articleDirPath + key + '.html'), mode='w', encoding='utf-8') as f:
        title = pson[key]['title']
        photo = pson[key]['photo']
        content = pson[key]['content']

        template = base.replace('[[TITLE]]', title).replace('[[PHOTO]]', photo).replace('[[CONTENT]]', content).replace('[[URL]]', url)

        f.write(template)
        print('{0} build complete!'.format(title))
    pass

# copy index.html & about.html
copy(articleDirPath + indexPath, indexPath)
copy(articleDirPath + aboutPath, aboutPath)

# build README.md
with open(readmePath, mode='w', encoding='utf-8') as r:
    r.write(pson['about']['content'])