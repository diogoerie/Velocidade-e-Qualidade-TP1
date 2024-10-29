"""Modifique a função bubbleSort() para que ela ordene uma lista de strings em ordem alfabética.
Em seguida, teste a função com diferentes listas de strings e verifique se ela está ordenando corretamente."""


def bubble_sort_strings(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
