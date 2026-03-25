"""Bài 5: Viết chương trình nhập vào một số nguyên và in kết quả ra màn hình dưới
dạng số đảo ngược (về thứ tự) của số nguyên vừa nhập đó."""
n = int(input("Nhập một số nguyên: "))
if n >= 0:
    m = 0
    while n > 0:
        a = n % 10
        m = m * 10 + a
        n //= 10
    print("Số đảo ngược là:", m)
else:
    print("Vui lòng nhập một số nguyên không âm.")