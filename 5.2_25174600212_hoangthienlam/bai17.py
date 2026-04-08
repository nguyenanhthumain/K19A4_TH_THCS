
try:
    m = int(input("Nhập số hàng m: "))
    n = int(input("Nhập số cột n: "))
    A = []
    print(f"Nhập các phần tử cho ma trận {m}x{n}:") 
    for i in range(m):
        hang = []
        for j in range(n):
            val = int(input(f"Nhập phần tử a[{i+1}][{j+1}]: "))
            hang.append(val)
        A.append(hang)
    print("\nMa trận A vừa nhập là:")
    for hang in A:
        print(hang)
    tong_ma_tran = 0
    for hang in A:
        for phan_tu in hang:
            tong_ma_tran += phan_tu        
    print(f"\n=> Tổng tất cả các phần tử của ma trận A là: {tong_ma_tran}")
except ValueError:
    print("Vui lòng chỉ nhập số tự nhiên hợp lệ!")