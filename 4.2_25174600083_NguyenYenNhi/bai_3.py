# bai_3
"""
Viết chương trình nhập vào số bất kỳ từ bàn phím, chương trình chỉ dừng khi
gặp số âm hoặc số thập phân.
"""
# for
n = float(input("Nhập một số: "))
for i in range(10000000) :
    if n < 0 or n % 1 != 0 :
        print("Yêu cầu nhập lại")
        break
    else :
        print("Số bạn vừa nhập là: ", n)
        break

# while
n = float(input("Nhập một số: "))
while True :
    if n < 0 or n % 1 != 0 :
        print("Yêu cầu nhập lại")
        break
    else :
        print("Số bạn vừa nhập là: ", n)
        break