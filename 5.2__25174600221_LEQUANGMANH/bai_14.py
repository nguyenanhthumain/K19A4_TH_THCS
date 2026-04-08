data = []
while True:
    s = input("Nhập thông tin (Tên,Tuổi,Điểm) - Trống để dừng: ")
    if not s:
        break
    # Tách chuỗi và ép kiểu: tên (string), tuổi (int), điểm (int)
    name, age, score = s.split(",")
    data.append((name.strip(), int(age), int(score)))

# Python có cơ chế mặc định khi sắp xếp tuple: 
# Nó sẽ so sánh phần tử đầu tiên, nếu bằng nhau sẽ xét đến phần tử thứ 2, và cứ thế.
# Đây chính là yêu cầu Tên > Tuổi > Điểm.
# Chúng ta dùng Bubble Sort để không vi phạm quy tắc "không dùng thư viện thuật toán".

n = len(data)
for i in range(n):
    for j in range(0, n-i-1):
        # So sánh toàn bộ tuple
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print("Danh sách sau khi sắp xếp:")
for item in data:
    print(item)