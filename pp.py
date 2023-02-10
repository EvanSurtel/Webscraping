from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <h1>This is a heading</h1>
        <p>This is a paragraph.</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
result = []

for tag in soup.descendants:
    if tag.name:
        result.append("<" + tag.name + ">")
    if tag.string:
        result.append(tag.string.strip())
    if tag.name:
        result.append("</" + tag.name + ">")

print(result)
