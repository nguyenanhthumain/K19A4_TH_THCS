import random
# List comprehension: số chia hết cho 5 và 7 (tức chia hết cho 35) từ 0-200
nums = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]

if nums:
    print("Các số thỏa mãn:", nums)
    print("Một số ngẫu nhiên từ danh sách:", random.choice(nums))