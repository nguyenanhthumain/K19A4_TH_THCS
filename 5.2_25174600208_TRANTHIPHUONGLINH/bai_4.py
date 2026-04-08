a=[]
while True:
    x = int(input("Nhập số (0 dừng): "))
    if x==0:
        break
    a.append(x)

#a chèn
a = [1,2,3]+a
a += [1,2,3]
if len(a)>=5:
    a[4:4]=[1,2,3]
else:
    a+= [1,2,3]
print("Sau khi chèn:", a)

#b xóa phần tử k
k = int(input("Nhập k: "))
if 0<=k<len(a):
    del a[k]
print("Sau khi xóa:", a)

#c sắp xếp tăng
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("Tăng:",a)

#c sắp xếp giảm
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("Giảm:",a)