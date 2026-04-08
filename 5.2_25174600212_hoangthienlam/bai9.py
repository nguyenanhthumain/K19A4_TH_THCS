
input_str = input("Nhập các số nguyên, cách nhau bởi dấu cách: ")
lst = [int(x) for x in input_str.split()]
try:
    for x in lst:
        assert x % 2 == 0, f"Số {x} không phải là số chẵn!"
    print("Tất cả các số trong list đều là số chẵn.")
except AssertionError as e:
    print("Lỗi xác minh:", e)