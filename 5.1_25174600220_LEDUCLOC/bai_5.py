#Bài 5. Nhập từ bàn phím một số tự nhiên n. Tạo một list có n phần tử từ 1 đến n. Tìm và in ra màn hình một danh sách chứa các số nguyên tố và một danh sách chứa các số hoàn hảo thuộc dãy đã cho.

n = int(input("Nhập số tự nhiên n: "))

danh_sach_goc = list(range(1, n + 1))

so_nguyen_to = []
so_hoan_hao = []

for x in danh_sach_goc:
    if x > 1:
        la_nguyen_to = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                la_nguyen_to = False
                break
        if la_nguyen_to:
            so_nguyen_to.append(x)
    
    tong_uoc = 0
    for i in range(1, x):
        if x % i == 0:
            tong_uoc += i
    if tong_uoc == x and x != 0:
        so_hoan_hao.append(x)

print("Danh sách số nguyên tố:", so_nguyen_to)
print("Danh sách số hoàn hảo:", so_hoan_hao)