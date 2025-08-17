from bs4 import BeautifulSoup

with open("website.html", 'r') as file:
    contents = file.read()
    # print(contents)

soup = BeautifulSoup(contents, 'html.parser')
print(soup.find_all(name='a'))