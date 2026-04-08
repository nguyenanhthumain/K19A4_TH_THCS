import random
so_ngau_nhien = random.sample([i for i in range(201) if i % 35 == 0], 1)
print(f"Số ngẫu nhiên được chọn: {so_ngau_nhien}")
