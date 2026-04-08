"""Viết chương trình sử dụng lệnh assert để xác minh rằng tất cả các số trong một list
được nhập vào là chẵn."""
a = list(map(int, input("Nhập danh sách a (các phần tử cách nhau bằng dấu cách): ").split()))
for i in a:
    assert i % 2 == 0, f"Số {i} không phải là số chẵn."
print("Tất cả các số trong danh sách đều là số chẵn.")