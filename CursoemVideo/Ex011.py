larg = float(input('Largura da parede: '))
alt = float(input('altura da parede: '))
area = larg * alt
input('Sua parede tem a dimenção de {}x{} e sua área é de {}m2,'.format(larg, alt,area))
tinta = area / 2
print('Para pintar essa parede, você precisa de {}L de tinta.'.format(tinta))