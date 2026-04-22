import random
def tinh_binh_phuong():
    n = int(input("Nhập độ dài danh sách n: "))
    danh_sach = [random.randint(1, 100) for _ in range(n)]
    print(f"Danh sách ngẫu nhiên ban đầu: {danh_sach}")
    list_binh_phuong = list(map(lambda x: x**2, danh_sach))
    print(f"Danh sách sau khi bình phương: {list_binh_phuong}")
tinh_binh_phuong()
