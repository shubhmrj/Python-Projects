import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

all_movies_data = soup.find_all("h3", class_="title")

movies_name = [movie.get_text(strip=True) for movie in all_movies_data]
movies = movies_name[::-1]

with open("file.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
