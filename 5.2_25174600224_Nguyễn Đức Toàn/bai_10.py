x=123

while True:
    x=(x*5+3)%201  # số giả ngẫu nhiên 0-200
    if x%5==0 and x%7==0:
        so=x
        break

print("Số chia hết cho 5 và 7:", so)