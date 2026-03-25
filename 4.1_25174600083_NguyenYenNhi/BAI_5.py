# Bài 5:
"""
Viết chương trình nhập vào một số nguyên và in kết quả ra màn hình dưới
dạng số đảo ngược (về thứ tự) của số nguyên vừa nhập đó.
"""

n = int(input("Nhập một số nguyên dương : "))
if n < 0 :
    print("Yêu cầu nhập lại.")      
else :
    so_nghich_dao = 0
    while n > 0 :
        so_nghich_dao = so_nghich_dao * 10 + n 
        n = n // 10
    print("Số đảo ngược của số nguyên vừa nhập là : ", so_nghich_dao)