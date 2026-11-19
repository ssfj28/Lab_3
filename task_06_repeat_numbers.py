# Задание 6. Каждое целое число от A до B выводится столько раз,
# каково его значение.

a = int(input("Введите целое положительное число A: "))
b = int(input("Введите целое число B (B > A): "))

for number in range(a, b + 1):
    for _ in range(number):
        print(number, end=" ")
    print()
