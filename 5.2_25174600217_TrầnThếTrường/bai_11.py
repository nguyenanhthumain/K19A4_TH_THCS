n = int(input("Nhập số lượng phần tử n: "))
A = [int(input(f"A[{i}] = ")) for i in range(n)]
print("Danh sách A:", A)

# a.
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("a. Danh sách B (chia hết cho 3, không chia hết cho 5):", B)

# b.
C = [x * x for x in A]
print("b. Danh sách C (bình phương A):", C)

# c.
D = []
i = 1  
valid = [x for x in A if x % 3 == 0]

for _ in range(len(valid)):
    index = (i * 37 + 123) % len(valid)
    D.append(valid[index])
    i += 1
print("c. Danh sách D (lấy ngẫu nhiên từ A chia hết cho 3):", D)