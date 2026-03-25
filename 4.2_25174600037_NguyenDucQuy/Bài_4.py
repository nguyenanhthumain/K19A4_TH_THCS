n_str = input("Nhập số: ")
chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
res = ""
for ky_tu in n_str:
    res += chu[int(ky_tu)] + " "
print(res.strip())
#
n_str = input("Nhập số: ")
chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
res = ""
i = 0
while i < len(n_str):
    res += chu[int(n_str[i])] + " "
    i += 1
print(res.strip())