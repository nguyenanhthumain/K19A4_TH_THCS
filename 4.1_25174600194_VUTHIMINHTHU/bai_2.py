m = int(input("Nhập giá trị m:"))
n = int(input("Nhập giá trị n:"))
if m<n:
    m,n = n,m
while m!=n:
        r = m-n
        if m>n:
            m=r
        else :
            m=n
            n=r
print(f"Ước chung lớn nhất là:",m)