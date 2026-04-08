#bai15
x = int(input("nhap x: "))
y = int(input("nhap y: "))
ma_tran = [[i * j for j in range(y)] for i in range(x)]
print("ma tran ket qua:")
for hang in ma_tran:
    print(hang)