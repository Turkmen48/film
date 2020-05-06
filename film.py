#themoviedb.org
#anahtar kelimeye göre arama
#en popüler film
#vizyondaki film
import requests
class dbmovie:
    def __init__(self):
        self.auth="68fa1778589e3c762c9d08c5d060d341"
        self.url="https://api.themoviedb.org/3"
    def trend(self):
        request=requests.get(f"{self.url}/trending/movie/day?api_key={self.auth}&language=tr-TR")
        return request.json()
    def search(self,keyword):
        request=requests.get(f"{self.url}/search/movie?api_key={self.auth}&query={keyword}&language=tr-TR&include_adult=true")
        return request.json()
print("""
Made by:Turkmen
""")
movieapi=dbmovie()
while True:
    secim=input("1-)Bugünün trend filmleri\n2-)Vizyondaki Filmler\n Çıkmak için q'ya bas")
    if(secim=="q"):
        break
    else:
        if(secim=="1"):
            movies=movieapi.trend()
            for i in movies["results"]:
                cevir=i["vote_average"]
                cevir=str(cevir)
                print(f"Filmin adı:{i['title']}\nFilmin orjinal adı:{i['original_title']}\nPuanı:{cevir}\nGösterim Tarihi:{i['release_date']}\nAçıklama: {i['overview']}")
                print("".center(10,'*'))
        elif(secim=="2"):
            keyword=input("Aramak istediğiniz filmin adını girin")
            movies = movieapi.search(keyword)
            for i in movies["results"]:
                cevir = i["vote_average"]
                cevir = str(cevir)
                print(
                    f"Filmin adı:{i['title']}\nFilmin orjinal adı:{i['original_title']}\nPuanı:{cevir}\nGösterim Tarihi:{i['release_date']}\nAçıklama: {i['overview']}")
                print("".center(10, '*'))