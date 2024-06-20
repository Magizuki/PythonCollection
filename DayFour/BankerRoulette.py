import random

names = ["Budi", "Tono", "Lala"]
num_string = len(names)
pick_name = random.randint(0, num_string - 1)
print(names[pick_name])