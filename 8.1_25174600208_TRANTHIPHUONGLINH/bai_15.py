# Bai 15
# a) Tao list chan 
def tao_chan():
    i = 1
    ds = []
    while i <= 100:
        if i % 2 == 0:
            ds.append(i)
        i += 1
    return ds

# b) Tong chan 
def tong_chan(n):
    tong = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            tong += i
    return tong

print(tao_chan())

n = int(input("Nhap n: "))
print("Tong chan:", tong_chan(n))