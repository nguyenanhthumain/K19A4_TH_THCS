lst = []  

#a:nhập danh sách
while True:
    n = int(input())
    if n == 0:
        break
    lst.append(n)

#b:tìm x và in vị trí
x = int(input())
if x in lst:
    print("Vi tri cua x:", lst.index(x))
else:
    print("Khong tim thay x")
    
#c