ds_thoa_man = [i for i in range(0, 201) if i % 35 == 0]

if ds_thoa_man:
    vi_tri_giua = len(ds_thoa_man) // 2
    so_chon_duoc = ds_thoa_man[vi_tri_giua]
    print("Danh sách các số thỏa mãn:", ds_thoa_man)
    print("Số chọn được từ danh sách:", so_chon_duoc)