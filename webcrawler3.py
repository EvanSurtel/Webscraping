import requests

import re
import hashlib
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

initial_url = input("prompt")

# Download the HTML content of the initial URL
response = requests.get(initial_url)
html_content = response.text

data = []

# Parse the html
soup = BeautifulSoup(html_content, 'html.parser')
soup1 = BeautifulSoup(html_content, 'html.parser')

# Replace all words from html with 0


def tokenize(soup):
    for token in soup.find_all(text=True):
        replaced_text = re.sub('\w+', '0', token)
        token.replace_with(replaced_text)
    return str(soup)

# Replace all html tags with 1


def replace_tags(s):
    new_html = re.sub(r'<.*?>', '1', s)
    return (new_html)

# remove whitespaces


def remove(s):
    return ''.join(c for c in s if c in ('0', '1'))

# f(i, j), append data to data array, find i and j for the greatest outcome


def function(s):
    max = 0
    max_i = 0
    max_j = 0
    i = 0
    while (i < len(s) - 1):
        c = 0
        a = 0
        while a < i:
            if (s[a] == '1'):
                c += 1
            a += 1
        j = i+1
        while (j < len(s)):
            value = c
            m = i
            while m <= j:
                if (s[m] == '0'):
                    value += 1
                m += 1
            n = j+1
            while n < len(s):
                if s[n] == '1':
                    value += 1
                n += 1

            data.append([i, j, value])
            if value > max:
                max = value
                max_i = i
                max_j = j

            j += 1

        i += 1

    return max, max_i, max_j

# Returns list where each element is a single HTML tag or word


def make_array(soup):
    content = soup.prettify().split('\n')
    result = []
    for line in content:
        line_elements = re.findall('<[^<]+?>', line)
        line = re.sub('<[^<]+?>', '', line)
        line = re.sub(r'[^\w\s]+', '', line)
        words = line.strip().split()
        result.extend(line_elements + words)
    return result


# partition list


def access_i_j(list, i, j):
    list = list[i:j]
    content = [word for word in list if not re.match('<.*>', word)]
    content = ' '.join(content)
    return content

# write to H.html file where H is the hash value of url


def write_to_file_html(content, url):
    hash_object = hashlib.sha1(url.encode())
    hash_value = hash_object.hexdigest()
    filename = hash_value + ".html"
    with open(filename, "w") as file:
        file.write(content)

# write to H.txt file where H is the hash value of url


def write_to_file_txt(content, url):
    hash_object = hashlib.sha1(url.encode())
    hash_value = hash_object.hexdigest()
    filename = hash_value + ".txt"
    with open(filename, "w") as file:
        file.write(content)

# write to csv file


def write_to_csv(data):
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['i', 'j', 'value'])
        writer.writerows(data)


tokenized = tokenize(soup)

tags = replace_tags(tokenized)

cleaned = remove(tags)

max, max_i, max_j = function(cleaned)

array = make_array(soup1)

content = access_i_j(array, max_i, max_j)

write_to_file_html(html_content, 'http://toscrape.com/')
write_to_file_txt(content, 'http://toscrape.com/')

write_to_csv(data)

df = pd.read_csv('data.csv')
sns.heatmap(df.pivot('i', 'j', 'value').sort_index(ascending=False))
plt.show()
