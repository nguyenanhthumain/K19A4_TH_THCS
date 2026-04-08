danh_sach=[]
while True:
    x=int(input())
    if x==0: break
    danh_sach=danh_sach+[x]

chen=[1,2,3]
danh_sach=chen+danh_sach+danh_sach[-len(chen):]  
if len(danh_sach)>=5: danh_sach=danh_sach[:4]+chen+danh_sach[4:]
print("Sau khi chèn:",danh_sach)

k=int(input("Vị trí k để xóa: "))
if 0<=k<len(danh_sach): danh_sach=danh_sach[:k]+danh_sach[k+1:]
print("Sau khi xóa:",danh_sach)

ds=danh_sach[:]
n=len(ds)
for i in range(n-1):
    for j in range(n-1-i):
        if ds[j]>ds[j+1]: ds[j],ds[j+1]=ds[j+1],ds[j]
print("Tăng dần:",ds)

ds2=danh_sach[:]
for i in range(n-1):
    for j in range(n-1-i):
        if ds2[j]<ds2[j+1]: ds2[j],ds2[j+1]=ds2[j+1],ds2[j]
print("Giảm dần:",ds2)