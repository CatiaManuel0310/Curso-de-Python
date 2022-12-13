import random
nome1 = str(input('O primeiro nome: '))
nome2 = str(input('O segundo nome: '))
nome3 = str(input('O terceiro nome: '))
nome4 = str(input('O quarto nome: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O nome do aluno escolhido é: {}'.format(escolhido))