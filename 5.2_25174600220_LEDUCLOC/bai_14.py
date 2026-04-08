"""Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, name
là string, age và height là number. Tuple được nhập vào bởi người dùng. Tiêu chí
sắp xếp là:
a. Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score.
b. Ưu tiên là tên > tuổi > điểm."""


n = int(input("Nhập số lượng tuple: "))
tuple_list = []
for i in range(n):
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    score = float(input("Nhập điểm: "))
    tuple_list.append((name, age, score))

tuple_list.sort(key=lambda x: (x[0], x[1], x[2]))

print("Danh sách sau khi sắp xếp:")
for name, age, score in tuple_list:
    print(f"ên: {name}, Tuổi: {age}, Điểm: {score}")