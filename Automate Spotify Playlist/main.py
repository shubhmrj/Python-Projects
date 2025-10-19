from bs4 import BeautifulSoup
import requests


Date = input("Which year famous song playlist do you want to create ? Fomat YYYY-MM-DD : ")

# response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/")
#
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, 'html.parser')

# Get all article links
# articles = soup.find_all(name='a', id='title-of-a-story' , class_='c-title  a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max')
#
# print(articles)

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + Date
response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)