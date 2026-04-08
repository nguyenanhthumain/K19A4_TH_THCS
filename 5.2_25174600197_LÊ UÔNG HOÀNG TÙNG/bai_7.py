#bai7
list_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], 
         ["fri", 115], ["sat", 128], ["sun", 120]]
print("danh sach list_:")
for item in list_:
    print(item)
print("phan tu thu hai cua sublist vi tri 3:", list_[2][1])
import random
list_.append(["random", random.randint(50, 150)])
print("sau khi them sublist:", list_)
tong = list_[0][1] + list_[1][1] + list_[5][1] + list_[6][1]
print("tong sale thu 2, thu 3, thu 7, chu nhat:", tong)