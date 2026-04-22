"""Bài 15:
a) Viết chương trình tạo một list chứa toàn số chẵn thuộc khoảng đóng [1,100].
b) Viết chương trình nhập vào một danh sách các số nguyên từ 1 đến n (n có thể
nhập từ bàn phím), sử dụng filter và reduce để viết hàm tính tổng các số chẵn
trong danh sách đã nhập."""

#a
print(list(range(2, 101, 2)))

#b
n = int(input("Nhập số nguyên n: "))
numbers = list(range(1, n + 1))
print(list(filter(lambda x: x % 2 == 0, numbers)))
print(sum(list(filter(lambda x: x % 2 == 0, numbers))))
