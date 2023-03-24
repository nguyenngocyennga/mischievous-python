# Web Scraping with Beautiful Soup

from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

movie_list = [movie.img.get("alt") for movie in soup.find_all(class_="listicle-item")]

with open("movies.txt", mode="a") as file:
    order = 1
    for movie in list(reversed(movie_list)):
        file.write(f"{order}) {movie}\n")
        order += 1
