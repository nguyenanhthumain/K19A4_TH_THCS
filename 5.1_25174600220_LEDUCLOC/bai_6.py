#Bài 6. Viết chương trình trò chơi ra búa, kéo, lá chơi với máy tính. Người chơi có 5 lượt chơi với máy tính, sau 5 lượt chơi thì thống kê người chơi đã thắng, hòa, thua bao nhiêu lượt với máy tính. (Làm các bài tập sau sử dụng kiến thức đã được học (LIST và TUPLE), không sử dụng các thư viện để thực hiện các thuật toán.)

import random

thang = 0
hoa = 0
thua = 0
lua_chon = ["kéo", "búa", "lá"]

print("Chào mừng bạn đến với trò chơi Kéo - Búa - Lá!")

for i in range(5):
    print(f"\nLượt chơi thứ {i+1}:")
    nguoi_choi = input("Nhập lựa chọn của bạn (kéo, búa, lá): ").lower()
    may_tinh = random.choice(lua_chon)
    
    print(f"Máy tính chọn: {may_tinh}")
    
    if nguoi_choi == may_tinh:
        print("Kết quả: Hòa")
        hoa += 1
    elif (nguoi_choi == "kéo" and may_tinh == "lá") or \
         (nguoi_choi == "búa" and may_tinh == "kéo") or \
         (nguoi_choi == "lá" and may_tinh == "búa"):
        print("Kết quả: Bạn thắng!")
        thang += 1
    else:
        print("Kết quả: Bạn thua!")
        thua += 1

print("-" * 20)
print(f"Kết thúc 5 lượt. Thống kê: Thắng: {thang}, Hòa: {hoa}, Thua: {thua}")
