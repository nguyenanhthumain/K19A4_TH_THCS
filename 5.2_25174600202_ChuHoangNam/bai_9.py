#cau9
input_str = input("Nhap cac so, cach nhau boi dau phay: ")

danh_sach = input_str.split(",")

tat_ca_la_chan = True

for s in danh_sach:
    so = int(s.strip()) 
    if so % 2 != 0:     
        tat_ca_la_chan = False
        break           
if tat_ca_la_chan:
    print("Tat ca cac so trong list deu la so chan.")
else:
    print("Trong list co chua so le.")