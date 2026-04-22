# Bai 9
# Phep tinh co ban
def thuc_hien_phep_tinh(a, b):
    print("Cong:", a + b)
    print("Tru:", a - b)
    print("Nhan:", a * b)
    if b != 0:
        print("Chia:", a / b)
        
        
# Luy thua
def tinh_luy_thua(a, b, n):
    print("a^(b+n):", a ** (b+n))
    print("b^(n+2)*a:", (b ** (n+2)) * a)

a = int(input())
b = int(input())
n = int(input())

thuc_hien_phep_tinh(a, b)
tinh_luy_thua(a, b, n)