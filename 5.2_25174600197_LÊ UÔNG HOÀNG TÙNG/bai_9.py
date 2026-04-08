# bai9
a = [int(input(f"nhap so thu {i+1}: ")) for i in range(int(input("nhap so luong: ")))]
assert all(x % 2 == 0 for x in a), "tat ca cac so phai la so chan"
print("tat ca cac so deu chan:", a)