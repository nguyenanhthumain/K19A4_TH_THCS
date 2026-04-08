while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        break
    else:
        print("Lỗi 0 < m < n.Vui lòng nhập lại\n")
numbers = []
current = m

while current <= n and len(numbers) < 100:
    numbers.append(current)
    current += 2
print("Danh sách 100 số tự nhiên đầu tiên với bước nhảy 2:", numbers)
print("Tổng các số trong danh sách:", sum(numbers))