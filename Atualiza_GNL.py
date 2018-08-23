""" ~ ~ ~ Atualizador do arquivo DADGNL'.RVX, parte do modelo de otimização de despacho hidrotérmico Decomp ~ ~ ~
Dentro do contexto do Planejamento Mensal de Operações (PMO), ocorrem revisões semanais (rv) que são acrescentadas à revisão inicial rv0
Essa rotina automatiza alterações na estrutura do código do DADGER.RVx, parte do modelo DECOMP 
A leitura do arquivo ocorre com o seguinte comando: 
    arquivo = open('caminho para aquivo alvo', 'modo de leitura') // a arquivo alvo é lido pelo Python e é armazenado dentro de uma lista onde 
    cada item da lista é uma linha da lista. 
No nosso exemplo, se o arquivo alvo possui n linhas:
    arquivo = [linha_1 do arquivo alvo, linha_2 do arquivo alvo, ..., linha_n do arquivo alvo]
A seguir, com o conhecimento do formato do DADGER.RVX, é possível 'parsear' todo o arquivo em busca dos valores a serem alterados e/ou 
comentados para a formação de uma próxima revisão.

 """
from Dadgnl import *

numero_revisao = 0 

caminho_dadger = "H:\\BC Mesa\\middle\\Dados de Rodadas\\Agosto\\rv0"

ARQUIVO_DAGDER = open(caminho_dadger + '\DADGNL.RV%s' %numero_revisao, "r+") # abre o arquivo DADGER.rvX
LINHAS_DADGER = ARQUIVO_DAGDER.readlines() # lê todas as linhas do DAGDER.RVO, incluindo fins de linhas
LINHAS_TOTAIS = 0 # inicializa o contador de linhas

for linhas in LINHAS_DADGER: # corre todas as linhas do script 
    # TG 
    if linhas[0:2] == "TG":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_TG(LINHAS_DADGER[LINHAS_TOTAIS], LINHAS_DADGER[LINHAS_TOTAIS + 1]))
    
    if linhas[0:2] == "GS":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_GS(LINHAS_DADGER[LINHAS_TOTAIS]))
    
    if linhas[0:2] == "GL":
        LINHAS_DADGER[LINHAS_TOTAIS] = str(Atualizar_GL(LINHAS_DADGER[LINHAS_TOTAIS], LINHAS_DADGER[LINHAS_TOTAIS + 1]))

    LINHAS_TOTAIS += 1  

ARQUIVO_DAGDER.close()
 
NOVO_ARQUIVO_DADGER = open(caminho_dadger + '/DADGNL1.RV%s' %(numero_revisao + 1), "w") # um novo arquivo do DADGER.RVx + 1 é criado
NOVO_ARQUIVO_DADGER.writelines(LINHAS_DADGER)
NOVO_ARQUIVO_DADGER.close()