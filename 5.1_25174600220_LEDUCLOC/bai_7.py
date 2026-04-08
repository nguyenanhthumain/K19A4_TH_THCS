#Bài 7. Viết chương trình chuẩn hóa một chuỗi ký tự được nhập từ bàn phím. Chuỗi chuẩn hóa là chuỗi không có các khoảng trắng (dấu cách) ở đầu và cuối, các từ trong chuỗi chỉ cách nhau đúng một dấu cách.
chuoi_nhap = input("Nhập chuỗi cần chuẩn hóa: ")
cac_tu = chuoi_nhap.split()
chuoi_chuan_hoa = " ".join(cac_tu)

print("Chuỗi sau khi chuẩn hóa:")
print(f"'{chuoi_chuan_hoa}'")