X=int(input("Nhập số hàng X: "))
Y=int(input("Nhập số cột Y: "))

ma_tran=[]

for i in range(X):
    hang=[]
    for j in range(Y):
        hang=hang+[i*j]
    ma_tran=ma_tran+[hang]

for hang in ma_tran:
    print(hang)