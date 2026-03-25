n = int(input("Nhập số n: "))
#Số nguyên tố
ds_snt = []
 
for so in range(2, n + 1):
    la_snt = True
    i = 2
    while i * i <= so:
        if so % i == 0:
            la_snt = False
            break
        i += 1
    if la_snt:
        ds_snt.append(so)
 
print("Danh sách số nguyên tố:", ds_snt)
 
#Số hoàn hảo
ds_shh = []
 
for so in range(2, n + 1):
    tong_uoc = 0
    for i in range(1, so):
        if so % i == 0:
            tong_uoc += i
    if tong_uoc == so:
        ds_shh.append(so)
 
print("Danh sách số hoàn hảo:", ds_shh)