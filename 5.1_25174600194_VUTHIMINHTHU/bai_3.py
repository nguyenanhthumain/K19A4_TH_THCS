while True:
    m = int(input("Nhập giá trị m: "))
    n = int(input("Nhập giá trị n: "))
    if 0 < m < n:
        break
    print(f"Yêu cầu nhập lại.")
lst = list(range(m, n+1))
lstn = list(filter(lambda x: x % 2 == 0, lst))
print("Các số chẵn đã lọc trong danh sách:", lstn)