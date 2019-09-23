#/usr/bin/python
import pandas as pd
import numpy as np
import os 
import glob
from selenium import webdriver
import io
import urllib
from PIL import Image
from io import BytesIO
import time
from selenium.webdriver.chrome.options import Options
import time
import shutil

"""
options = Options()
options.headless = False 
options.add_argument("download.default_directory=C:\\Users\\jose.eustaquio\\Downloads\\RDH")
driver = webdriver.Chrome(chrome_options=options)

i = 0

driver.get ("https://sintegre.ons.org.br/")
driver.find_element_by_id("username").send_keys("jose_cpfl")
driver.find_element_by_id ("password").send_keys("bbAA4433!!")
driver.find_element_by_name("submit.Signin").click()

time.sleep(27.5)

#for dia in range(10,11):
 #   driver.get ("https://sintegre.ons.org.br/sites/7/39/_layouts/download.aspx?SourceUrl=/sites/7/39/Produtos/156/IPDO-0" + str(dia) + "-09-2019.xlsm")
  #  time.sleep(7.5)
   # shutil.move("C:\\Users\\jose.eustaquio\\Downloads\\IPDO-0" + str(dia) + "-09-2019.xlsm", "C:\\Users\\jose.eustaquio\\Downloads\\RDH")

for dia in range(19,20):
    driver.get ("https://sintegre.ons.org.br/sites/7/39/_layouts/download.aspx?SourceUrl=/sites/7/39/Produtos/156/IPDO-" + str(dia) + "-09-2019.xlsm")
    time.sleep(7.5)
    shutil.move("C:\\Users\\jose.eustaquio\\Downloads\\IPDO-" + str(dia) + "-09-2019.xlsm", "C:\\Users\\jose.eustaquio\\Downloads\\RDH")

"""
path = 'C:\\Users\\jose.eustaquio\\Downloads\\RDH'

files = []
ENA = []
ARM = []

DadosENA = {'ENA Med'}
ENASE = pd.DataFrame(DadosENA)
ENAS = pd.DataFrame(DadosENA)
ENANE = pd.DataFrame(DadosENA)
ENASN = pd.DataFrame(DadosENA)
DadosENAS1 = pd.DataFrame({'Arquivo, ENA Med, ENA Med, ENA Med, ENA Med'}) 

DadosARM = {'ARM'}
ARMSE = pd.DataFrame(DadosARM)
ARMS = pd.DataFrame(DadosARM)
ARMNE = pd.DataFrame(DadosARM)
ARMN = pd.DataFrame(DadosARM)
DadosARM1 = pd.DataFrame({'Arquivo, ENA Med, ENA Med, ENA Med, ENA Med'}) 

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if "IPDO" in file:
            print(file)
            files.append(os.path.join(r, file))

for file in files:

    RDH = pd.read_excel(file, sheet_name='IPDO',usecols="M:R",skiprows=60,nrows=4)
    ENA = [RDH.iloc[3][0], RDH.iloc[2][0], RDH.iloc[1][0] , RDH.iloc[0][0]]
    ARM = [RDH.iloc[3][4], RDH.iloc[2][4], RDH.iloc[1][4] , RDH.iloc[0][4]]

    ENASE = pd.concat([ENASE, pd.Series(RDH.iloc[3][0])], axis=0)
    ENAS  = pd.concat([ENAS,  pd.Series(RDH.iloc[2][0])], axis=0)
    ENANE = pd.concat([ENANE, pd.Series(RDH.iloc[1][0])], axis=0)
    ENASN = pd.concat([ENASN, pd.Series(RDH.iloc[0][0])], axis=0)

    ARMSE = pd.concat([ARMSE, pd.Series(RDH.iloc[3][4])], axis=0)
    ARMS  = pd.concat([ARMS , pd.Series(RDH.iloc[2][4])], axis=0)
    ARMNE = pd.concat([ARMNE, pd.Series(RDH.iloc[1][4])], axis=0)
    ARMN  = pd.concat([ARMN , pd.Series(RDH.iloc[0][4])], axis=0)

#print(ENASE)

ENASE.reset_index(drop=True, inplace=True)
ENAS.reset_index(drop=True, inplace=True)
ENANE.reset_index(drop=True, inplace=True)
ENASN.reset_index(drop=True, inplace=True)

ARMSE.reset_index(drop=True, inplace=True)
ARMS.reset_index(drop=True, inplace=True)
ARMNE.reset_index(drop=True, inplace=True)
ARMN.reset_index(drop=True, inplace=True)

files = [x[43:] for x in files]

files.insert(0,"Dia")

Dias = pd.Series(files)

DadosENAS1 = pd.concat([Dias, ENASE, ENAS, ENANE, ENASN], axis = 1)

DadosARM1 = pd.concat([Dias, ARMSE, ARMS, ARMNE, ARMN],  axis = 1)

Dados = pd.concat([DadosENAS1,DadosARM1], axis = 1)

Dados.to_csv("C:\\Users\\jose.eustaquio\\Downloads\\RDH\\DADOS.csv" , decimal='.', sep=';', na_rep='')
