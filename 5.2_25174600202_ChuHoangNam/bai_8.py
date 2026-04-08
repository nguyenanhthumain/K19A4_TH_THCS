#cau8
n = int(input("Nhập n: "))

f = [0, 1]

for i in range(n - 1):
    so_tiep_theo = f[i] + f[i+1]
    f.append(so_tiep_theo)

ket_qua_str = ""
for i in range(len(f)):
    if i == len(f) - 1:
        ket_qua_str = ket_qua_str + str(f[i])
    else:
        ket_qua_str = ket_qua_str + str(f[i]) + ", "

print(ket_qua_str)