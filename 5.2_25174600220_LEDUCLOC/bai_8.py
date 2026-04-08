"""Với n được nhập vào từ bàn phím. Hãy viết chương trình sử dụng list
comprehension để in dãy Fibonacci dưới dạng tách biệt bằng dấu phẩy. Ví dụ: Nếu
n được nhập là 7 thì chương trình sẽ in ra: 0, 1, 1, 2, 3, 5, 8, 13."""

n = int(input("Nhap n: "))
list = [0, 1]
for i in range(2, n):
    list.append(list[i-1] + list[i-2])
print(list)