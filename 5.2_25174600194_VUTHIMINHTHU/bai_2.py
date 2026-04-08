lst = []
while True:
    so = int(input("Nhập gia tri: "))
    if so == 0:
        break
    lst.append(so)
print("Danh sách ban đầu:", lst)
phn_tu_duong = [x for x in lst if x > 0]
phn_tu_am = [x for x in lst if x <= 0]
lst = phn_tu_duong+phn_tu_am
print("a.Danh sách sau khi chuyển số dương lên đầu:", lst)
m = int(input("Nhập số m muốn chèn: "))
lst.insert(0, m)        
lst.append(m)           
if len(lst) >= 5:
    lst.insert(4, m)    
else:
    lst.append(m)       
print("b.Danh sách sau khi chèn số m:", lst)