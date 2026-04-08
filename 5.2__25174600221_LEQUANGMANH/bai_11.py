import random

# Nhập danh sách A ban đầu
n = int(input("Nhập số lượng phần tử n: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
print("Danh sách A:", A)

# a. Tạo danh sách B: chia hết cho 3 nhưng không chia hết cho 5
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("11a. Danh sách B:", B)

# b. Tạo danh sách C: bình phương các phần tử của A
C = [x**2 for x in A]
print("11b. Danh sách C:", C)

# c. Tạo danh sách D: lấy ngẫu nhiên các phần tử từ A mà chia hết cho 3
# Bước 1: Lọc ra các số chia hết cho 3
chia_het_3 = [x for x in A if x % 3 == 0]

# Bước 2: Lấy ngẫu nhiên (giả sử lấy ngẫu nhiên 2 phần tử nếu có đủ)
if len(chia_het_3) > 0:
    # Lấy ngẫu nhiên k phần tử (ở đây mình ví dụ lấy 1 số ngẫu nhiên)
    D = [random.choice(chia_het_3)] 
    print("11c. Danh sách D (ngẫu nhiên 1 số chia hết cho 3 từ A):", D)
else:
    print("11c. Không có số nào trong A chia hết cho 3 để tạo D.")