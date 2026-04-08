#bai_6
"""
Viết chương trình trò chơi ra búa, kéo, lá chơi với máy tính. Người chơi có 5 lượt
chơi với máy tính, sau 5 lượt chơi thì thống kê người chơi đã thắng, hòa, thua bao
nhiêu lượt với máy tính.
"""

print("Trò chơi ra búa, kéo, lá")
thang = 0
hoa = 0
thua = 0
for i in range(5):
    print("Lượt chơi thứ", i + 1)
    nguoi_choi = input("Nhập lựa chọn của bạn (búa, kéo, lá): ")
    chon = ["búa", "kéo", "lá"]
    may_tinh = chon[i % 3] 
    print("Máy tính chọn:", may_tinh)
    if nguoi_choi == may_tinh:
        hoa += 1
        print("Kết quả: Hòa!")
    elif (nguoi_choi == "búa" and may_tinh == "kéo") or (nguoi_choi == "kéo" and may_tinh == "lá") or (nguoi_choi == "lá" and may_tinh == "búa"):
        thang += 1
        print("Kết quả: Bạn thắng!")
    else:
        thua += 1
        print("Kết quả: Bạn thua!")
print("Thống kê sau 5 lượt chơi:")
print("Bạn thắng:", thang)
print("Bạn hòa:", hoa)
print("Bạn thua:", thua)