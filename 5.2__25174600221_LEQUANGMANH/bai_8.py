n = int(input("Nhập n: "))
fib = [0, 1]
# Tạo dãy trước
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

# List comprehension để format chuỗi
result = ", ".join([str(x) for x in fib[:n]])
print(result)