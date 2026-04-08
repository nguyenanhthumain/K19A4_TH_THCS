username = input("Nhập username: ")
password = input("Nhập password: ")
# a:
dk1 = any('a' <= c <= 'z' for c in password)
# b:
dk2 = any('0' <= c <= '9' for c in password)
# c:
dk3 = any('A' <= c <= 'Z' for c in password)
# d:
dk4 = any(c in "S#@" for c in password)
# e + f
dk5 = 6 <= len(password) <= 12
if dk1 and dk2 and dk3 and dk4 and dk5:
    print("Mật khẩu hợp lệ")
else:
    print("Mật khẩu không hợp lệ")