import random
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("a. Các phần tử của List_:")
for item in List_:
    print(item, end=" ")
item_b = List_[2][1]
print(f"b. Phần tử thứ hai của sublist thứ 3 là: {item_b}")
print(f"c. Độ dài hiện tại của list: {len(List_)}")
sublist = ["ngau_nhien", random.randint(1, 150)]
List_.append(sublist)
print(f"Danh sách sau khi thêm sublist ngẫu nhiên {sublist}:")
print(List_)
days = ["mon", "tue", "sat", "sun"]
tong_sale = 0
for sublist in List_:
    if sublist[0] in days:
        tong_sale += sublist[1]
print(f"d. Tổng sale value của các ngày {days} là: {tong_sale}")