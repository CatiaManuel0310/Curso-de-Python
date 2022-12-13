
velocidade = float(input('Qual é a velocidade do carrro? '))
if velocidade > 80:
    print('MULTADO! Voce ultrapassou a velocidade adequado')
    multa = (velocidade - 80) * 7
    print(' Voce deve pagar a multa de {:.2f}'.format(multa))
else:
    print('Tenha um bom dia!!!')