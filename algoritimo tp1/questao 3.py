'''Quantos passos seriam necessários para realizar uma busca linear pelo número 8 no array ordenado, [2, 4, 6, 8, 10, 12, 13]?'''

array = [2, 4, 6, 8, 10, 12, 13]
passo = 0

for i in array:
    passo += 1
    if i == 8:
        break
print(passo)