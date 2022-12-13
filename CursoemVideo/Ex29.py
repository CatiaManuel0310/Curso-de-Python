
velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! Você ultrapassou a velocidade adequado')
    multa = (velocidade - 80) * 7
    print(' Você deve pagar a multa de {:.2f}'.format(multa))
else:
    print('Tenha um bom dia!!!')