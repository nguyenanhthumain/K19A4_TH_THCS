n = int(input("Nhập số lượng phần tử n: "))
lst = []
print("Nhập các số nguyên:")
for i in range(n):
    x = int(input())
    lst.append(x)
tp = tuple(lst)
print("Tuple ban đầu:", tp)
lst_le = []
for i in range(len(tp)):
    if tp[i] > 0 and tp[i] % 2 != 0:
        lst_le.append(tp[i])
tp_le = tuple(lst_le)
print("Tuple chứa các số nguyên dương lẻ:", tp_le)