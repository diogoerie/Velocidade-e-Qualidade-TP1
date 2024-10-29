"""Escreva uma função em Python que implemente o algoritmo Bubble Sort para ordenar
uma lista de números em ordem crescente. Em seguida, teste a função com diferentes
listas de números e verifique se ela está ordenando corretamente."""

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
