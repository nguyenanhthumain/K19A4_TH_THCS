n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    a.append(int(input("Số thứ {}: ".format(i))))

#a 
max1 = max2 = -999999
for x in a:
    if x>max1:
        max2 = max1
        max1 = x
    elif x>max2 and x!=max1:
        max2 = x
vitri_max2 = -1
for i in range(len(a)):
    if a[i]==max2:
        vitri_max2 = i
        break
print("Lớn thứ 2:", max2,"Vị trí:", vitri_max2)

#b 
cur = 0
maxlen = 0
for x in a:
    if x>0:
        cur+=1
        if cur>maxlen:
            maxlen = cur
    else:
        cur =0
print("Số dương liên tiếp nhiều nhất:", maxlen)

#c 
cur = 0
sumcur = 0
maxsum = 0
for x in a:
    if x>0:
        cur+=1
        sumcur += x
        if sumcur>maxsum:
            maxsum = sumcur
            maxlen_sum = cur
    else:
        cur =0
        sumcur =0
print("Số dương liên tiếp tổng lớn nhất:", maxlen_sum)