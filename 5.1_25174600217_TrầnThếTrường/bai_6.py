import random

choices = ["kéo", "búa", "lá"]
win = draw = lose = 0
for _ in range(5):
    player = input("Chọn kéo/búa/lá: ").lower()
    comp = random.choice(choices)
    print("Máy chọn:", comp)
    if player == comp:
        draw += 1
    elif (player == "kéo" and comp == "lá") or \
         (player == "búa" and comp == "kéo") or \
         (player == "lá" and comp == "búa"):
        win += 1
    else:
        lose += 1

print("\nKết quả sau 5 lượt:")
print("Thắng:", win, "Hòa:", draw, "Thua:", lose)