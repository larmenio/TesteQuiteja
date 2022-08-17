import re
from bs4 import BeautifulSoup
from gazpacho import Soup

class WebPage:
    def __init__(self):
        #Variáveis arquivo atribuídos na classe
        self.url = data['url']
        self.inicio = data['inicio']
        self.fim = data['fim']

    def url(self):
        #Passar parametro lucas na url
        url = self.url.replace('candidato', 'lucas')
        return url

    def page_capture(self, url):
        #Capturar pagina
        soup = Soup.get(url)
        page = (str(soup))
        return page

    def treating(self, page):
        #Tratando página - pip install lxml
        treated = BeautifulSoup(page, "lxml").text

        #Removendo escape characters(quebra de linha, ...)
        treated = re.sub('\xa0','\n', treated)
        treated = re.sub('\n+', '\n', treated)
        return treated

    def words(self, treated):
        #Procurando palavras com: Inicio: con | Fim: e
        #Criando lista com essas palavras
        words = treated.split()
        counter = 0
        lista = []
        for word in words:
            word = word.replace(".", "").replace(",", "")
            if self.inicio in word.lower()[0:3]:
                if self.fim in word.lower()[-1]:
                    counter+=1
                    lista.append(word)

        return counter, lista


#Leitura arquivo desafio.ini
data = {}
with open('desafio.ini') as f:
    for line in f:
        (key, sign, value) = line.split()
        data[key] = value

#Execução script
pagina = WebPage()
url = pagina.url
page = pagina.page_capture(url)
treating = pagina.treating(page)
counter, lista = pagina.words(treating)

print(treating)
print(counter)
print(lista)

