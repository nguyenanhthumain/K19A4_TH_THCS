chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
n = input("Nhập một số: ")
ket_qua = []
for ky_tu in n:
    if ky_tu.isdigit():
        index = int(ky_tu)
        ket_qua.append(chu_so[index])
print("Kết quả:", " ".join(ket_qua))