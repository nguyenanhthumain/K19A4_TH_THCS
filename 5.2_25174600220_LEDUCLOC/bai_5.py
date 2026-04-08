"""5. Viết chương trình sinh một dãy list A gồm 1000 số tự nhiên, nằm ngẫu nhiên trong
khoảng [1,99999] sao cho giá trị đó thoả mãn không chia hết cho 7."""   

n = int(input("Nhập một số bất kỳ để bắt đầu: "))
A = []
buoc_nhay = 123  

hien_tai = n
while len(A) < 1000:
    hien_tai = (hien_tai * 31 + buoc_nhay) % 100000 
    if hien_tai >= 1 and hien_tai <= 99999:
        if hien_tai % 7 != 0:
            A.append(hien_tai)

print("Đã sinh xong 1000 số. Vài số đầu:", A[:10])