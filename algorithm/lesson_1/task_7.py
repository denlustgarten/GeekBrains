"""По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой треугольник
существует, то определить, является ли он разносторонним, равнобедренным или равносторонним."""

a = int(input("Введите первую сторону треугольника: "))
b = int(input("Введите вторую сторону треугольника: "))
c = int(input("Введите третью сторону треугольника: "))

if (a + b) <= c or (a + c) <= b or (b + c) < a:
    print('Такой треугольник не существует')
else:
    if a == b == c:
        print('Треугольник равносторонний')
    else:
        if a == b or a == c or b == c:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')
