# Задание 8. Наименьшее K, при котором 1 + 2 + ... + K >= N,
# и значение этой суммы.

n = int(input("Введите целое число N (N > 1): "))

k = 0
current_sum = 0
while current_sum < n:
    k += 1
    current_sum += k

print("Наименьшее K:", k)
print("Сумма:", current_sum)
