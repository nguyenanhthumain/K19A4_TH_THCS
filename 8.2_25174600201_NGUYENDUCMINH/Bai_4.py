def dao_nguoc_danh_sach(ds):
    ds_dao = []
    for i in range(len(ds)-1, -1, -1):
        ds_dao.append(ds[i])
    return ds_dao