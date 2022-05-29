import json
import requests

from Individuos.Libro import LibroAPI


class GoogleBooksAPI:
    def __init__(self):
        self.url = 'https://www.googleapis.com/books/v1/volumes'
        self.params = {}

    def addParam(self, key, value):
        self.params[key] = value

    def resetParams(self):
        self.params = {}

    def parseParams(self, params):
        return "+".join(f"{key}:{value}" for key, value in params.items())

    def getBook(self):
        parsedParams = self.parseParams(self.params)
        response = requests.get(f"{self.url}?q={parsedParams}&printType=books")
        self.resetParams()
        print(response.url)
        return json.loads(response.text)["items"][0]

    def parseBook(self, bookJson: json) -> LibroAPI:
        volumeInfo = bookJson.get('volumeInfo')
        saleInfo = bookJson.get('saleInfo')
        publishedDate = volumeInfo.get('publishedDate')
        paginas = volumeInfo.get('pageCount')
        ratings = volumeInfo.get('ratingsCount')
        precio = saleInfo.get('retailPrice').get(
            'amount') if saleInfo.get('retailPrice') else saleInfo.get('listPrice').get('amount') if saleInfo.get('listPrice') else None
        return LibroAPI(paginas, ratings, precio, publishedDate)

    def fetchBook(self):
        parsedParams = self.parseParams(self.params)
        response = requests.get(f"{self.url}?q={parsedParams}&printType=books")
        self.resetParams()
        return response

    def getBook(self):
        response = self.fetchBook()
        return self.parseBook(json.loads(response.text)["items"][0])

    def addTitulo(self, title):
        print(title)
        self.addParam('intitle', title)
        return self

    def addAutor(self, author):
        self.addParam('inauthor', author)
        return self

    def addGenero(self, genre):
        self.addParam('subject', genre)
        return self
