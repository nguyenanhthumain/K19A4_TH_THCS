def dao_nguoc_list():
    lst = list(map(int, input("Nhập list: ").split()))
    
    dao = []
    for i in range(len(lst)-1, -1, -1):
        dao.append(lst[i])

    print("List đảo:", dao)

dao_nguoc_list()