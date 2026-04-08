import random

choices = ["búa", "kéo", "lá"]

win = 0
draw = 0
lose = 0

for i in range(5):
    user = input("Nhập (búa/kéo/lá): ")
    comp = random.choice(choices)

    print("Máy:", comp)

    if user == comp:
        draw += 1
    elif (user == "búa" and comp == "kéo") or \
         (user == "kéo" and comp == "lá") or \
         (user == "lá" and comp == "búa"):
        win += 1
    else:
        lose += 1

print("Thắng:", win)
print("Hòa:", draw)
print("Thua:", lose)