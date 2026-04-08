def is_even(x):
    return x % 2 == 0
while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        break
    else:
        print("Lỗi 0 < m < n.Vui lòng nhập lại\n")

numbers = list(range(m, n + 1))
even_numbers = list(filter(is_even, numbers))
print("Danh sách ban đầu:", numbers)
print("Các số chẵn:", even_numbers)