def tao_list():
    n = int(input("Nhập số lượng phần tử n: "))
    lst = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)
    return lst

def binh_phuong_list(lst):
    return list(map(lambda x: x * x, lst))

def main():
    ds = tao_list()
    print("List ban đầu:", ds)
    ds_bp = binh_phuong_list(ds)
    print("List bình phương:", ds_bp)
main()