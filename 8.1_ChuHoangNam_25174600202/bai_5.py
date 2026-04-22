#cau5
def nhap_ky_tu_ascii():
    print("Chuong trinh in ma ASCII.")
    print("Go 'ESC' (hoac 'q') roi nhan Enter de thoat.")
    
    while True:
        s = input("Nhap mot ky tu: ")
        
        if s == "ESC" or s == "q":
            print("Da thoat chuong trinh.")
            break
        if len(s) > 0:
            char = s[0]
            print("Gia tri ASCII cua", char, "la:", ord(char))
nhap_ky_tu_ascii()