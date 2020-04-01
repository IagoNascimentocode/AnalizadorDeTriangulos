print(23 * '\033[1;34m=\033[m')
print('\033[1;30mAnalizador de triangulo\033[m')
print(23 * '\033[1;34m=\033[m')
a = float(input('Digite o lado A do triangulo:'))
b = float(input('Digite o lado B do triangulo:'))
c = float(input('Digite o labo C do triandulo:'))
if a < b+c and b < a+c and c < a+b:
    print('esses valores podem formar um triangulo',end=' ')
    if a == b == c:
        print('Equilatero.')
    if a != b != c != a:
        print('Escaleno.')
    else:
        print('Isosceles')
else:
    print('esses valores não podem formar um triangulo')
