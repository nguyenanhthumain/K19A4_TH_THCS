#WHILE
print("Bắt đầu nhập số (Chương trình sẽ dừng nếu là số âm hoặc số thập phân):")

while True:
    n = input("Nhập một số: ")
    
    if "." in n:
        print("Dừng chương trình vì bạn đã nhập số thập phân.")
        break
    
    
    n = int(n)
    if n < 0:
        print("Dừng chương trình vì bạn đã nhập số âm.")
        break
        
    print(f"Bạn vừa nhập số: {n}")



#FOR
print("Nhập số nguyên dương:")

for i in range(10**6): 
    nhap = input(f"Lần nhập thứ {i+1}: ")
    
    if "." in nhap:
        print("Dừng chương trình: Bạn vừa nhập một số thập phân.")
        break
    
    n = int(nhap)
    if n < 0:
        print("Dừng chương trình: Bạn vừa nhập một số âm.")
        break
    
    print(f"Số vừa nhập: {n}")