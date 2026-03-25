# bai_4
"""
Viết chương trình nhập một số từ bàn phím và in ra màn hình bằng chữ. Ví dụ:
1234, kết quả in ra màn hình là một hai ba bốn
"""
# for
n = int(input("Nhập một số nguyên: "))
chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
for i in str(n) :
    print(chu[int(i)], end=" ")

# while
n = int(input("Nhập một số nguyên: "))
chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
i = 0   
while n > 0 :
    i = n % 10 + i * 10
    n = n // 10
while i > 0 :
    print(chu[i % 10], end=" ")
    i = i // 10