while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        break
    print("Sai, nhập lại!")
lst = list(range(m, n+1))
even = list(filter(lambda x: x % 2 == 0, lst))
print(even)