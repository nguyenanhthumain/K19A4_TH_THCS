List_=[["mon",73],["tue",89],["wed",95],
       ["thu",103],["fri",115],["sat",128],["sun",120]]

print("Danh sách List_:")
for x in List_:
    print(x)

phan_tu = List_[2][1] 
print("Phần tử thứ hai của sublist thứ ba:", phan_tu)

test=[1,2,3]
print("Độ dài list test trước:", len(test))
sublist_ngau_nhien=[42,99]
test = test + [sublist_ngau_nhien]
print("List test sau khi thêm sublist ngẫu nhiên:", test)
print("Độ dài list test sau:", len(test))

tong = List_[1][1] + List_[2][1] + List_[5][1] + List_[6][1]
print("Tổng sale value các ngày thứ hai, thứ ba, thứ bảy, chủ nhật:", tong)