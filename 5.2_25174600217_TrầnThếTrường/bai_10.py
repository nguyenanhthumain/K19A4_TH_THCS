valid_numbers = [x for x in range(201) if x % 35 == 0]

i = int(input("Nhập một số bất kỳ để tạo ngẫu nhiên: "))
index = (i * 37 + 123) % len(valid_numbers)
result = valid_numbers[index]

print("Số chia hết cho 5 và 7 từ 0 đến 200 là:", result)