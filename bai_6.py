import random
choices = ["kéo", "búa", "lá"]
win = draw = lose = 0
for i in range(5):
    user = input("Nhập (kéo/búa/lá): ")
    comp = random.choice(choices)
    print("Máy:", comp)
    if user == comp:
        draw += 1
    elif (user == "kéo" and comp == "lá") or \
         (user == "búa" and comp == "kéo") or \
         (user == "lá" and comp == "búa"):
        win += 1
    else:
        lose += 1
print("Thắng:", win, "Hòa:", draw, "Thua:", lose)