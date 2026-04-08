# Nhập chuỗi mật khẩu phân tách bởi dấu phẩy
raw_input = input("Nhập danh sách mật khẩu (cách nhau bởi dấu phẩy): ")
passwords = raw_input.split(",")

valid_passwords = []

for p in passwords:
    p = p.strip() # Xóa khoảng trắng thừa ở hai đầu
    
    # Kiểm tra các tiêu chí
    if 6 <= len(p) <= 12:
        has_lower = any('a' <= c <= 'z' for c in p)
        has_number = any('0' <= c <= '9' for c in p)
        has_upper = any('A' <= c <= 'Z' for c in p)
        has_special = any(c in "$#@" for c in p)
            
        if has_lower and has_number and has_upper and has_special:
            valid_passwords.append(p)

# In kết quả theo định dạng phân cách bởi dấu phẩy
print(",".join(valid_passwords))