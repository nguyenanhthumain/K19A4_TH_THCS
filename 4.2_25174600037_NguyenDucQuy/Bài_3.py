while True:
    s = input("Nhập số: ")
    if "." in s: break 
    n = float(s)
    if n < 0: break
#
import itertools
for _ in itertools.count():
    s = input("Nhập số: ")
    if "." in s or float(s) < 0:
        print("Dừng chương trình.")
        break  