n = int(input("Nhập số phần tử: "))
gia_tri = tuple(int(input("Nhập giá trị: ")) for _ in range(n))
x = 0
for x in gia_tri:
   if x > 0 and x % 2 != 0:
        print("Tuple số lẻ:",x, end =" ")