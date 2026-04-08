m=int(input("Nhập số hàng m: "))
n=int(input("Nhập số cột n: "))

ma_tran=[]

for i in range(m):
    hang=[]
    for j in range(n):
        gia_tri=int(input(f"Nhập phần tử hàng {i+1}, cột {j+1}: "))
        hang=hang+[gia_tri]
    ma_tran=ma_tran+[hang]

tong=0
for hang in ma_tran:
    for gia_tri in hang:
        tong+=gia_tri

print("Tổng các phần tử của ma trận là:", tong)