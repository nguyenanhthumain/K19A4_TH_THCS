#FOR
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
n = input("Nhập một số: ")
ket_qua = ""

for kytu in n:
    idx = int(kytu)
    ket_qua += chu_so[idx] + " "

print(ket_qua.strip())


#WHILE
n = input("Nhập một số: ")
ket_qua = ""

while len(n) > 0:
    kytu = n[0]
    idx = int(kytu)
    ket_qua += chu_so[idx] + " "
    n = n[1:]

print(ket_qua.strip())