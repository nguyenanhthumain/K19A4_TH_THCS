m=int(input("Số hàng: "))
n=int(input("Số cột: "))
A=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(int(input("Nhập A[{}][{}]: ".format(i,j))))
    A.append(row)
tong=0
for row in A:
    for x in row:
        tong+=x
print("Tổng các phần tử:",tong)