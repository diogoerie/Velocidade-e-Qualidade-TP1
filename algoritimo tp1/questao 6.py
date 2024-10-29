"""Imagine que você tem um tabuleiro de xadrez e coloca um único grão de arroz em um quadrado.
No segundo quadrado, você coloca 2 grãos de arroz, já que isso é o dobro da quantidade de arroz
no quadrado anterior. No terceiro quadrado, você coloca 4 grãos. No quarto quadrado, você coloca 8 grãos,
e no quinto quadrado, você coloca 16 grãos, e assim por diante."""

tabuleiro = 8 * 8
arroz = 1
quadrado = int(input("Digite o número do quadrado do tabuleiro (1 a 64): "))

if quadrado <= tabuleiro:
    arroz = 1
    for i in range(quadrado - 1):
        arroz *= 2
print(f"Nesse quadrado teremos {arroz} grãos de arroz.")

