from random import shuffle
nome1 = str(input('primeiro nome: '))
nome2 = str(input('O segundo nome: '))
nome3 = str(input('O terceiro nome: '))
nome4 = str(input('O quarto nome: '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A ordem da apresentação será: ')
print(lista)
