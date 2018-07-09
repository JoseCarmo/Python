# Atualizador para o Decomp 

ARQUIVO_DAGDER = open('C:\\Users\\Joseeustaquio\\Downloads\\PMO_deck_preliminar\\DEC_ONS_072018_RV0_VE\\DADGER.RV0', "r+") # abre o arquivo DADGER.RV0
LINHAS_DADGER = ARQUIVO_DAGDER.readlines() # le todas as linhas do DAGDER.RVO, incluindo fins de linhas
LINHAS_TOTAIS = 0 # inicializa o contador de linhas

LINHAS_COM_MP = [] # diferente 
LINHAS_COM_MT = [] # diferente
LINHAS_COM_FD = [] # diferente 
LINHAS_COM_VE = [] # diferente
LINHAS_COM_TI = [] # diferente 
LINHAS_COM_RQ = [] # diferente

BLOCOS_RESTRICOES = ["RE", "LU", "FU", "HV", "LV", "CV", "HQ", "LQ", "CQ"]

for linhas in LINHAS_DADGER: # corre todas as linhas do script 
    # CT 
    if (linhas[0:2]) == "CT":
        print('1eiro if')
        placeholder_MP = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder_MP_1 = LINHAS_DADGER[LINHAS_TOTAIS + 1]
        print(LINHAS_TOTAIS)
        print(placeholder_MP[25])
        print(placeholder_MP)
        print(linhas)
        if int(placeholder_MP[25]) == 1:
            print("2gundo if")
            if placeholder_MP_1[0:2] == "CT" and placeholder_MP[4:7] == placeholder_MP_1[4:7]:
                    print("3eiro if")
                    if int(placeholder_MP_1[25]) == 2:
                        placeholder_MP = "&" + placeholder_MP
                        placeholder_MP_1 = (placeholder_MP_1[:25] + str(int(placeholder_MP_1[25]) - 1) + placeholder_MP_1[26:])
                        LINHAS_TOTAIS += 1 
                    elif int(placeholder_MP_1[25]) > 2:
                         placeholder_MP = (placeholder_MP[:25] + str(int(placeholder_MP[25]) - 1) + placeholder_MP[26:])
                    else:
                        pass
            else:
                pass
        else:
            placeholder_MP = (placeholder_MP[:25] + str(int(placeholder_MP[25]) - 1) + placeholder_MP[26:])   
    # MP
    if (linhas[0:2]) == "MP":
        placeholder_MP = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder_MP = (placeholder_MP[:9] + placeholder_MP[14:])
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder_MP
    # MT
    elif (linhas[0:2]) == "MT":
        placeholder_MP = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder_MP = (placeholder_MP[:14] + placeholder_MP[19:])
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder_MP
    # FD
    elif (linhas[0:2]) == "FD":
        placeholder_MP = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder_MP = (placeholder_MP[:9] + placeholder_MP[14:])
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder_MP    
    # VE
    elif (linhas[0:2]) == "VE":
        placeholder_MP = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder_MP = (placeholder_MP[:9] + placeholder_MP[14:])
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder_MP
    # TI
    elif (linhas[0:2]) == "TI":
        placeholder_RQ = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder_RQ = (placeholder_RQ[:11] + placeholder_RQ[16:])
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder_RQ
    # RQ
    elif (linhas[0:2]) == "RQ":
        placeholder_RQ = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder_RQ = (placeholder_RQ[:11] + placeholder_RQ[16:])
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder_RQ 
    # PQ
    elif (linhas[0:2]) == "PQ":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if (int(placeholder[20]) == 1):
            pass
        else:
            placeholder = (placeholder[:20] + str(int(placeholder[20]) - 1) + placeholder[21:])
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder      
    # IT
    elif (linhas[0:2]) == "IT":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if (int(placeholder[5]) == 1):
            pass
        else:
            placeholder = (placeholder[:5] + str(int(placeholder[5]) - 1) + placeholder[6:])
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder
    # IA
    elif (linhas[0:2]) == "IA":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if (int(placeholder[5]) == 1):
            pass
        else:
            placeholder = (placeholder[:5] + str(int(placeholder[5]) - 1) + placeholder[6:])
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder      
    # DP
    elif (linhas[0:2]) == "DP":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if (int(placeholder[5]) == 1): # revisar conforme a revisão 
           LINHAS_DADGER[LINHAS_TOTAIS] = ''
        else:
            placeholder = (placeholder[:5] + str(int(placeholder[5]) - 1) + placeholder[6:])
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder         
            
    # BLOCO PARA RESTRIÇÕES (RE, LU, FU, HV, LV, CV, HQ, LQ, CQ)
    else:
        for bloco in BLOCOS_RESTRICOES:
            if (linhas[0:2]) == bloco:
                    placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
                    if (int(placeholder[10]) == 1):
                        pass
                    else:
                        placeholder = (placeholder[:10] + str(int(placeholder[10]) - 1) + placeholder[11])
                        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder
    LINHAS_TOTAIS += 1  

ARQUIVO_DAGDER.close()

NOVO_ARQUIVO_DADGER = open("C:\\Users\\Joseeustaquio\\Downloads\\PMO_deck_preliminar\\DEC_ONS_072018_RV0_VE\\DADGER.RV1", "w") # um novo arquivo do DADGER.RVO passa a ser criado
NOVO_ARQUIVO_DADGER.writelines(LINHAS_DADGER)
NOVO_ARQUIVO_DADGER.close()

# Fim do Programa 




