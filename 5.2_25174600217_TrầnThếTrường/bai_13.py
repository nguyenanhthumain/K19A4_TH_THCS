passwords = input("Nhập mật khẩu: ")

password_list = [pw.strip() for pw in passwords.split(",")]
valid_passwords = []

for pw in password_list:
    if len(pw) < 6 or len(pw) > 12:
        continue
    has_lower = any(ch.islower() for ch in pw)     
    has_digit = any(ch.isdigit() for ch in pw)     
    has_upper = any(ch.isupper() for ch in pw)     
    has_special = any(ch in "S#@" for ch in pw)     
    if has_lower and has_digit and has_upper and has_special:
        valid_passwords.append(pw)
print(", ".join(valid_passwords))