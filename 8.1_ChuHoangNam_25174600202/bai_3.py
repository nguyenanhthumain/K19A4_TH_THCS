#cau3
#a
def check_prime():
    n = int(input("Nhap n: "))
    
    if n < 2:
        print(n, "khong phai so nguyen to")
        return
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break     
    if is_prime:
        print(n, "la so nguyen to")
    else:
        print(n, "khong phai so nguyen to")
check_prime()
 
#b
def check_perfect():
    n = int(input("Nhap n: "))
    
    sum_div = 0
    for i in range(1, n):
        if n % i == 0:
            sum_div = sum_div + i
            
    if sum_div == n:
        print(n, "la so hoan hao")
    else:
        print(n, "khong phai so hoan hao")
check_perfect()

#c
def print_symmetric():
    count_row = 0 
    
    for i in range(1, 1000):
        temp = i
        rev = 0
        while temp > 0:
            rev = rev * 10 + (temp % 10)
            temp = temp // 10
        if i == rev:
            print(f"{i:>5}", end="")
            count_row = count_row + 1
            if count_row == 15:
                print()
                count_row = 0
print_symmetric()