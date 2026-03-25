so = input("Nhập một số: ")
tu_dien = {'0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn',
           '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín'}

print("CÁCH 1:FOR")
ket_qua_for = ""
for chu_so in so:
    ket_qua_for += tu_dien.get(chu_so, "") + " "
print(f"Kết quả: {ket_qua_for.strip()}")


print("CÁCH 2:WHILE")
ket_qua_while = ""
i = 0
while i < len(so):
    ket_qua_while += tu_dien.get(so[i], "") + " "
    i += 1
print(f"Kết quả: {ket_qua_while.strip()}")