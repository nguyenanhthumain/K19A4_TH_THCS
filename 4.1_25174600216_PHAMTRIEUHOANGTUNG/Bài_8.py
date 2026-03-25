ds_snt = []
 
for so in range(2, 1001):
    la_snt = True
    i = 2
    while i * i <= so:
        if so % i == 0:
            la_snt = False
            break
        i += 1
    if la_snt:
        ds_snt.append(so)
 
print(f"Có {len(ds_snt)} số nguyên tố từ 1 đến 1000:")
print(ds_snt)