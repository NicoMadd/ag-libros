import json
from pandas import Series
import requests

from Individuos.Libro import LibroAPI


'''

La API de Google Books es una API de servicio web que permite obtener información sobre libros.
Se hizo para formalizar los precios, y paginas. Al ser muy pesado, se opta por generar un dataset comun.


'''


class GoogleBooksAPI:
    def __init__(self):
        self.url = 'https://www.googleapis.com/books/v1/volumes'
        self.params = {}

    def addParam(self, key: str, value):
        self.params[key] = value

    def resetParams(self):
        self.params = {}

    def parseParams(self, params: dict):
        return "+".join(f"{key}:{value}" for key, value in params.items())

    def getBook(self):
        parsedParams = self.parseParams(self.params)
        response = requests.get(f"{self.url}?q={parsedParams}&printType=books")
        self.resetParams()
        print(response.url)
        return json.loads(response.text)["items"][0]

    def parseBook(self, bookJson: json) -> LibroAPI:
        # if bookJson is None then return LibroApi()
        if bookJson is None:
            return LibroAPI()
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
        try:
            response = self.fetchBook()
            items = self.parseBook(json.loads(response.text)["items"][0])
            return items
        except KeyError as e:
            return LibroAPI()

    def addTitulo(self, title: str):
        print(title)
        self.addParam('intitle', title)
        return self

    def addAutor(self, author: str):
        self.addParam('inauthor', author)
        return self

    def addGenero(self, genre: str):
        self.addParam('subject', genre)
        return self

    def buscarLibro(self, libro: Series):
        self.addTitulo(libro.titulo)
        # self.addAutor(libro.autor)
        # self.addGenero(libro.genero)
        return self.getBook()
