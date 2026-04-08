#cau15
X = int(input("Nhập số hàng X: "))
Y = int(input("Nhập số cột Y: "))

mang_2_chieu = []

for i in range(X):
    hang = [] 
    for j in range(Y):
        gia_tri = i * j
        hang.append(gia_tri) 
        
    mang_2_chieu.append(hang)

print(mang_2_chieu)