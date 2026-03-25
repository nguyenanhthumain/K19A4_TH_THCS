# Bài 10:
"""
Viết chương trình in tất cả các số nguyên tố từ 1 đến n được nhập từ bàn phím.
"""

n = int(input("Nhập n : "))
if n < 2 :
    print("Không có số nguyên tố nào nhỏ hơn 2.")
else :
    for i in range(2, n + 1) :
        if i > 1 :
            for j in range(2, i) :
                if i % j == 0 :
                    break
            else :
                print(i, end = " ")