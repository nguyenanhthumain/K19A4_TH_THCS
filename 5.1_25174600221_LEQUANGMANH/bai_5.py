n = int(input("Nhập n: "))

lst = list(range(1, n + 1))

# kiểm tra nguyên tố
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# kiểm tra hoàn hảo
def is_perfect(x):
    s = 0
    for i in range(1, x):
        if x % i == 0:
            s += i
    return s == x

prime_list = []
perfect_list = []

for x in lst:
    if is_prime(x):
        prime_list.append(x)
    if is_perfect(x):
        perfect_list.append(x)

print("Số nguyên tố:", prime_list)
print("Số hoàn hảo:", perfect_list)