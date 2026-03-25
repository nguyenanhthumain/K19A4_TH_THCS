n= int(input("Nhập số nguyênt tố n: "))
if n < 2:
    print(n, "không phải là số nguyên tố")
else:
    la_snt = True
    for i in range(2, n):
        if n % i == 0:
            la_snt = False
            break
    if la_snt:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")