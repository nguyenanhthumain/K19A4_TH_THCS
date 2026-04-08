n = int(input("Nhập n phần tử cho danh sách A: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
print("Danh sách A:", A)
A_duong = [x for x in A if x > 0]
print("Các số dương trong A:", A_duong)
A_binh_phuong = [x**2 for x in A]
print("Bình phương các phần tử A:", A_binh_phuong)