import re
inputs = input("Nhập các mật khẩu: ").split(",")
phan_tu = []
for mk in [p.strip() for p in inputs]:
    if (6 <= len(mk) <= 12 and
        re.search("[a-z]", mk) and
        re.search("[A-Z]", mk) and
        re.search("[0-9]", mk) and
        re.search("[$#@]", mk)):
        phan_tu.append(mk)
print(",".join(phan_tu))
