n = int(input("Nhập số > 100: "))
while n <= 100:
    n = int(input("Nhập lại giá trị: "))
s = 0
t = n
while t > 0:
    s += t % 10
    t //= 10
print(s)





n = int(input("Nhập số > 100: "))
while n <= 100:
    n = int(input("Nhập lại giá trị: "))
s = 0
for ch in str(n):
    s += int(ch)
print(s)