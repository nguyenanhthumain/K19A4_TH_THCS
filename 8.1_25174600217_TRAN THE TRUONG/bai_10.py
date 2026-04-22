def in_uoc_so(n):
    print("Các ước số của", n, "là:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print() 

def main():
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        print("n phải là số nguyên dương")
        return

    in_uoc_so(n)
main()