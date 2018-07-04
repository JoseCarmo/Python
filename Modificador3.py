# Atualizador de Manutencao Programada (MP) para o Decomp 

ARQUIVO_DAGDER = open('C:\\Users\\Joseeustaquio\\Downloads\\PMO_deck_preliminar\\DEC_ONS_072018_RV0_VE\\DADGER.RV0', "r+") # abre o arquivo DADGER.RV0
LINHAS_DADGER = ARQUIVO_DAGDER.readlines() # le todas as linhas do DAGDER.RVO, incluindo fins de linhas

LINHAS_TOTAIS = 0 # inicializa o contador de linhas

LINHAS_COM_MP = [] # diferente 
LINHAS_COM_MT = [] # diferente
LINHAS_COM_FD = [] # diferente 
LINHAS_COM_VE = [] # diferente
LINHAS_COM_TI = [] # diferente 
LINHAS_COM_RQ = [] # diferente
LINHAS_COM_RE = [] # igual
LINHAS_COM_LU = [] # igual
LINHAS_COM_FU = [] # igual
LINHAS_COM_FI = [] # igual
LINHAS_COM_FT = [] # igual
LINHAS_COM_HV = [] # igual 
LINHAS_COM_LV = [] # igual 
LINHAS_COM_CV = [] # igual 
LINHAS_COM_CQ = [] # igual 
LINHAS_COM_HQ = [] # igual 
LINHAS_COM_RI = [] # igual 
LINHAS_COM_LQ = [] # igual 

BLOCOS_RESTRICOES = ["RE", "FU", "LU", "FI", "FT", "HV", "LV", "CV", "CQ", "HQ", "LQ"]

# BLOCO MT
for linhas in LINHAS_DADGER: # identifica todas as linhas que fazer parte do bloco MP
    if (linhas[0:2]) == "MP":
        LINHAS_COM_MP.append(LINHAS_TOTAIS)
    LINHAS_TOTAIS += 1 

for linhas_MP in LINHAS_COM_MP: # retira uma semana das linhas do bloco MP, i.e. as desloca para a esquerda 
    placeholder_MP = LINHAS_DADGER[linhas_MP] 
    placeholder_MP = (placeholder_MP[:9] + placeholder_MP[14:])
    LINHAS_DADGER[linhas_MP] = placeholder_MP

# BLOCO MT
LINHAS_TOTAIS = 0

for linhas in LINHAS_DADGER: # identifica todas as linhas que fazer parte do bloco MP
    if (linhas[0:2]) == "MT":
        LINHAS_COM_MT.append(LINHAS_TOTAIS)
    LINHAS_TOTAIS += 1 

for linhas_MT in LINHAS_COM_MT: # retira uma semana das linhas do bloco MP, i.e. as desloca para a esquerda 
    placeholder_MT = LINHAS_DADGER[linhas_MT] 
    if (int(placeholder_MT[10]) == 6):
        placeholder_MT = (placeholder_MT[:10] + str(int(placeholder_MT[10])) + str('   ') + placeholder_MT[19:])
        LINHAS_DADGER[linhas_MT] = placeholder_MT
    else:
        placeholder_MT = (placeholder_MT[:10] + str(int(placeholder_MT[10]) + 1) + str('   ') + placeholder_MT[19:])
        LINHAS_DADGER[linhas_MT] = placeholder_MT

# BLOCO FD
LINHAS_TOTAIS = 0

for linhas in LINHAS_DADGER: # identifica todas as linhas que fazer parte do bloco MP
    if (linhas[0:2]) == "FD":
        LINHAS_COM_FD.append(LINHAS_TOTAIS)
    LINHAS_TOTAIS += 1 

for linhas_FD in LINHAS_COM_FD: # retira uma semana das linhas do bloco MP, i.e. as desloca para a esquerda 
    placeholder_FD = LINHAS_DADGER[linhas_FD] 
    placeholder_FD = (placeholder_FD[:9] + placeholder_FD[14:])
    LINHAS_DADGER[linhas_FD] = placeholder_FD

# BLOCO VE
LINHAS_TOTAIS = 0

for linhas in LINHAS_DADGER: # identifica todas as linhas que fazer parte do bloco MP
    if (linhas[0:2]) == "VE":
        LINHAS_COM_VE.append(LINHAS_TOTAIS)
    LINHAS_TOTAIS += 1 

for linhas_VE in LINHAS_COM_VE: # retira uma semana das linhas do bloco MP, i.e. as desloca para a esquerda 
    placeholder_VE = LINHAS_DADGER[linhas_VE] 
    placeholder_VE = (placeholder_VE[:9] + placeholder_VE[14:])
    LINHAS_DADGER[linhas_VE] = placeholder_VE

