import random
thang = 0
thua = 0
hoa = 0
for i in range(5):
    nguoi = input()
    r = random.randint(1,3)
    if r == 1:
        may = "bua"
    elif r == 2:
        may = "keo"
    else:
        may = "la"
    if nguoi == may:
        hoa = hoa + 1
    else:
        if nguoi == "bua" and may == "keo":
            thang += 1
        elif nguoi == "keo" and may == "la":
            thang += 1
        elif nguoi == "la" and may == "bua":
            thang += 1
        else:
            thua += 1
print(thang)
print(thua)
print(hoa)