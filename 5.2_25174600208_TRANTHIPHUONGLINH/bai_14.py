n=int(input("Nhập số tuple: "))
lst=[]
for i in range(n):
    name=input("Tên: ")
    age=int(input("Tuổi: "))
    score=int(input("Điểm: "))
    lst.append((name,age,score))

#a
lst.sort(key=lambda x: (x[0],x[1],x[2]))
print("Sau khi sắp xếp:",lst)