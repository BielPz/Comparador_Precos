from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from time import sleep

options = Options()
options.add_argument("--headless=new") # Roda sem abrir a janela do navegador

# Selecao do navergador 
driver = webdriver.Chrome(options=options)

# Entrar no site
driver.get('https://www.kabum.com.br/produto/1017204/monitor-gamer-asus-rog-strix-27-qhd-220hz-0-3ms-fast-ips-vrr-g-sync-freesync-hdr-400-altura-ajustavel-xg27acsr')
sleep(5)

nomes_Produtos = driver.find_element(By.XPATH, "//h1[@class='text-sm font-semibold text-gray-800 desktop:text-base desktopLarge:text-xl']")
precos_Produtos = driver.find_element(By.XPATH, "//number-flow-react[@class='text-2xl leading-tight transition-colors duration-500 [--number-flow-mask-width:0px] [--number-flow-mask-height:0px]']")

# Guardar informacoes em um csv
# Para mais de um produto usar -> for produto, valor in zip(nomes_Produtos, precos_Produtos):
with open('precos.csv', 'a', encoding='utf-8') as arquivo:
    arquivo.write(f'{nomes_Produtos.text}: {precos_Produtos.text}{os.linesep}')

# Fecha o navegador
driver.quit()