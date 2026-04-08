password = input("Nhập mật khẩu: ")
if len(password) < 6 or len(password) > 12:
    print("Mật khẩu không hợp lệ: độ dài phải từ 6 đến 12 ký tự.")
else:
    has_lower = any(ch.islower() for ch in password)         
    has_digit = any(ch.isdigit() for ch in password)          
    has_upper = any(ch.isupper() for ch in password)         
    has_special = any(ch in "S#@" for ch in password)        

    if has_lower and has_digit and has_upper and has_special:
        print("Mật khẩu hợp lệ.")
    else:
        print("Mật khẩu không hợp lệ.")