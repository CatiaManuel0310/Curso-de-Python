salario = float(input('Digite o salário do funcionário:R$ '))
novo = salario + (salario * 15 /100)
print('O salário do funcionário era R${}, agora com o aumento de 15% o salário passa a ser R${}'.format(salario, novo))