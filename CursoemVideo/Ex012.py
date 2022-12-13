preço = float(input('Qual é o preço do produto: R$'))
novo = preço - (preço * 5 / 100)
print(' O preço que custava R${}, na promoção com 5% vai curstar R${}'.format(preço, novo))