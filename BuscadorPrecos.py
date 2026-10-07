from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from time import sleep

options = Options()
options.add_argument("--headless=new")              # Roda sem abrir a janela do navegador

# Selecao do navergador 
driver = webdriver.Chrome(options=options)

site = input("Digite o link do produto que vai ser pesquisado: ")
xpath_preco = input("Digite o XPATH do Elemento HTML que contem o preço do Produto: ")
# Precisa validar a entrada do usuario

# Fluxo Principal do Script
try:
    driver.get(site)
    sleep(5)
    nome_Produto = driver.find_element(By.XPATH, "//h1")
    nome = nome_Produto.text
    preco = driver.find_element(By.XPATH, xpath_preco)
finally:
    driver.quit()

if preco is None:
    raise SystemExit("Não foi possivel achar o preço no site escolhido")

# Guardar informacoes em um csv
# Para mais de um produto usar -> for produto, valor in zip(nomes_Produtos, precos_Produtos):
with open('precos.csv', 'a', encoding='utf-8') as arquivo:
    arquivo.write(f'{nome}: {preco.text}{os.linesep}')