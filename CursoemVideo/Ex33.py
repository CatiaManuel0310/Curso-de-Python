a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
Menor = a
if b < a and b < c:
    Menor = b
if c < a and c < b:
    Menor = c
print('O menor valor é {}'.format(Menor))
Maior = c
if b > a and b > c:
    Maior = b
if c > a and c > b:
    Maior = c
print(' O maior valor é {}'.format(Menor))
print(' O maior valor é {}'.format(Maior))