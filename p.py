from bs4 import BeautifulSoup

html = '<html><body><p>Hello, world!</p></body></html>'
soup = BeautifulSoup(html, 'html.parser')

elements = []


def walk(node):
    if node.name:
        elements.append(node.name)
    for child in node.children:
        walk(child)
    if node.string:
        for word in node.string.strip().split():
            elements.append(word)


walk(soup)
print(elements)
# Output: ['html', 'body', 'p', 'Hello,', 'world!', 'p', 'body', 'html']
