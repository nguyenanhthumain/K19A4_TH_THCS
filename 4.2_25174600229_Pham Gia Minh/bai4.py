n = input("Nhap so: ")
d = {'0':'khong', '1':'mot', '2':'hai', '3':'ba', '4':'bon', '5':'nam', '6':'sau', '7':'bay', '8':'tam', '9':'chin'}

# FOR
res_f = ""
for c in n: res_f += d[c] + " "
print("For:", res_f.strip())

# WHILE
res_w = ""; i = 0
while i < len(n):
    res_w += d[n[i]] + " "
    i += 1
print("While:", res_w.strip())