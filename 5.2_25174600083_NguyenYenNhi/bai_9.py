#bai_9
"""
Viết chương trình sử dụng lệnh assert để xác minh rằng tất cả các số trong một list
được nhập vào là chẵn.
"""


ds = list(map(int, input(f"Nhập danh sách : ").split()))
for i in ds:
    assert i % 2 == 0 , f"Số {i} không là số chẵn."
print("Tất cả các số trong danh sách đều là số chẵn.")