# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:

# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;


texto = input("Digite um nome: ")[::-1]
print(texto)
texto1 = "Gustavo"

def reversed_string(texto):
    count = int(len(texto))-1
    palavra_reversa = ''
    while count >= 0:
        palavra_reversa = palavra_reversa + texto[count]
        count= count - 1
    return palavra_reversa

print(reversed_string(texto1))