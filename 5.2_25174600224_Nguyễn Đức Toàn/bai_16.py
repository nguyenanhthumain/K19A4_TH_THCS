n=int(input("Nhập n: "))

ma_tran=[]

for i in range(n):
    hang=[]
    for j in range(n):
        if i==j:
            hang=hang+[1]
        else:
            hang=hang+[0]
    ma_tran=ma_tran+[hang]

for hang in ma_tran:
    print(hang)