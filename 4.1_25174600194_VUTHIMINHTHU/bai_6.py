n = int(input("Nhập giá trị:"))
if n<2:
    print(f"Đây không phải số nguyên tố")
else:
    is_prime = False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            is_prime= True
            break
    if is_prime:
        print(f"Đây không phải số nguyên tố")
    else:
        print(f"Đây là số nguyên tố")