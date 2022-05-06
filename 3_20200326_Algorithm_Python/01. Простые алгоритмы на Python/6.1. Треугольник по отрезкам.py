# 6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

print('Введите длину трех стронон треугольника')
a = int(input('1-я сторона: '))
b = int(input('2-я сторона: '))
c = int(input('3-я сторона: '))

if a + b <= c or a + c <= b or b + c <= a:
    print(f'Треугольник со сторонами {a}, {b}, {c} не существует.')
elif a != b and a != c and b != c:
    print('Треугольник является разносторонним.')
elif a == b == c:
    print('Треугольник является равносторонним.')
else:
    print('Треугольник является равнобедренным.')