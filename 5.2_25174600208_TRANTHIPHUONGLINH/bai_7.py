#a
List_=[["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
print("List tuần:",List_)

#b
print("Phần tử thứ 2 sublist 3:", List_[2][1])

#c
import random
print("Độ dài list:",len(List_))
sub = [random.randint(0,100),random.randint(0,100)]
List_.append(sub)
print("Sau khi thêm sublist:",List_)

#d
tong = List_[0][1]+List_[1][1]+List_[5][1]+List_[6][1]
print("Tổng sale các ngày Mon,Tue,Sat,Sun:",tong)