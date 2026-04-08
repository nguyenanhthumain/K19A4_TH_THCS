gia_tri = input("Nhập X, Y (cách nhau bởi dấu phẩy): ")
X, Y = [int(x) for x in gia_tri.split(',')]
mang_2_chieu = [[i * j for j in range(Y)] for i in range(X)]
print(f"Mảng {X}x{Y}:")
for hang in mang_2_chieu:
    print(hang)