# Задание 4. Сумма 1 + A + A^2 + ... + A^N с использованием одного цикла.

a = float(input("Введите вещественное число A: "))
n = int(input("Введите целое положительное число N: "))

term = 1.0
result = 1.0
for _ in range(n):
    term *= a
    result += term

print("Значение суммы:", f"{result:.10g}")
