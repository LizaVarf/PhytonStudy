list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2  #  3

first_team = list_players[:middle_index]  #  конец слайсирование до 3 элемента ["Маша", "Петя", "Саша"]
second_team = list_players[middle_index:]  #  начало слайсирования с 3 эл до конца ["Оля", "Кирилл", "Коля"]

print(first_team)
print(second_team)
