
 #n1 = int(input('Digite um número: '))
 #n2 = int(input('Digite outro número: '))
# c = n1 + n2
 #print('O resultado entre {} e {} é: {} '.format(n1,n2,c))

s = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(s))
print('É um número? ', s.isnumeric())
print('É alfabético? ', s.isalpha())
print('É um alfanúmero? ', s.isalnum())
print('Está em maiúscula? ', s.isupper())
print('Está capitalizada? ', s.istitle())