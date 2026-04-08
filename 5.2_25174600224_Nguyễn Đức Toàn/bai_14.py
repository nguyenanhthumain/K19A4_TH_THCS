n=int(input("Nhập số lượng tuple: "))
danh_sach=[]

for i in range(n):
    name=input(f"Nhập tên {i+1}: ")
    age=int(input(f"Nhập tuổi {i+1}: "))
    score=int(input(f"Nhập điểm {i+1}: "))
    danh_sach=danh_sach+[(name, age, score)]

for i in range(len(danh_sach)-1):
    for j in range(len(danh_sach)-1-i):
        if danh_sach[j][0]>danh_sach[j+1][0] or \
           (danh_sach[j][0]==danh_sach[j+1][0] and danh_sach[j][1]>danh_sach[j+1][1]) or \
           (danh_sach[j][0]==danh_sach[j+1][0] and danh_sach[j][1]==danh_sach[j+1][1] and danh_sach[j][2]>danh_sach[j+1][2]):
            danh_sach[j], danh_sach[j+1] = danh_sach[j+1], danh_sach[j]

for t in danh_sach:
    print(t)