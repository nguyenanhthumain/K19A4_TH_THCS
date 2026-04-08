#bai16
n = int(input("nhap bac ma tran n: "))
ma_tran_don_vi = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print("ma tran don vi bac", n, ":")
for hang in ma_tran_don_vi:
    print(hang)