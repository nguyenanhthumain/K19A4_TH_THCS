x = float(input("Nhập một số (âm để dừng): "))
so = []
 
while True:
    if x < 0:
        print("Gặp số âm, kết thúc nhập.")
        break
    so.append(x)
 
print(f"Các số dương đã nhập: {so}")