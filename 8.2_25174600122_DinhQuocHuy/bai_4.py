def dao_nguoc_danh_sach(ds):

    ds_dao = []
    for i in range(len(ds) - 1, -1, -1):
        ds_dao.append(ds[i])
    return ds_dao


input_str = input("Nhập các phần tử của danh sách, cách nhau bằng dấu cách: ")
ds_goc = input_str.split()  
ds_dao = dao_nguoc_danh_sach(ds_goc)
print("Danh sách gốc:", ds_goc)
print("Danh sách sau khi đảo ngược:", ds_dao)