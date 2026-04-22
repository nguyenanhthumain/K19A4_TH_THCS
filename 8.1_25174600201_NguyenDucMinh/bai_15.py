#câu a
even_list = []

for i in range(1, 101):
    if i % 2 == 0:
        even_list.append(i)

print("Các số chẵn từ 1 đến 100:", even_list)

#câu b 
n = int(input("Nhập n: "))

tong = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        tong = tong + i

print("Tổng các số chẵn:", tong)