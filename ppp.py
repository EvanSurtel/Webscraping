from bs4 import BeautifulSoup
import re

# Your HTML document as a string
html = "<html className='hello'><body><p>Hello, world! ! !</p></body></html>"
soup = BeautifulSoup(html, 'html.parser')
content = soup.prettify().split('\n')
result = []
for line in content:
    line_elements = re.findall('<[^<]+?>', line)  # find all HTML tags in line
    line = re.sub('<[^<]+?>', '', line)  # remove HTML tags from line
    # remove non-word characters from line
    line = re.sub(r'[^\w\s]+', '', line)
    words = line.strip().split()  # split text content into words
    result.extend(line_elements + words)
print(result)
