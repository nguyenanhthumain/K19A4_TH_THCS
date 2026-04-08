#Bài 10: Viết chương trình tạo một tuple chứa toàn các số nguyên dương lẻ được lọc ra từ tuple cho trước với số lượng n phần tử được nhập từ bàn phím.
n = int(input("Nhập số lượng phần tử n: "))

danh_sach_tam = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach_tam.append(so)

tuple_goc = tuple(danh_sach_tam)

ket_qua_le = []
for x in tuple_goc:
    if x > 0 and x % 2 != 0:
        ket_qua_le.append(x)

tuple_so_le = tuple(ket_qua_le)

print("Tuple ban đầu:", tuple_goc)
print("Tuple các số lẻ:", tuple_so_le)
