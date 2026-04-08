A=[]
x=12345 
while len(A)<1000:
    x=(1103515245*x+12345)%99999 +1
    A=A+[x] 
    
A_tang_sorted = sorted(A)
print("Danh sách tăng dần: ")
for x in A_tang_sorted:
    print(x, end=" ")
print("\n")

A_tang = A[:] 
n=len(A_tang)
for i in range(n-1):
    for j in range(n-1-i):
        if A_tang[j]>A_tang[j+1]:
            A_tang[j],A_tang[j+1]=A_tang[j+1],A_tang[j]

print("Danh sách tăng dần: ")
for x in A_tang:
    print(x, end=" ")
print("\n")