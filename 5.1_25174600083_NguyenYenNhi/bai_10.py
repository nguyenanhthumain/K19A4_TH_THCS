#bai_10
"""
Viết chương trình tạo một tuple chứa toàn các số nguyên dương lẻ được lọc ra
từ tuple cho trước với số lượng n phần tử được nhập từ bàn phím.
"""

n = int(input("Nhập số lượng phần tử n: "))
ds = []
a = 1
while len(ds) < n:
    if a % 2 != 0:
        ds.append(a)
    a += 1
print("Tuple số lẻ:", tuple(ds))