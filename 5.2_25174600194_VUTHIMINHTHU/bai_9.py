a = list(map(int, input("Nhập giá trị: ").split(",")))
assert all(x % 2 == 0 for x in a),"Danh sách chứa số lẻ!"
print("Tất cả các số trong danh sách đều là chẵn.")