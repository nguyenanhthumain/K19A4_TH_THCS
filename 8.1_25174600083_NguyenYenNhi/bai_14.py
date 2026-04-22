#bai_14
"""
Viết chương trình thực hiện các yêu cầu sau:
+ Tạo một list có n phần tử là số nguyên được nhập từ bàn phím.
+ Sử dụng map, lambda: Lạo một list chứa bình phương của các số hạng thuộc
list trên.
"""
def list() :
    n = int(input("Nhập số phần tử của list: "))
    list = []
    for i in range(n):
        so = int(input(f"Nhập phần tử thứ {i+1}: "))
        list.append(so)
    return list
list_so = list()
def binh_phuong(list):
    return 
ds_binh_phuong =list(map(lambda x: x**2, list_so))
binh_phuong(list_so)

print("List chứa bình phương các số hạng là : ", ds_binh_phuong)