# BLOCO RQ - VER OS SINAIS DE MENOS
LINHAS_TOTAIS = 0

for linhas in LINHAS_DADGER: # identifica todas as linhas que fazer parte do bloco MP
    if (linhas[0:2]) == "RQ":
        LINHAS_COM_RQ.append(LINHAS_TOTAIS)
    LINHAS_TOTAIS += 1 

for linhas_RQ in LINHAS_COM_RQ: # retira uma semana das linhas do bloco MP, i.e. as desloca para a esquerda 
    placeholder_RQ = LINHAS_DADGER[linhas_RQ] 
    placeholder_RQ = (placeholder_RQ[:11] + placeholder_RQ[16:])
    LINHAS_DADGER[linhas_RQ] = placeholder_RQ

# BLOCO RE - RESTRICOES ELÉTRICAS 
LINHAS_TOTAIS = 0

for linhas in LINHAS_DADGER: # identifica todas as linhas que fazer parte do bloco MP
    if (linhas[0:2]) == "RE":
        LINHAS_COM_RE.append(LINHAS_TOTAIS)
    LINHAS_TOTAIS += 1 

for linhas_RE in LINHAS_COM_RE: # retira uma semana das linhas do bloco MP, i.e. as desloca para a esquerda 
    placeholder_RE = LINHAS_DADGER[linhas_RE] 
    if (int(placeholder_RE[10]) == 6):
        pass
    else:
        placeholder_RE = (placeholder_RE[:10] + str(int(placeholder_RE[10]) + 1) + str(' ') + placeholder_RE[11:])
        LINHAS_DADGER[linhas_RE] = placeholder_RE

# BLOCO LU - RESTRICOES ELÉTRICAS
LINHAS_TOTAIS = 0

for linhas in LINHAS_DADGER: # identifica todas as linhas que fazer parte do bloco MP
    if (linhas[0:2]) == "LU":
        LINHAS_COM_RE.append(LINHAS_TOTAIS)
    LINHAS_TOTAIS += 1 

for linhas_LU in LINHAS_COM_LU: # retira uma semana das linhas do bloco MP, i.e. as desloca para a esquerda 
    placeholder_LU = LINHAS_DADGER[linhas_LU] 
    if (int(placeholder_LU[10]) == 6):
        pass
    else:
        placeholder_LU = (placeholder_LU[:10] + str(int(placeholder_LU[10]) + 1) + str(' ') + placeholder_LU[11:])
        LINHAS_DADGER[linhas_LU] = placeholder_LU

# BLOCO FU - RESTRIÇÕES ELÉTRICAS  
LINHAS_TOTAIS = 0

for linhas in LINHAS_DADGER: # identifica todas as linhas que fazer parte do bloco MP
    if (linhas[0:2]) == "FU":
        LINHAS_COM_RE.append(LINHAS_TOTAIS)
    LINHAS_TOTAIS += 1 

for linhas_FU in LINHAS_COM_FU: # retira uma semana das linhas do bloco MP, i.e. as desloca para a esquerda 
    placeholder_FU = LINHAS_DADGER[linhas_FU] 
    if (int(placeholder_FU[10]) == 6):
        pass
    else:
        placeholder_FU = (placeholder_FU[:10] + str(int(placeholder_FU[10]) + 1) + str(' ') + placeholder_FU[11:])
        LINHAS_DADGER[linhas_FU] = placeholder_FU

# BLOCO FI - RESTRIÇÕES ELÉTRICAS  
LINHAS_TOTAIS = 0

for linhas in LINHAS_DADGER: # identifica todas as linhas que fazer parte do bloco MP
    if (linhas[0:2]) == "FI":
        LINHAS_COM_RI.append(LINHAS_TOTAIS)
    LINHAS_TOTAIS += 1 

for linhas_FI in LINHAS_COM_FI: # retira uma semana das linhas do bloco MP, i.e. as desloca para a esquerda 
    placeholder_FI = LINHAS_DADGER[linhas_FI] 
    if (int(placeholder_FI[10]) == 6):
        pass
    else:
        placeholder_FI = (placeholder_FI[:10] + str(int(placeholder_FI[10]) + 1) + str(' ') + placeholder_FI[11:])
        LINHAS_DADGER[linhas_FI] = placeholder_FI


# BLOCO FT - RESTRIÇÕES ELÉTRICAS  
LINHAS_TOTAIS = 0

