#cau15
#a
ds_chan = []

for i in range(1, 101):
    if i % 2 == 0:
        ds_chan.append(i)

print("List so chan [1, 100]:", ds_chan)

#b
n = int(input("Nhap n: "))
ds = []
for i in range(1, n + 1):
    ds.append(i)
ds_chan = []
for x in ds:
    if x % 2 == 0:
        ds_chan.append(x)
tong = 0
for x in ds_chan:
    tong = tong + x
print("Danh sach ban dau:", ds)
print("Danh sach so chan:", ds_chan)
print("Tong cac so chan la:", tong)