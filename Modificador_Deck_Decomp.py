# Atualizador para o Decomp 

ARQUIVO_DAGDER = open('C:\\Users\\Joseeustaquio\\Downloads\\PMO_deck_preliminar\\DEC_ONS_072018_RV0_VE\\DADGER.RV1', "r+") # abre o arquivo DADGER.RV0
LINHAS_DADGER = ARQUIVO_DAGDER.readlines() # le todas as linhas do DAGDER.RVO, incluindo fins de linhas
LINHAS_TOTAIS = 0 # inicializa o contador de linhas

LINHAS_COM_MP = [] # diferente 
LINHAS_COM_MT = [] # diferente
LINHAS_COM_FD = [] # diferente 
LINHAS_COM_VE = [] # diferente
LINHAS_COM_TI = [] # diferente 
LINHAS_COM_RQ = [] # diferente

BLOCOS_RESTRICOES = ["FI", "LU", "FU", "LV", "CV", "LQ", "CQ"]

for linhas in LINHAS_DADGER: # corre todas as linhas do script 
    # CT 
    if (linhas[0:2]) == "CT":
        placeholder_MP = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder_MP_1 = LINHAS_DADGER[LINHAS_TOTAIS + 1]
        if int(placeholder_MP[25]) == 1:
            if placeholder_MP_1[0:2] == "CT" and placeholder_MP[4:7] == placeholder_MP_1[4:7]:
                    if int(placeholder_MP_1[25]) == 2:
                        placeholder_MP = "&" + placeholder_MP
                        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder_MP
                    else:
                        pass
            else:
                pass
        else:
            placeholder_MP = (placeholder_MP[:25] + str(int(placeholder_MP[25]) - 1) + placeholder_MP[26:])  
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder_MP 
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
           LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder 
        else:
            placeholder = (placeholder[:5] + str(int(placeholder[5]) - 1) + placeholder[6:])
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder 

    elif (linhas[0:2]) == "RE":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if (int(placeholder[15]) == 1): # revisar conforme a revisão 
           LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder
        else:
            placeholder = (placeholder[:15] + str(int(placeholder[15]) - 1) + placeholder[16:])
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder     

    elif (linhas[0:2]) == "HV":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if (int(placeholder[15]) == 1): # revisar conforme a revisão 
           LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder
        else:
            placeholder = (placeholder[:15] + str(int(placeholder[15]) - 1) + placeholder[16:])
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder      

    elif (linhas[0:2]) == "HQ":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if (int(placeholder[15]) == 1): # revisar conforme a revisão 
           LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder
        else:
            placeholder = (placeholder[:15] + str(int(placeholder[15]) - 1) + placeholder[16:])
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder          
            
    # BLOCO PARA RESTRIÇÕES (LU, FU, LV, CV, HQ, LQ, CQ)
    else:
        for bloco in BLOCOS_RESTRICOES:
            if (linhas[0:2]) == bloco:
                placeholder_MP = LINHAS_DADGER[LINHAS_TOTAIS] 
                placeholder_MP_1 = LINHAS_DADGER[LINHAS_TOTAIS + 1]
                if int(placeholder_MP[10]) == 1:
                    if placeholder_MP_1[0:2] == bloco and placeholder_MP[4:7] == placeholder_MP_1[4:7]:
                        if int(placeholder_MP_1[10]) == 2:
                            placeholder_MP = "&" + placeholder_MP
                            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder_MP
                        else:
                            pass
                    else:
                        pass
                else:
                    placeholder_MP = (placeholder_MP[:10] + str(int(placeholder_MP[10]) - 1) + placeholder_MP[11:])  
                    LINHAS_DADGER[LINHAS_TOTAIS] = placeholder_MP 
    
    LINHAS_TOTAIS += 1  

ARQUIVO_DAGDER.close()

NOVO_ARQUIVO_DADGER = open("C:\\Users\\Joseeustaquio\\Downloads\\PMO_deck_preliminar\\DEC_ONS_072018_RV0_VE\\DADGER.RV2", "w") # um novo arquivo do DADGER.RVO passa a ser criado
NOVO_ARQUIVO_DADGER.writelines(LINHAS_DADGER)
NOVO_ARQUIVO_DADGER.close()

# Fim do Programa 
