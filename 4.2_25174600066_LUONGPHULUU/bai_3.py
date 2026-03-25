# Cách 1 while:
while True:
    s = input("Nhập số: ")
    if "." in s:
        print("Gặp số thập phân -> dừng!")
        break

    n = int(s)
    if n < 0:
        print("Gặp số âm -> dừng!")
        break

    print("Bạn vừa nhập:", n)
# Cách 2 for:
for _ in range(1000):
    s = input("Nhập số: ")
    if "." in s:
        print("Gặp số thập phân -> dừng!")
        break
    n = int(s)
    if n < 0:
        print("Gặp số âm -> dừng!")
        break

    print("Bạn vừa nhập:", n)
