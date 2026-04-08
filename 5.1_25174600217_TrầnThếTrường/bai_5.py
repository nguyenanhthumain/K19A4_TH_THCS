n = int(input("Nhập n: "))
numbers = list(range(1, n + 1))

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def is_perfect(x):
    return x > 1 and sum(i for i in range(1, x) if x % i == 0) == x

prime_list = [x for x in numbers if is_prime(x)]
perfect_list = [x for x in numbers if is_perfect(x)]

print("Số nguyên tố:", prime_list)
print("Số hoàn hảo:", perfect_list)