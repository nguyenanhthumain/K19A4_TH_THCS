#bai2
n = int(input("nhap so phan tu n: "))
a = [int(input(f"nhap phan tu thu {i+1}: ")) for i in range(n)]
print("danh sach:", a)
if len(a) < 2:
    print("khong du phan tu de tim lon thu hai")
else:
    sorted_a = sorted(set(a), reverse=True)
    if len(sorted_a) >= 2:
        lon_thu_hai = sorted_a[1]
        vitri = a.index(lon_thu_hai)
        print("phan tu lon thu hai:", lon_thu_hai, "tai vi tri", vitri)
    else:
        print("khong co phan tu lon thu hai")
max_lien_tiep = 0
hien_tai = 0
for x in a:
    if x > 0:
        hien_tai += 1
        max_lien_tiep = max(max_lien_tiep, hien_tai)
    else:
        hien_tai = 0
print("so luong so duong lien tiep nhieu nhat:", max_lien_tiep)
max_tong = 0
tong_hien_tai = 0
for x in a:
    if x > 0:
        tong_hien_tai += x
        max_tong = max(max_tong, tong_hien_tai)
    else:
        tong_hien_tai = 0
print("tong so duong lien tiep lon nhat:", max_tong)