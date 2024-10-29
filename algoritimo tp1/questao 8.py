"""O índice interno sempre vai da esquerda para a direita, encontrando o maior item e levando-o para a direita.
Modifique o método bubbleSort() para que ele seja bidirecional. Isso significa que o índice interno primeiro
levará o maior item da esquerda para a direita como antes, mas quando alcançar o último, ele se inverterá e
levará o menor item da direita para a esquerda. Você precisará de dois índices externos, um à
direita (o antigo último) e outro à esquerda. """

def bubble_sort(self):
    for last in range(self._nItens - 1, 0, -1):
        for inner in range(last):
            if self._a[inner] > self._a[inner + 1]:
                self.swap(inner, inner + 1)
