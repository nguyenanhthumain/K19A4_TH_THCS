print("CÁCH 1:FOR")
for _ in range(9999):
    n = input("Nhập số bất kỳ (Cách 1): ")
    if '.' in n or int(n) < 0:
        print("-> Đã phát hiện số âm hoặc số thập phân\n")
        break

print("CÁCH 2:WHILE")
while True:
    n = input("Nhập số bất kỳ (Cách 2): ")
    if '.' in n or int(n) < 0:
        print("-> Đã phát hiện số âm hoặc số thập phân")
        break