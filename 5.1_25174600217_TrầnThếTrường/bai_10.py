n = int(input("Nhập số lượng phần tử n: "))
lst = []
print("Nhập các số nguyên dương:")

for i in range(n):
    x = int(input(f"Phần tử {i+1}: "))
    lst.append(x)
tp = tuple(lst)
print("Tuple ban đầu:", tp)
odd_tp = tuple([x for x in tp if x > 0 and x % 2 == 1])

print("Tuple chứa các số nguyên dương lẻ:", odd_tp)