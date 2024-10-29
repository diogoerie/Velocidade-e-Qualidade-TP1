"""A seguinte função encontra o maior número único dentro de um array, mas tem uma eficiência de O(N²). Reescreva a função para que se torne uma eficiência O(N):"""

array = [3, 1, 4, 5, 2, 5, 7, 6, 8]

def greatest_number(array):
    passo = 0
    ocorre = {}
    maior = float('-inf')
    for num in array:
        passo += 1
        ocorre[num] = ocorre.get(num, 0) + 1
        if num > maior:
            maior = num
    if ocorre[maior] == 1:
        return maior, passo
    for num in array:
        if ocorre[num] == 1 and num > float('-inf'):
            return num, passo
    return passo

maior, passos = greatest_number(array)
print(f"O maior número único é: {maior}")
print(f"Total de passos: {passos}")



