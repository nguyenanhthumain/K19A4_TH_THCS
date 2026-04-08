# Nhập mật khẩu
p = input("Nhập mật khẩu để kiểm tra: ")

# Thiết lập các biến đánh dấu (flag)
is_valid = True
has_lower = False
has_number = False
has_upper = False
has_special = False
special_chars = "$#@"

# Kiểm tra độ dài (Câu e, f)
if 6 <= len(p) <= 12:
    for char in p:
        if 'a' <= char <= 'z': # Câu a
            has_lower = True
        elif '0' <= char <= '9': # Câu b
            has_number = True
        elif 'A' <= char <= 'Z': # Câu c
            has_upper = True
        elif char in special_chars: # Câu d
            has_special = True
    
    # Kiểm tra xem có thiếu tiêu chí nào không
    if not (has_lower and has_number and has_upper and has_special):
        is_valid = False
else:
    is_valid = False

if is_valid:
    print("Mật khẩu hợp lệ.")
else:
    print("Mật khẩu không hợp lệ.")