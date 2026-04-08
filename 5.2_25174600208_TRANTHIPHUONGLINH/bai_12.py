pwd = input("Nhập mật khẩu: ")

#a
chu_thuong = False
for i in range(len(pwd)):
    if pwd[i] >= 'a' and pwd[i] <= 'z':
        chu_thuong = True
        break

#b
chu_hoa = False
for i in range(len(pwd)):
    if pwd[i] >= 'A' and pwd[i] <= 'Z':
        chu_hoa = True
        break

#c
co_so = False
for i in range(len(pwd)):
    if pwd[i] >= '0' and pwd[i] <= '9':
        co_so = True
        break

#d
co_ky = False
for i in range(len(pwd)):
    if pwd[i] == 'S' or pwd[i] == '#' or pwd[i] == '@':
        co_ky = True
        break

#e,f
do_dai = len(pwd)
if do_dai >= 6 and do_dai <= 12:
    ok_do_dai = True
else:
    ok_do_dai = False

if chu_thuong and chu_hoa and co_so and co_ky and ok_do_dai:
    print("Mật khẩu hợp lệ")
else:
    print("Mật khẩu không hợp lệ")