"""Bài 6: Viết chương trình kiểm tra một số n nhập từ bàn phím có là số nguyên tố
không."""

n = int(input("Nhập một số nguyên: "))
if n > 1:
    m = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            m = False
            break
    if m:
        print(n, "là số nguyên tố.")
    else:
        print(n, "không phải là số nguyên tố.")