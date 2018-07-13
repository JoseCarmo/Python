""" Atualizador do arquivo DADGER.RVX, parte do modelo de otimização de despacho hidrotérmico Decomp

Dentro do contexto do Planejamento Mensal de Operações (PMO), ocorrem revisões semanais (rv) que são acrescentadas à revisão inicial rv0
Essa rotina automatiza alterações na estrutura do código do DADGER.RVx, parte do modelo DECOMP 
A leitura do arquivo ocorre com o seguinte comando: 
    arquivo = open('caminho para aquivo alvo', 'modo de leitura') // a arquivo alvo é lido pelo Python e é armazenado dentro de uma lista onde 
    cada item da lista é uma linha da lista. 

No nosso exemplo, se o arquivo alvo possui n linhas:
    arquivo = [linha_1 do arquivo alvo, linha_2 do arquivo alvo, ..., linha_n do arquivo alvo]

A seguir, com o conhecimento do formato do DADGER.RVX, é possível 'parsear' todo o arquivo em busca dos valores a serem alterados e/ou 
comentados para a formação de uma próxima revisão.

A interpretação do restante da estrutura lógica do programa é responsabilidade do leitor.

Revisao 0
==== x ====
rv0

UH -> ok (OK)
CT -> ult. estagio (sem manutt) (OK)
DP -> nw + patamar Zé (OK)
PQ -> ult. estagio (OK)
IA & IT -> ultimo estagio (OK)
MP e MT -> valores de colunas por estagios (OK)
FD -> ok (ver numeros das semanas e ajustar OK)
VE -> ok (ver numeros das semanas  e ajustar OK)
Restrições -> ver ultimos valores/ analisar (ATENÇÃO)
Alterar JUSMED e COTVOL (ATENÇAO) (OK)
Bloco TI -> replicar ultimos valores (OK)

"""

ARQUIVO_DAGDER = open('C:\\Users\\Joseeustaquio\\Downloads\\PMO_deck_preliminar\\REV AGOSTO\\DADGER.RV0', "r+") # abre o arquivo DADGER.rvX
LINHAS_DADGER = ARQUIVO_DAGDER.readlines() # lê todas as linhas do DAGDER.RVO, incluindo fins de linhas
LINHAS_TOTAIS = 0 # inicializa o contador de linhas
BLOCOS_RESTRICOES = ["FI", "LU", "FU", "LV", "CV", "LQ", "CQ"]

for linhas in LINHAS_DADGER: # corre todas as linhas do script 
    # AJUSTAR DE ACORDO COM A REVISÃO VIGENTE, POIS NEM SEMPRE VAI SER 6 
    # PQ 
    if (linhas[0:2]) == "PQ":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if int(placeholder[20]) != 6:
            LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder                       
        else:
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder[:20] + '1' + placeholder[21:]
    # CT
    elif (linhas[0:2]) == "CT":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if int(placeholder[25]) != 6:
            LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder                       
        else:
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder[:25] + '1' + placeholder[26:]
    # IT
    elif (linhas[0:2]) == "IT":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder 
    # IA 
    elif (linhas[0:2]) == "IA":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        if int(placeholder[5]) != 6:
            LINHAS_DADGER[LINHAS_TOTAIS] = "&" + placeholder                       
        else:
            LINHAS_DADGER[LINHAS_TOTAIS] = placeholder[:5] + '1' + placeholder[6:]               
    # MP
    elif (linhas[0:2]) == "MP":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder = placeholder[:9] + "1.0001.0001.0001.0001.0001.000 \n"
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder
    # MT
    elif (linhas[0:2]) == "MT":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder = placeholder[:14] + "1.0001.0001.0001.0001.0001.000 \n"
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder    
    # FD
    elif (linhas[0:2]) == "FD":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder = (placeholder[:9] + placeholder[14:])
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder    
    # VE
    elif (linhas[0:2]) == "VE":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder = (placeholder[:9] + placeholder[14:])
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder
    # TI
    elif (linhas[0:2]) == "TI":
        placeholder = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder = (placeholder[:10] + placeholder[35:39] + 
        ' ' + placeholder[35:39] + ' ' + placeholder[35:39] +
        ' ' + placeholder[35:39] + ' ' + placeholder[35:39] + 
        ' ' + placeholder[35:39] + '\n' )
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder
    # RQ
    elif (linhas[0:2]) == "RQ":
        placeholder_RQ = LINHAS_DADGER[LINHAS_TOTAIS] 
        placeholder_RQ = (placeholder_RQ[:11] + placeholder_RQ[16:])
        LINHAS_DADGER[LINHAS_TOTAIS] = placeholder_RQ 
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

NOVO_ARQUIVO_DADGER = open('C:\\Users\\Joseeustaquio\\Downloads\\PMO_deck_preliminar\\REV AGOSTO\\DADGER.RV1', "w") # um novo arquivo do DADGER.RVx + 1 é criado
NOVO_ARQUIVO_DADGER.writelines(LINHAS_DADGER)
NOVO_ARQUIVO_DADGER.close()