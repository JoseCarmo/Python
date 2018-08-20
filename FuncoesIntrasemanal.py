# Definicao das funcoes a serem usadas no Intrasemanal.py

if __name__ == "__main__":
    print ("O arquivo com as funções para atualização intrasemanal do deck foi carregado")

def Atualizar_MP_FD_VE(linha):
        linha = (linha[:9] + linha[14:])
        return linha

def Atualizar_RQ_TI(linha):
        linha = (linha[:11] + linha[16:])
        return linha

def Atualizar_HQ_HV_RE(linha): 
        if (int(linha[15]) == 1): 
           linha = "&" + linha
        else:
            linha = (linha[:15] + str(int(linha[15]) - 1) + linha[16:])
        return linha 

def Atualizar_IT_IA(linha): 
        if (int(linha[5]) == 1):
            pass
        else:
            linha = (linha[:5] + str(int(linha[5]) - 1) + linha[6:])
        return linha 

def Atualizar_MT(linha): 
        linha = (linha[:14] + linha[19:])
        return linha

def Atualizar_PQ(linha): 
        if (int(linha[20]) == 1):
            pass 
        else:
            linha = (linha[:20] + str(int(linha[20]) - 1) + linha[21:])
        return linha      

def Atualizar_DP(linha): 
        if (int(linha[5]) == 1): # revisar conforme a revisão 
           linha = "&" + linha 
        else:
            linha = (linha[:5] + str(int(linha[5]) - 1) + linha[6:])
        return linha  

def Atualizar_Outras_Restricoes(linha_atual, linha_seguinte, bloco):
        if int(linha_atual[10]) == 1:
            if linha_seguinte[0:2] == bloco and linha_atual[4:7] == linha_seguinte[4:7]:
                if int(linha_seguinte[10]) == 2:
                    linha_atual = "&" + linha_atual
                    return linha_atual
                else:
                    pass
            else:
                pass
        else:
            linha_atual = (linha_atual[:10] + str(int(linha_atual[10]) - 1) + linha_atual[11:])  
        return str(linha_atual) 

def Atualizar_CT(linha_atual, linha_seguinte):
        if int(linha_atual[25]) == 1:
            if linha_seguinte[0:2] == "CT" and linha_atual[3:8] == linha_seguinte[3:8]:
                    if int(linha_seguinte[25]) == 2:
                        print("aqui")
                        linha_atual = "&" + linha_atual
                        return str(linha_atual)
        else:
            linha_atual = (linha_atual[:25] + str(int(linha_atual[25]) - 1) + linha_atual[26:])   
        return str(linha_atual)

def Atualizar_FC(linha):
        if(linha[4:10] == "NEWV21"):
            linha = linha[:14] + "cortesh.dat" + "\n"
        if(linha[4:10] == "NEWCUT"):
            linha = linha[:14]  + "cortes.dat" +  "\n"  
        return linha

def Atualizar_AC(linha):
        if linha[0:2] == "AC" and len(linha) > 74:
            if int(linha[74]) == 1:
                linha = "&" + linha
            else:
                linha = linha[:74] + str(int(linha[74]) - 1) + "\n"
        return str(linha)

def Atualizar_PREVS(linha):
        linha = linha[:47] + str(int(linha[47]) + 1) + "\n"
        return str(linha)

def Atualizar_DT(linha):
    from datetime import timedelta, date

    def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

    lista_datas = []

    start_date = date(2018, 6, 30)
    end_date = date(2020, 7, 31)
    for single_date in daterange(start_date, end_date):
        lista_datas.append(single_date.strftime("%d   %m   %Y"))

    DIA_DADGER = linha[4:18]

    for dia in lista_datas:
        if DIA_DADGER == dia:
            DIA_DADGER = lista_datas[lista_datas.index(dia, 0, len(lista_datas)) + 7]
            linha = linha[:4] + DIA_DADGER + "\n"
            break             
                
    return str(linha)

# Fim