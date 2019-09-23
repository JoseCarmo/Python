#/usr/bin/python
import os 
from selenium import webdriver
import io
import time
from selenium.webdriver.chrome.options import Options
import time
import shutil
import zipfile
import os

options = Options()
options.headless = False 
options.add_argument("download.default_directory=C:\\Users\\jose.eustaquio\\Downloads\\Vazoes")
driver = webdriver.Chrome(chrome_options=options)

driver.get ("https://sintegre.ons.org.br/")
driver.find_element_by_id("username").send_keys("jose_cpfl")
driver.find_element_by_id ("password").send_keys("bbAA4433!!")
driver.find_element_by_name("submit.Signin").click()

time.sleep(7.5)

while "1" == "1":
    driver.get ("https://sintegre.ons.org.br/sites/9/13/79/Produtos/246/Nao_Consistido_201909_RV1.zip")
    print("voltei")
    time.sleep(5.5)
    if "Página não encontrada" in driver.page_source:
        print("Deu errado")
        # def método que fecha o drive
        quit()

    else:
        arquivo = zipfile.ZipFile("C:\\Users\\jose.eustaquio\\Downloads\\Nao_Consistido_201909_PMO.zip")
        arquivo.extractall("C:\\Users\\jose.eustaquio\\Downloads\\Vazoes")
        shutil.move("C:\\Users\\jose.eustaquio\\Downloads\\Vazoes\\Nao_Consistido\\Prevs_VE.prv", "C:\\Users\\jose.eustaquio\\Downloads\\Vazoes\\prevs.prv")
        shutil.rmtree("C:\\Users\\jose.eustaquio\\Downloads\\Vazoes\\Nao_Consistido")
        
        # def método para o GEVAZP 
        # def método para rodar o DECOMP 
        # def método para convergir o DECOMP
        # def método avisar que saiu vazão

