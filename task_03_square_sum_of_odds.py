# Задание 3. Вычисление N^2 как суммы первых N нечетных чисел.
# После каждого слагаемого выводится текущая сумма.

n = int(input("Введите целое положительное число N: "))

current_sum = 0
for i in range(1, n + 1):
    odd_number = 2 * i - 1
    current_sum += odd_number
    print(f"После добавления {odd_number}: сумма = {current_sum}")

print(f"Квадрат числа {n} равен {current_sum}")
