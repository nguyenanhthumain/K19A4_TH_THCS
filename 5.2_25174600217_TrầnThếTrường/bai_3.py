a = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    a.append(x)
print("Danh sách ban đầu:", a)

# a.
duong = [x for x in a if x > 0]
khac = [x for x in a if x <= 0]
a_new = duong + khac
print("a. Danh sách sau khi đưa số dương lên đầu:", a_new)

# b.
m = int(input("Nhập số m: "))
a_new.insert(0, m)    
a_new.append(m)      

if len(a_new) >= 5:
    a_new.insert(4, m)  
else:
    a_new.append(m)
print("b. Danh sách sau khi chèn m:", a_new)