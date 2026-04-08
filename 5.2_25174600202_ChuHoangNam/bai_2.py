#cau2
n = int(input("Nhap n: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhap phan tu thu {i}: ")))
max1 = a[0]
for x in a:
    if x > max1:
        max1 = x

max2 = -float('inf') 
vi_tri_max2 = -1
for i in range(len(a)):
    if a[i] < max1 and a[i] > max2:
        max2 = a[i]
        vi_tri_max2 = i
max_lien_tiep = 0
hien_tai_lien_tiep = 0

max_tong_duong = 0
hien_tai_tong_duong = 0

for x in a:
    if x > 0:
        hien_tai_lien_tiep += 1
        if hien_tai_lien_tiep > max_lien_tiep:
            max_lien_tiep = hien_tai_lien_tiep
        
        hien_tai_tong_duong += x
        if hien_tai_tong_duong > max_tong_duong:
            max_tong_duong = hien_tai_tong_duong
    else:
        hien_tai_lien_tiep = 0
        hien_tai_tong_duong = 0

print(f"Gia tri lon thu hai: {max2} tai vi tri: {vi_tri_max2}")
print(f"So luong so duong lien tiep nhieu nhat: {max_lien_tiep}")
print(f"Tong so duong lien tiep lon nhat: {max_tong_duong}")