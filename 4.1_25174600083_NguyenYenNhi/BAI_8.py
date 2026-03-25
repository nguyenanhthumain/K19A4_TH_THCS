# Bài 8:
"""
Viết chương trình yêu cầu xuất ra các số từ 1 đến 1000, liệt kê những số là
số nguyên tố.
"""
for i in range(1, 1001) :
    if i > 1 :
        for j in range(2, i) :
            if i % j == 0 :
                break
        else :
            print(i, end = " ")