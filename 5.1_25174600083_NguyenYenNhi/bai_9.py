#bai_9
"""
Cho trước mọt tuple chứa các số tự nhiên từ m đến n với 0 < m < n được nhập
từ bàn phím. Viết chương trình sao cho nửa đầu và nửa cuối của tuple trên được
lưu vào các tuple có tên là “tp1” và “tp2” tương ứng. In kết quả ra màn hình.
"""

m = int(input("Nhập số m (0 < m): "))
n = int(input("Nhập số n (m < n): "))   
tup = tuple(range(m, n + 1))
giua = len(tup) // 2
tp1, tp2 = tup[:giua], tup[giua:]
print("Nửa đầu của tuple là :", tp1)
print("Nửa sau của tuple là :", tp2)