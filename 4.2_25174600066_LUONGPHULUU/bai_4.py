 # Cách 1 while:4
chu_so = ["không", "một", "hai", "ba", "bốn", 
          "năm", "sáu", "bảy", "tám", "chín"]

n = int(input("Nhập số: "))
temp = n
ket_qua = ""
dao = 0
while temp > 0:
    dao = dao * 10 + temp % 10
    temp //= 10
while dao > 0:
    so = dao % 10
    ket_qua += chu_so[so] + " "
    dao //= 10

print("Kết quả:", ket_qua)
# Cách 2 for:
chu_so = ["không", "một", "hai", "ba", "bốn", 
          "năm", "sáu", "bảy", "tám", "chín"]

n = input("Nhập số: ")
ket_qua = ""
for ky_tu in n:
    ket_qua += chu_so[int(ky_tu)] + " "

print("Kết quả:", ket_qua)
