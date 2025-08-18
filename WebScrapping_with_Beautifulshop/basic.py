from bs4 import BeautifulSoup

with open("website.html", 'r') as file:
    contents = file.read()
    # print(contents)

soup = BeautifulSoup(contents, 'html.parser')
all_anchor_tab = soup.find_all(name='a')
# print(all_anchor_tab)

# print all link present a tag
for anchor in all_anchor_tab:
    # print(anchor['href'])
    print(anchor.get("href"))

# heading = soup.find_all(name='h1',id="name")
# print(heading)

section_heading = soup.find_all(name='h3',class_="heading")
print(section_heading)

# name = soup.select_one('#name').text
# print(name)
#
# heading = soup.select('.heading')
# print(heading)

