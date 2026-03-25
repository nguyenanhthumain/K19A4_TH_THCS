n = int(input("Nhập n: "))

if n < 2:
    print("Không phải SNT")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Không phải SNT")
            break
    else:
        print("Là SNT")