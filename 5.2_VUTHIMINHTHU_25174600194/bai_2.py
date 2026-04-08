n = int(input("Nhập giá trị n:"))
m = int(input("Nhập giá trị m:"))
lst = [i**2 for i in range (1,n+1)]
if m<n:
    print(f"Mục đầu tiên trong danh sách:",lst[m:])
else:
    print(f"Danh sách rỗng")