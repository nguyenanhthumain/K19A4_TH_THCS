#bai_7
"""
Viết chương trình chuẩn hóa một chuỗi ký tự được nhập từ bàn phím. Chuỗi chuẩn
hóa là chuỗi không có các khoảng trắng (dấu cách) ở đầu và cuối, các từ trong
chuỗi chỉ cách nhau đúng một dấu cách.
"""

chuoi_chuan_hoa = input("Nhập chuỗi cần chuẩn hóa: ")
chuoi_chuan_hoa = chuoi_chuan_hoa.strip()  # Loại bỏ khoảng trắng ở đầu và cuối
chuoi_chuan_hoa = ' '.join(chuoi_chuan_hoa.split())  # Loại bỏ khoảng trắng thừa giữa các từ
print("Chuỗi sau khi chuẩn hóa:", chuoi_chuan_hoa)