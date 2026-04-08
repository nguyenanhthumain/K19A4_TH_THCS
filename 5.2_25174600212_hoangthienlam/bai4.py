a = []
while True:
    val = int(input("Nhập số (0 để dừng): "))
    if val == 0: break
    a.append(val)
sub = [1, 2, 3]
a = sub + a             
a = a + sub             
if len(a) >= 5:
    a = a[:4] + sub + a[4:] 
print("Sau khi chèn [1,2,3]:", a)
k = int(input("Nhập vị trí k cần xóa (index): "))
if 0 <= k < len(a):
    a.pop(k)
print("Sau khi xóa:", a)
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print("Tăng dần:", a)
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print("Giảm dần:", a)