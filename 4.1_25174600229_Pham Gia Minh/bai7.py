while True:
    print("--- MENU ---")
    print("1. Cong, 2. Tru, 3. Nhan, 4. Chia, 0. Thoat")
    chon = int(input("Moi ban chon: "))
    
    if chon == 0:
        break
        
    a = float(input("Nhap so thu nhat: "))
    b = float(input("Nhap so thu hai: "))
    
    if chon == 1:
        print(f"Tong = {a + b}")
    elif chon == 2:
        print(f"Hieu = {a - b}")
    elif chon == 3:
        print(f"Tich = {a * b}")
    elif chon == 4:
        if b != 0:
            print(f"Thuong = {a / b}")
        else:
            print("Loi: Khong the chia cho 0")