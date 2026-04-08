X = int(input("Nhập giá trị X: "))
Y = int(input("Nhập giá trị Y: "))
mang_2_chieu = []
for i in range(X):
    hang = [] 
    for j in range(Y):
        hang.append(i * j) 
    mang_2_chieu.append(hang)
print(f"Đầu vào:{X},{Y}")
print(f"Đầu ra:",mang_2_chieu)
