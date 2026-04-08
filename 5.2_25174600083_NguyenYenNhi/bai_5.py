#bai_5
"""
Viết chương trình sinh một dãy list A gồm 1000 số tự nhiên, nằm ngẫu nhiên trong
khoảng [1,99999] sao cho giá trị đó thoả mãn không chia hết cho 7.
"""
list_A = []
n = 1
while len(list_A) < 1000:
    if n % 7 != 0:
        list_A.append(n)
    n += 1
print("dãy A là :", list_A[:100])