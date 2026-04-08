s = input("Nhập chuỗi: ")

# bỏ khoảng trắng thừa
words = s.strip().split()
result = " ".join(words)

print(result)