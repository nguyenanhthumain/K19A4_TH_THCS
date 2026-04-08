m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
ma_tran_A = []
for i in range(m):
    print(f"Nhập các phần tử cho hàng {i+1}:")
    hang = [int(input(f"  A[{i}][{j}]: ")) for j in range(n)]
    ma_tran_A.append(hang)
tong_ma_tran = 0
for hang in ma_tran_A:
    tong_ma_tran += sum(hang)
print("Ma trận A bạn vừa nhập:")
for hang in ma_tran_A:
    print(hang)
print(f"==> Tổng tất cả các phần tử của ma trận là: {tong_ma_tran}")