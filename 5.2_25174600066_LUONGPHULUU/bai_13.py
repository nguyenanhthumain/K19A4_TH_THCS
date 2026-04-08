s = input("Nhập mật khẩu: ")
passwords = s.split(",")
result = []
for pw in passwords:
    pw = pw.strip()
    dk1 = dk2 = dk3 = dk4 = False
    for c in pw:
        if 'a' <= c <= 'z':
            dk1 = True
        elif 'A' <= c <= 'Z':
            dk3 = True
        elif '0' <= c <= '9':
            dk2 = True
        elif c in "S#@":
            dk4 = True
    if dk1 and dk2 and dk3 and dk4 and 6 <= len(pw) <= 12:
        result.append(pw)

print(",".join(result))