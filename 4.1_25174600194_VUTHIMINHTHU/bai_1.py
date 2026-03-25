n = int(input("Nhập giá trị:"))
if n>0:
    for i in range (n,n*n+1):
        print(i,end =" ")
else:
    print(f"Yêu cầu nhập lại")