data_final = "2019-08-01"

import datetime 
import pandas as pd
data_final = datetime.datetime.strptime(data_final, "%Y-%m-%d")

# encoding: utf-8
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('U:\\Comercializacao\\11. Geração\\Base de Dados.xlsm', sheet_name='Dados PCH',skiprows =1)
df = df.drop(["Cód","Nome Usina_BE","Agente","SAP"],axis=1)
df = df.drop(labels=[17,27,33,38,42,44,46],axis = 0)
df = df.dropna(axis=1, how = 'all')
df = df.T
df.columns = df.iloc[0] #promote header but doesn't quite drop the rest
df_PCH = df.drop("Usina",axis=0)
df_PCH.index = pd.to_datetime(df_PCH.index, format='%Y%m%d', errors='ignore')

df = pd.read_excel('U:\\Comercializacao\\11. Geração\\Base de Dados.xlsm', sheet_name='Dados EOL',skiprows =1)
df = df.drop(["Cód","Nome Usina_BE","Agente","SAP"],axis=1)
df = df.dropna(axis = 0, how = 'all')
df = df.dropna(axis=1, how = 'all')
df = df.drop(labels=[45],axis = 0)
df.iloc[28,53] = np.nan 
# deletar a linha de totalizado!!!!
df = df.T
df.columns = df.iloc[0]
df_EOL = df.drop("Usina",axis=0) 
df_EOL.index = pd.to_datetime(df_EOL.index, format='%Y%m%d', errors='ignore')
df_EOL.columns.name='Mes'

df = pd.read_excel('U:\\Comercializacao\\11. Geração\\Base de Dados.xlsm', sheet_name='Dados Bio',skiprows =1)
df = df.drop(["Cód","Nome Usina_BE","Agente","SAP"],axis=1)
df = df.dropna(axis = 0, how = 'all')
df = df.dropna(axis=1, how = 'all')
df = df.drop(labels=[8,9,36],axis = 0)
# deletar a linha de totalizado!!!!
df = df.T
df.columns = df.iloc[0]
df_BIO = df.drop("Usina",axis=0) 
df_BIO.index = pd.to_datetime(df_BIO.index, format='%Y%m%d', errors='ignore')
df_BIO.columns.name='Mes'

df = pd.read_excel('U:\\Comercializacao\\11. Geração\\Base de Dados.xlsm', sheet_name='Dados SOLAR',skiprows =1)
df = df.drop(["Cód","Nome Usina_BE","Agente","Grupo","SAP"],axis=1)
df = df.dropna(axis = 0, how = 'all')
df = df.dropna(axis=1, how = 'all')
df = df.T
df.columns = df.iloc[0]
df_SOL = df.drop("Usina",axis=0) 
df_SOL.index = pd.to_datetime(df_SOL.index, format='%Y%m%d', errors='ignore')
df_SOL.columns.name='Mes'

df_final=pd.concat([df_PCH,df_EOL,df_BIO,df_SOL], axis=1)
df_final.index.name='Mes'
df_final = df_final.loc[df_final.index[0]:data_final,:]


df3 = pd.read_excel('codes.xlsx', sheet_name='Plan1')


df_final.columns = df3["Mês"]
df_final.columns


df_final = df_final.astype(float)
df_final.dtypes
filename1 = "GER-" + datetime.datetime.now().strftime("%d-%m-%Y") +".csv"
df_final.to_csv(filename1, date_format = "%d/%m/%Y", sep=';', na_rep='', decimal=',',float_format='%.3f')