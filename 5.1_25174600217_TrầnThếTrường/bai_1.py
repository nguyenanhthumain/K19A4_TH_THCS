n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
list_square = [i**2 for i in range(1, n + 1)]
print("Danh sách bình phương:", list_square)
print("\nKết quả cần in:")
if m >= n:
    print(list_square)
else:
    print(list_square[:m])