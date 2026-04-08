#cau7
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

print("Cac phan tu cua List_:")
for item in List_:
    print(item)

print("Phan tu yeu cau:", List_[1][1])

print("Do dai hien tai:", len(List_))
List_.append(["ngay_moi", 100])

tong_sale = 0
ngay_can_tinh = ["thu hai", "thu ba", "thu bay", "chu nhat"]
for sub in List_:
    if sub[0] in ngay_can_tinh:
        tong_sale += sub[1]

print("Tong sale value (Thu hai, Thu Ba, Thu Bay, Chu Nhat):", tong_sale)