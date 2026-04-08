n = int(input("Nhập n: "))
lst = []
for i in range(1, n + 1):
    lst.append(i * i)
m = int(input("Nhập m: "))
if m >= n:
    print("Danh sách kết quả:", lst)
else:
    print("Danh sách kết quả:", lst[:m])