#Bài 9:
"""9. Cho trước mọt tuple chứa các số tự nhiên từ m đến n với 0 < m < n được nhập
từ bàn phím. Viết chương trình sao cho nửa đầu và nửa cuối của tuple trên được
lưu vào các tuple có tên là “tp1” và “tp2” tương ứng. In kết quả ra màn hình."""

while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        break
    else:
        print("Điều kiện không hợp lệ. Vui lòng nhập lại.")
tup = tuple(range(m, n + 1))
tp1 = tup[0:len(tup) // 2]
tp2 = tup[len(tup) // 2:]
print("nửa đầu là: " ,tp1)
print("nửa cuối là: " ,tp2)