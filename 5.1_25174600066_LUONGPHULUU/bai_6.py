choi = ["Búa", "Kéo", "Lá"]
win = 0
lose = 0
draw = 0
round = 1
while round <= 5:
    print("Lượt", round)
    print("0: Búa | 1: Kéo | 2: Lá")
    player = int(input("Bạn chọn: "))
    computer = round % 3
    print("Bạn chọn:", choi[player])
    print("Máy chọn:", choi[computer])
    if player == computer:
        print("Hòa")
        draw += 1
    else:
        if (player == 0 and computer == 1) or \
           (player == 1 and computer == 2) or \
           (player == 2 and computer == 0):
            print("Bạn thắng")
            win += 1
        else:
            print("Bạn thua")
            lose += 1

    round += 1
    print("------------------")
print("Kết quả:")
print("Thắng:", win)
print("Hòa:", draw)
print("Thua:", lose)