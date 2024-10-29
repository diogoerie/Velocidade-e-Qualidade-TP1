'''Escreva um código usando list comprehension em Python que retorne os caracteres individuais
de uma string que não são caracteres de espaço em branco. Aplique-a à string "Sítio do pica-pau amarelo \n 2023”.'''

frase = "Sítio do pica-pau amarelo \n 2023"

for i in frase:
    if i != " ":
        print(i)