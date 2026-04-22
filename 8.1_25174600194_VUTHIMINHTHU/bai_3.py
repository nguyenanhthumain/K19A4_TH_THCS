def kt_nguyento(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def ktr_sohoanhao(n):
    if n <= 1:
        return False
    tong_cac_uoc = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            tong_cac_uoc += i
            if i != n // i:
                tong_cac_uoc += n // i
    return tong_cac_uoc == n
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def nhap_so_nguyen_duong():
    while True:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            return n
        print(f"{n} không phải số nguyên dương")
n = nhap_so_nguyen_duong()
if kt_nguyento(n):
    print(f"a. {n} là số nguyên tố")
else:
    print(f"a. {n} không là số nguyên tố")
if ktr_sohoanhao(n):
    print(f"b. {n} là số hoàn hảo")
else:
    print(f"b. {n} không là số hoàn hảo")
print(f"c. Các số đối xứng trong phạm vi 1000 là:")
count = 0
for i in range(1, 1000):
    if is_palindrome(i):
        print(str(i).rjust(3), end=" ")
        count += 1
        if count % 15 == 0:
            print("")
