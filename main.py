# Задание №1

a = int(input('Введите первое число: '))
b = input('Введите действие: ')
c = int(input('Введите второе число: '))

if b == '+':
    print(f'Ответ: {a + c}')
if b == '-':
    print(f'Ответ: {a - c}')
if b == '*':
    print(f'Ответ: {a * c}')
if b == '/':
    print(f'Ответ: {a / c}')
print('\n')



# Задание №2

n = int(input('Введите число: '))
i = 1
while i ** 2 <= n:
    print(i ** 2, end=' ')
    i += 1
print('\n')



# Задание №3

f = int(input("Введите число: "))
k = 0
for i in range(2, f // 2 + 1):
    if (f % i == 0):
        k = k + 1
if (k <= 0):
    print("Это простое число")
else:
    print("Это не простое число")
