# Definicao das funcoes a serem usadas no Intrasemanal.py

if __name__ == "__main__":
    print ("O arquivo com as funções para atualização intrasemanal do deck foi carregado")

def Atualizar_TG(linha_atual, linha_seguinte):
        if int(linha_atual[25]) == 1:
            if linha_seguinte[0:2] == "TG" and linha_atual[5:7] == linha_seguinte[5:7]:
                    if int(linha_seguinte[25]) == 2:
                        linha_atual = "&" + linha_atual
                        return str(linha_atual)
        else:
            linha_atual = (linha_atual[:25] + str(int(linha_atual[25]) - 1) + linha_atual[26:])   
        return str(linha_atual)

def Atualizar_GS(linha):
        if int(linha[5]) == 1:
            linha = linha[:9] + str(int(linha[9]) - 1) + linha[10:]     
        return str(linha)

def Atualizar_GL(linha_atual, linha_seguinte): 
        if int(linha_atual[15]) == 1:
            if linha_seguinte[0:2] == "GL" and linha_atual[5:7] == linha_seguinte[5:7]:
                    if int(linha_seguinte[15]) == 2:
                        linha_atual = "&" + linha_atual
                        return str(linha_atual)
        else:
            linha_atual = (linha_atual[:15] + str(int(linha_atual[15]) - 1) + linha_atual[16:])   
        return str(linha_atual)

# Fim