#bai_8
"""
Với n được nhập vào từ bàn phím. Hãy viết chương trình sử dụng list
comprehension để in dãy Fibonacci dưới dạng tách biệt bằng dấu phẩy. Ví dụ: Nếu
n được nhập là 7 thì chương trình sẽ in ra: 0, 1, 1, 2, 3, 5, 8, 13.
"""

n = int(input("Nhập số phần tử của dãy Fibonacci: "))
a = [0, 1]
[a.append(a[-1] + a[-2]) for _ in range(n - 2)]
print(", ".join(map(str, a)))