n = input("Nhập giá trị:")
dict_so = {
    '0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn',
    '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín'
}
i = 0
while i < len(n):
    chu_so = n[i]
    if chu_so in dict_so:
        print(dict_so[chu_so],end=" ")
    i += 1

