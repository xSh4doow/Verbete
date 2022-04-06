from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options

#Configurar o WebDriver
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")
browser = wd.Chrome(options=chrome_options)


palavras = [
'Beco',
'Condenado',
'Galeria',
'Torpedo',
'Internacional',
'Oculista',
'Pato',
'Pasto',
'Lança',
'Zarabatana'
          ]

significados = []

def escolher_palavra(index):
    i = index
    for palavra in palavras:
        palavra = palavras[i]
        return palavra

def pegar_significados():
    i = 0
    while i < len(palavras):
        palavra = escolher_palavra(i)
        browser.get(f"https://dicionario.priberam.org/{palavra}")
        sign = browser.execute_script('return document.getElementsByClassName("def")[1].innerText')
        sign = str(sign).replace("\xa0", "")
        significados.append(sign)
        i = i + 1
    print(significados)

def unir():
    pegar_significados()
    n = 0
    for significado in significados:
        index = ((2 * n) + 1)
        palavras.insert(index, significados[n])
        n = n+1

def tudo():
    unir()
    print(palavras)

tudo()
