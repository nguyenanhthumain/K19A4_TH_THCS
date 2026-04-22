import random
n = int(input("Nhập n: "))
ds = [random.randint(1, 100) for _ in range(n)]
print("Danh sách:", ds)
ket_qua = list(map(lambda x: True if x % 2 == 0 else False, ds))
print("Kết quả:", ket_qua)