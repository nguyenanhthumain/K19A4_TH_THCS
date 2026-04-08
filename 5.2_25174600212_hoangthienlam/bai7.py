
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("a. Các phần tử trong List_:")
for sub in List_:
    print(sub)
val_b = List_[2][1] 
print(f"b. Phần tử thứ hai của sublist thứ 3 là: {val_b}")
print(f"c. Độ dài hiện tại của List_: {len(List_)}")
List_.append(["new_day", 100])
print("List_ sau khi thêm sublist mới:", List_)
targets = ["mon", "tue", "sat", "sun"]
tong_sale = 0
for sub in List_:
    if sub[0] in targets:
        tong_sale += sub[1]
print(f"d. Tổng sale value (mon, tue, sat, sun): {tong_sale}")