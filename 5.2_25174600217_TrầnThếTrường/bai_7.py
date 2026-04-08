# a.
List_ = [["mon", 73], ["tue", 89], ["wed", 95],
         ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("a. Danh sách List_:")
for item in List_:
    print(item)

# b.
b_value = List_[2][1]
print("b. Phần tử thứ hai của sublist thứ 3 là:", b_value)

# c.
length_before = len(List_)
print("c. Độ dài List_ trước khi thêm:", length_before)

new_value = (length_before * 37 + 123) % 200 + 1
new_sublist = ["new", new_value]

List_.append(new_sublist)
print("   Đã thêm sublist:", new_sublist)
print("   Độ dài List_ sau khi thêm:", len(List_))

#d.
days_need = ["mon", "tue", "sat", "sun"]
total_sale = 0
for day, value in List_:
    if day in days_need:
        total_sale += value

print("d. Tổng sale value của Mon, Tue, Sat, Sun =", total_sale)