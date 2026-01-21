# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, sep =','):
    first_group = set(first_group.split(sep))
    second_group = second_group.split(sep)
    common_participants = list(first_group.intersection(second_group))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
participants = find_common_participants(participants_first_group, participants_second_group,'|')
print(participants)