for linhas in LINHAS_DADGER: # identifica todas as linhas que fazer parte do bloco MP
    if (linhas[0:2]) == "FT":
        LINHAS_COM_FT.append(LINHAS_TOTAIS)
    LINHAS_TOTAIS += 1 

for linhas_FT in LINHAS_COM_FT: # retira uma semana das linhas do bloco MP, i.e. as desloca para a esquerda 
    placeholder_FT = LINHAS_DADGER[linhas_FT] 
    if (int(placeholder_FT[10]) == 6):
        pass
    else:
        placeholder_FT = (placeholder_FT[:10] + str(int(placeholder_FT[10]) + 1) + str(' ') + placeholder_FT[11:])
        LINHAS_DADGER[linhas_FT] = placeholder_FT

# BLOCO HQ - RESTRIÇÕES ELÉTRICAS  
LINHAS_TOTAIS = 0

for linhas in LINHAS_DADGER: # identifica todas as linhas que fazer parte do bloco MP
    if (linhas[0:2]) == "HQ":
        LINHAS_COM_FT.append(LINHAS_TOTAIS)
    LINHAS_TOTAIS += 1 

for linhas_HQ in LINHAS_COM_HQ: # retira uma semana das linhas do bloco MP, i.e. as desloca para a esquerda 
    placeholder_HQ = LINHAS_DADGER[linhas_HQ] 
    if (int(placeholder_HQ[10]) == 6):
        pass
    else:
        placeholder_HQ = (placeholder_HQ[:10] + str(int(placeholder_HQ[10]) + 1) + str(' ') + placeholder_HQ[11:])
        LINHAS_DADGER[linhas_HQ] = placeholder_HQ

# BLOCO LQ - RESTRIÇÕES ELÉTRICAS  
LINHAS_TOTAIS = 0

for linhas in LINHAS_DADGER: # identifica todas as linhas que fazer parte do bloco MP
    if (linhas[0:2]) == "LQ":
        LINHAS_COM_LQ.append(LINHAS_TOTAIS)
    LINHAS_TOTAIS += 1 

for linhas_LQ in LINHAS_COM_LQ: # retira uma semana das linhas do bloco MP, i.e. as desloca para a esquerda 
    placeholder_LQ = LINHAS_DADGER[linhas_LQ] 
    if (int(placeholder_LQ[10]) == 6):
        pass
    else:
        placeholder_LQ = (placeholder_LQ[:10] + str(int(placeholder_LQ[10]) + 1) + str(' ') + placeholder_LQ[11:])
        LINHAS_DADGER[linhas_LQ] = placeholder_LQ

# BLOCO CQ - RESTRIÇÕES ELÉTRICAS  
LINHAS_TOTAIS = 0

for linhas in LINHAS_DADGER: # identifica todas as linhas que fazer parte do bloco MP
    if (linhas[0:2]) == "CQ":
        LINHAS_COM_CQ.append(LINHAS_TOTAIS)
    LINHAS_TOTAIS += 1 

for linhas_CQ in LINHAS_COM_CQ: # retira uma semana das linhas do bloco MP, i.e. as desloca para a esquerda 
    placeholder_CQ = LINHAS_DADGER[linhas_CQ] 
    if (int(placeholder_CQ[10]) == 6):
        pass
    else:
        placeholder_CQ = (placeholder_CQ[:10] + str(int(placeholder_CQ[10]) + 1) + str(' ') + placeholder_CQ[11:])
        LINHAS_DADGER[linhas_CQ] = placeholder_CQ

# BLOCO TI - VER OS SINAIS DE MENOS
LINHAS_TOTAIS = 0

for linhas in LINHAS_DADGER: # identifica todas as linhas que fazer parte do bloco MP
    if (linhas[0:2]) == "TI":
        LINHAS_COM_TI.append(LINHAS_TOTAIS)
    LINHAS_TOTAIS += 1 

for linhas_TI in LINHAS_COM_TI: # retira uma semana das linhas do bloco MP, i.e. as desloca para a esquerda 
    placeholder_TI = LINHAS_DADGER[linhas_TI] 
    placeholder_TI = (placeholder_TI[:11] + placeholder_TI[16:])
    LINHAS_DADGER[linhas_TI] = placeholder_TI

ARQUIVO_DAGDER.close()

NOVO_ARQUIVO_DADGER = open("C:\\Users\\Joseeustaquio\\Downloads\\PMO_deck_preliminar\\DEC_ONS_072018_RV0_VE\\DADGER1.RV0", "w") # um novo arquivo do DADGER.RVO passa a ser criado
NOVO_ARQUIVO_DADGER.writelines(LINHAS_DADGER)
NOVO_ARQUIVO_DADGER.close()

# Fim do Programa 




