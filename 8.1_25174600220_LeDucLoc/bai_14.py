"""Bài 14:
Viết chương trình thực hiện các yêu cầu sau:
+ Tạo một list có n phần tử là số nguyên được nhập từ bàn phím.
+ Sử dụng map, lambda: Lạo một list chứa bình phương của các số hạng thuộc
list trên."""

n = int(input("Nhập số lượng phần tử n: "))
numbers = []
for i in range(n):
    num = int(input(f"Nhập số nguyên thứ {i + 1}: "))
    numbers.append(num)
squares = list(map(lambda x: x ** 2, numbers))
print(f"List chứa bình phương của các số hạng thuộc list trên: {squares}")

