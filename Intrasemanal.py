""" ~ ~ ~ Atualizador do arquivo DADGER.RVX, parte do modelo de otimização de despacho hidrotérmico Decomp ~ ~ ~
Dentro do contexto do Planejamento Mensal de Operações (PMO), ocorrem revisões semanais (rv) que são acrescentadas à revisão inicial rv0
Essa rotina automatiza alterações na estrutura do código do DADGER.RVx, parte do modelo DECOMP 
A leitura do arquivo ocorre com o seguinte comando: 
    arquivo = open('caminho para aquivo alvo', 'modo de leitura') // a arquivo alvo é lido pelo Python e é armazenado dentro de uma lista onde 
    cada item da lista é uma linha da lista. 
No nosso exemplo, se o arquivo alvo possui n linhas:
    arquivo = [linha_1 do arquivo alvo, linha_2 do arquivo alvo, ..., linha_n do arquivo alvo]
A seguir, com o conhecimento do formato do DADGER.RVX, é possível 'parsear' todo o arquivo em busca dos valores a serem alterados e/ou 
comentados para a formação de uma próxima revisão.

Melhorias: talvez um menuzinho para colocar o caminho e adicionar o caráter iterativo das execuções, isto é, de rev 0 até uma rev 4 
 """
from FuncoesIntrasemanal import *

# vere estrutura da árvore, usar 259

numero_revisao = 3 

caminho_dadger = "H:\\BC Mesa\\middle\\Dados de Rodadas\\Agosto\\rv4\\DEC_ONS_082018_RV3_VE"

ARQUIVO_DAGDER = open(caminho_dadger + '/DADGER.RV%s' %numero_revisao, "r+") # abre o arquivo DADGER.rvX
LINHAS_DADGER = ARQUIVO_DAGDER.readlines() # lê todas as linhas do DAGDER.RVO, incluindo fins de linhas
LINHAS_TOTAIS = 0 # inicializa o contador de linhas
BLOCOS_RESTRICOES = ["FI", "LU", "FU", "LV", "CV", "LQ", "CQ"] # VER SE HQ ENTRA MESMO 

for linhas in LINHAS_DADGER: # corre todas as linhas do script 
    # CT 
    if linhas[0:2] == "CT":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_CT(LINHAS_DADGER[LINHAS_TOTAIS], LINHAS_DADGER[LINHAS_TOTAIS + 1]))

    # MP ou FD ou VE 
    elif linhas[0:2] == "MP" or linhas[0:2] == "FD" or linhas[0:2] == "VE":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_MP_FD_VE(linhas))

    # MT
    elif linhas[0:2] == "MT":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_MT(linhas))

    # RQ ou TI 
    elif linhas[0:2] == "RQ" or linhas[0:2] == "TI":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_RQ_TI(linhas))

    # PQ
    elif linhas[0:2] == "PQ":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_PQ(linhas))     

    # IT ou IA 
    elif linhas[0:2] == "IT" or linhas[0:2] == "IA":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_IT_IA(linhas))

    # DP
    elif linhas[0:2] == "FC":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_FC(linhas))   

    # FC
    elif linhas[0:2] == "DP":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_DP(linhas))       

    # AC
    elif linhas[0:2] == "AC":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_AC(linhas))

    # RE ou HV ou RE 
    elif linhas[0:2] == "RE" or linhas[0:2] == "HV" or linhas[0:2] == "HQ":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_HQ_HV_RE(linhas)) 

    # ALTERA NOME DO PREVS
    elif linhas[39:44] == "PREVS":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_PREVS(linhas))
            
    # DT
    elif linhas[0:2] == "DT":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_DT(linhas))

    # ÁRVORE
    elif linhas[0:21] == "& ESTRUTURA DA ARVORE":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_Arvore(linhas))

    # RESTRIÇÕES (LU, FU, LV, CV, HQ, LQ, CQ)
    else:
        for bloco in BLOCOS_RESTRICOES:
            if linhas[0:2] == bloco:
                LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_Outras_Restricoes(LINHAS_DADGER[LINHAS_TOTAIS], LINHAS_DADGER[LINHAS_TOTAIS + 1], bloco))
            else:
                LINHAS_DADGER[LINHAS_TOTAIS] = str(linhas)          
    
    LINHAS_TOTAIS += 1  

ARQUIVO_DAGDER.close()
 
NOVO_ARQUIVO_DADGER = open(caminho_dadger + '/DADGER.RV%s' %(numero_revisao + 1), "w") # um novo arquivo do DADGER.RVx + 1 é criado
NOVO_ARQUIVO_DADGER.writelines(LINHAS_DADGER)
NOVO_ARQUIVO_DADGER.close()