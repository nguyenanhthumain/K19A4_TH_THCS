#bai_10
"""
Viết chương trình sử dụng module random và list comprehension để xuất một
số ngẫu nhiên, chia hết cho 5 và 7, từ 0 đến 200 (gồm cả 0 và 200).
"""

ds = []
for i in range(201):
    if i % 5 == 0 and i % 7 == 0:
        ds.append(i)
print("Các số ngẫu nhiên chia hết cho 5 và 7 từ 0 đến 200 là:", ds)