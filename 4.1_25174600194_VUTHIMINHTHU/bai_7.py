a= float(input("Nhập gái trị a:"))
b =float(input("Nhập giá trị b:"))
phep_cong = a+b
phep_tru = a-b
phep_nhan = a*b
phep_chia =a/b
print("\n ===MENU PHÉP TOÁN===")
print("1.Cộng")
print("2.Trừ")
print("3.Nhân")
print("4.Chia")
print("0.Thoát")
lua_chon = input("Chọn chức năng:")
if lua_chon =="1":
    print(f"Kết quả:",phep_cong)
elif lua_chon == "2":
    print(f"Kết quả:",phep_tru)
elif lua_chon == "3":
    print(f"Kết quả:",phep_nhan)
elif lua_chon == "4":
    print(f"Kết quả:",phep_chia)
elif lua_chon=="0":
    print(f"Đã thoát khỏi chương trình")
else:
    print(f"Yêu cầu nhập lại")
