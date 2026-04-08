#Bài 4. Tạo một list có 100 số tự nhiên đầu tiên với bước nhảy là 2 nằm trong đoạn từ m đến n với 0 < m < n được nhập từ bàn phím. Tính tổng của chúng và đưa kết quả ra màn hình. 
while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        break
    else:
        print("Điều kiện không hợp lệ. Vui lòng nhập lại.")
