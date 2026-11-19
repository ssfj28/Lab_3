# Задание 7. Остаток от размещения максимально возможного числа отрезков B
# на отрезке A. Умножение и деление не используются.
# Decimal позволяет выполнять вычисления с десятичными дробями точнее, чем float.

from decimal import Decimal

a = Decimal(input("Введите длину отрезка A: ").replace(",", "."))
b = Decimal(input("Введите длину отрезка B (A > B): ").replace(",", "."))

remaining_length = a
while remaining_length >= b:
    remaining_length -= b

print("Длина незанятой части:", format(remaining_length, "f"))
