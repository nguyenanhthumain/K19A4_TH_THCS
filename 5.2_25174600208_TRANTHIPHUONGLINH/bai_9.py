a = list(map(int,input("Nhập danh sách cách nhau bằng space: ").split()))
assert all(x%2==0 for x in a),"Có số lẻ trong danh sách"
print("Tất cả số đều chẵn")