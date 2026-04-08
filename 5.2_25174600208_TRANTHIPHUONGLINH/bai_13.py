pwds = input("Nhập các mật khẩu, cách nhau bằng dấu phẩy: ")
pwds_list = []
current = ""
for i in range(len(pwds)):
    if pwds[i] != ',':
        current += pwds[i]
    else:
        pwds_list.append(current)
        current = ""
pwds_list.append(current)

res = []
for i in range(len(pwds_list)):
    pwd = pwds_list[i].strip()
    chu_thuong = False
    chu_hoa = False
    co_so = False
    co_ky = False

    for j in range(len(pwd)):
        if pwd[j] >= 'a' and pwd[j] <= 'z':
            chu_thuong = True
        if pwd[j] >= 'A' and pwd[j] <= 'Z':
            chu_hoa = True
        if pwd[j] >= '0' and pwd[j] <= '9':
            co_so = True
        if pwd[j] == 'S' or pwd[j] == '#' or pwd[j] == '@':
            co_ky = True

    if len(pwd) >= 6 and len(pwd) <= 12 and chu_thuong and chu_hoa and co_so and co_ky:
        res.append(pwd)

print("Mật khẩu hợp lệ:")
for i in range(len(res)):
    print(res[i], end=', ' if i < len(res)-1 else '\n')