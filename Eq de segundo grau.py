# Raízes de uma equação de segundo grau

a = float(input('Digite o valor do coeficiente angular:\n'))
b = float(input('Digite o valor do coeficiente linear:\n'))
c = float(input('Digite o valor do termo independente:\n'))


d = b ** 2-4*a*c
if d<0:
    print('Solução complexa.')
    print('x1 =', (d**0.5-b)/2*a)
    print('x2 =', (d**0.5+b)/2*a)
else:
    print('Solução real.')
    print('x1 =', (d**0.5-b)/2*a)
    print('x2 =', (d**0.5+b)/2*a)
