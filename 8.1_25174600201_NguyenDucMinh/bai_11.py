def tinh_tb(t, l, h):
    return (t + l + h) / 3

ten = input("Tên: ")
t = float(input("Toán: "))
l = float(input("Lý: "))
h = float(input("Hóa: "))

print("Trung bình:", tinh_tb(t, l, h))