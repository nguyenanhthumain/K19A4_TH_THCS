#cau5
seed = int(input("Nhập một số may mắn để bắt đầu sinh dãy: "))

list_A = []
so_hien_tai = seed

while len(list_A) < 1000:
    so_hien_tai = (so_hien_tai * 1103515245 + 12345) % 99999
    
    if 1 <= so_hien_tai <= 99999:
        if so_hien_tai % 7 != 0:
            list_A.append(so_hien_tai)
print(f"da tao xong danh sach A co {len(list_A)} phan tu.")
print("10 so dau tien trong danh sach la:", list_A[:10])