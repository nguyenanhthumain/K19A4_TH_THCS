while True:
    m = int(input("Nhập giá trị m: "))
    n = int(input("Nhập giá trị n: "))
    if 0 < m < n:
        break
    print("Yêu cầu nhập lại.")
lst = list(range(m, n+1, 2))[:100]
print("Danh sách:", lst)
print("Tổng:", sum(lst))