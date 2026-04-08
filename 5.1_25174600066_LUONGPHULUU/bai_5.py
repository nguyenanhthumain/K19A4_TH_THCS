n = int(input("Nhập n: "))
numbers = []
i = 1
while i <= n:
    numbers.append(i)
    i += 1
snt_list = []
shh_list = []
idx = 0
while idx < len(numbers):
    x = numbers[idx]
    if x >= 2:
        is_prime = True
        j = 2
        while j < x:
            if x % j == 0:
                is_prime = False
                break
            j += 1
        if is_prime:
            snt_list.append(x)
    if x >= 2:
        total = 0
        j = 1
        while j < x:
            if x % j == 0:
                total += j
            j += 1
        if total == x:
            shh_list.append(x)
    idx += 1
print("Danh sách số nguyên tố:", snt_list)
print("Danh sách số hoàn hảo:", shh_list)