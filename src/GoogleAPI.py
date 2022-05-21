import json
import requests


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
