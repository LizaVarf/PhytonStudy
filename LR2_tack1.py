money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0 # Количество месяцев без долг
while True:
    budget = money_capital + salary # Бюджет
    if salary > budget:
        break
    month += 1
    spend *= (1 + increase) # Ежемесячный рост цен на 5% кроме 1-го месяца
    money_capital += salary - spend
print("Количество месяцев, которое можно протянуть без долгов:", month )
