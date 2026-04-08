n = int(input("n = "))
a = [int(input()) for _ in range(n)]

# a.
u = sorted(set(a), reverse=True)
if len(u) < 2:
    print("Không có phần tử lớn thứ hai")
else:
    second = u[1]
    print("a.", second, a.index(second))

# b.
max_len = cur = 0
for x in a:
    cur = cur + 1 if x > 0 else 0
    max_len = max(max_len, cur)
print("b.", max_len)

# c.
max_sum = cur_sum = cur_len = best_len = 0
for x in a:
    if x > 0:
        cur_sum += x
        cur_len += 1
    else:
        if cur_sum > max_sum:
            max_sum, best_len = cur_sum, cur_len
        cur_sum = cur_len = 0

if cur_sum > max_sum:
    max_sum, best_len = cur_sum, cur_len

print("c. Tổng lớn nhất =", max_sum, ", số lượng =", best_len)