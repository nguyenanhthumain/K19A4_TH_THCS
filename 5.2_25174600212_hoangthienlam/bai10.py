import random
candidates = [i for i in range(201) if i % 5 == 0 and i % 7 == 0]
if candidates:
    print(f"Số ngẫu nhiên chia hết cho 5 và 7 trong khoảng [0, 200]: {random.choice(candidates)}")
else:
    print("Không tìm thấy số nào thỏa mãn.")