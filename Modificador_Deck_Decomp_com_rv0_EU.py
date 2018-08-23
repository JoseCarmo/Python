""" Atualizador do arquivo DADGER.RVX, parte do modelo de otimização de despacho hidrotérmico Decomp

UH -> ok (OK) ENTENDI 
CT -> ult. estagio (sem manutt) (OK) ENTENDI 
DP -> nw + patamar Zé (OK)
PQ -> ult. estagio (OK) ENTENDI 
IA & IT -> ultimo estagio (OK) SUSPENDE OS INTERCÂMBIOS NO IT E IA FICA NO ULTIMO ESTAGIO 
MP e MT -> valores de colunas por estagios (OK) ENTENDI
FD -> ok (ver numeros das semanas e ajustar OK) ENTENDI
VE -> ok (ver numeros das semanas  e ajustar OK) ENTENDI
Restrições -> ver ultimos valores/ analisar (ATENÇÃO)
Alterar JUSMED e COTVOL (ATENÇAO) (OK)
Bloco TI -> replicar ultimos valores (OK) ENTENDI
"""
numero_revisao = 0 #numero da revisão usada para a revisão 0 do próximo mês

caminho_dadger = "H:\\BC Mesa\\middle\\Dados de Rodadas\\Agosto\\rv4\\DEC_ONS_082018_RV3_VE"

ARQUIVO_DAGDER = open(caminho_dadger + "\\DADGER.RV%s" %numero_revisao, "r+") # abre o arquivo DADGER.rvX
LINHAS_DADGER = ARQUIVO_DAGDER.readlines() # lê todas as linhas do DAGDER.RVO, incluindo fins de linhas
LINHAS_TOTAIS = 0 # inicializa o contador de linhas
BLOCOS_RESTRICOES = ["FI", "LU", "FU", "LV", "CV", "LQ", "CQ"]

for linhas in LINHAS_DADGER: # corre todas as linhas do script 
    # PQ 
    if (linhas[0:2]) == "PQ":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if int(placeholder[20]) != (6 - numero_revisao):
            LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder                       
        else:
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder[:20] + '1' + placeholder[21:]
    # CT
    elif (linhas[0:2]) == "CT":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if int(placeholder[25]) != (6 - numero_revisao):
            LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder                       
        else:
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder[:25] + '1' + placeholder[26:]
    # IT
    elif (linhas[0:2]) == "IT":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if int(placeholder[5]) != (6 - numero_revisao):
            LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder                       
        else:
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder[:5] + '1' + placeholder[6:]     
    # IA 
    elif (linhas[0:2]) == "IA":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if int(placeholder[5]) != (6 - numero_revisao):
            LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder                       
        else:
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder[:5] + '1' + placeholder[6:]               
    # MP
    elif (linhas[0:2]) == "MP":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder = placeholder[:9] + (6)*"1.000" + "\n"
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder
    # MT
    elif (linhas[0:2]) == "MT":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder = placeholder[:14] + (6)*"1.000" + "\n"
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder    
    # FD
    elif (linhas[0:2]) == "FD":
        if numero_revisao == 0:
            placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
            placeholder = (placeholder[:9] + (6)*placeholder[34:39] + "\n")
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder    
    # VE
    elif (linhas[0:2]) == "VE":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder = (placeholder[:9] + (6)*placeholder[34:39] +'\n')
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder
    # TI
    elif (linhas[0:2]) == "TI":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder = (placeholder[:10] + 6*placeholder[34:39] +'\n' )
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder
    # RQ
    #elif (linhas[0:2]) == "RQ":
     #   placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
      #  placeholder = (placeholder[:10] + 5*placeholder[37:39] +'\n' )
       # LINHAS_DADGER[LINHAS_TOTAIS] = placeholder
    # IT
    elif (linhas[0:2]) == "IT":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if (int(placeholder[5]) == 1):
            pass
        else:
            placeholder = (placeholder[:5] + str(int(placeholder[5]) - 1) + placeholder[6:])
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder
    # RE
    elif (linhas[0:2]) == "RE":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if (int(placeholder[15]) == 1): 
           LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder
        else:
            placeholder = (placeholder[:15] + '6' + placeholder[16:])
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder     

    elif (linhas[0:2]) == "HV":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if (int(placeholder[15]) == 1):  
           LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder
        else:
            placeholder = (placeholder[:15] + '6' + placeholder[16:])
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder       

    elif (linhas[0:2]) == "HQ":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if (int(placeholder[15]) == 1): 
           LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder
        else:
            placeholder = (placeholder[:15] + '6' + placeholder[16:])
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder         
            
    # BLOCO PARA RESTRIÇÕES (LU, FU, LV, CV, HQ, LQ, CQ)
    else:
        for bloco in BLOCOS_RESTRICOES:
            if (linhas[0:2]) == bloco:
                placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
                placeholder_1 = LINHAS_DADGER[LINHAS_TOTAIS + 1]
                if int(placeholder[10]) == 1:
                    if placeholder_1[0:2] == bloco and placeholder[4:7] == placeholder_1[4:7]:
                        if int(placeholder_1[10]) == 2:
                            placeholder = "&" + placeholder
                            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder
                        else:
                            pass
                    else:
                        pass
                else:
                    placeholder = (placeholder[:10] + str(int(placeholder[10]) - 1) + placeholder[11:])  
                    LINHAS_DADGER[LINHAS_TOTAIS] = placeholder 
    
    LINHAS_TOTAIS += 1  

ARQUIVO_DAGDER.close()

NOVO_ARQUIVO_DADGER = open(caminho_dadger + "\\DADGER2.RV%s" %numero_revisao, "w") # um novo arquivo do DADGER.RVx + 1 é criado
NOVO_ARQUIVO_DADGER.writelines(LINHAS_DADGER)
NOVO_ARQUIVO_DADGER.close()