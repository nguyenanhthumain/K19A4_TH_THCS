#bai_13
"""
Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy
và kiểm tra xem chúng có đáp ứng những tiêu chí trên hay không. Mật khẩu hợp lệ
sẽ được in, mỗi mật khẩu cách nhau bởi dấu phẩy. Ví dụ nếu mật khẩu nhập vào
chương trình là: ABd1234@1, a FI#,2w3E*, 2We3345 thì đầu ra sẽ là:
ABd1234@1.
"""

mk = input("Nhập chuỗi : ")
ds = mk.split(",")
mk_hop_le = []
for password in ds:
    password = password.strip()
    if (6 <= len(password) <= 12):
        chu_thuong = False
        so = False
        chu_hoa = False
        ky_tu_db = False
        for ki_tu in password:
            if "a" <= ki_tu <= "z":
                chu_thuong = True   
            elif "A" <= ki_tu <= "Z":
                chu_hoa = True  
            elif "0" <= ki_tu <= "9":
                so = True
            elif ki_tu in "@#$":
                ky_tu_db = True
        if chu_thuong and chu_hoa and so and ky_tu_db:
            mk_hop_le.append(password)
print("Mật khẩu hợp lệ là: ", ",".join(mk_hop_le))