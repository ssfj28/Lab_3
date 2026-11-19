# Задание 1. Стоимость конфет массой от 0.1 до 1 кг.

price_per_kg = float(input("Введите цену 1 кг конфет: "))

for tenths in range(1, 11):
    weight = tenths / 10
    cost = price_per_kg * weight
    print(f"Стоимость {weight:.1f} кг конфет: {cost:.2f} руб.")
