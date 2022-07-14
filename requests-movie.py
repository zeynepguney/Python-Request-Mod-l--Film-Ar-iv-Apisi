# themoviedb.org => film ve dizi arşivi
# themovidedb' nin sunduğu apiyi uygulamanızda kullanınız
# anahtar kelimeye göre arama
# en popüler film listesi
# vizyondaki film listesi

from unittest import result
from urllib import response
import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "<api_key>"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    
    def getPlaying(self):
        response = requests.get(f"{self.api_url}/movie/now_playing?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearch(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

movieApi = theMovieDb()

while True:
    secim = input("1- Popular Movies\n2- Now Playing\n3- Search Movies\n4- Exit\nSeçim : ")

    if secim == "4":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])
            # print(movies)
        elif secim == "2":
            movies = movieApi.getPlaying()
            for movie in movies['results']:
                print(movie['title'])
        elif secim == "3":
            keyword = input("Keyword : ")
            movies = movieApi.getSearch(keyword)
            for movie in movies['results']:
                print(movie['name'])
