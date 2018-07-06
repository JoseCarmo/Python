import csv
tabela = []
relacao_posto_vazao = []
with open('/home/jose/Downloads/ACOMPH.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        tabela.append(row)
print(tabela)

for item in tabela:
    