# TODO решите задачу
import json

input_filename= "input.json"

def task() -> float:
    with open(input_filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    total = 0.0
    for item in data:
          total += item["score"] * item["weight"]
    result = round (total, 3)
    return result
# Нужно для проверки
print (task())
