card_list = []

def show_menu():
    # 显示菜单
    print("-" * 50)
    print("欢迎使用【人员管理系统】")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("4. 删除名片")
    print("5. 修改名片")
    print("0. 退出系统")
    print("")
    print("-" * 50)

def new_card():
    # 新建名片
    print("-"*50)
    print("功能：新建名片")

    # 1.提示用户输入正确名片信息
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ号码：")
    email = input("请输入邮箱：")

    # 2.将用户信息保存到一个字典中
    card_dict = {"name":name,
                 "phone":phone,
                 "qq":qq,
                 "email":email}

    # 3.将用户字典添加到名片列表
    card_list.append(card_dict)

    print(card_dict)

    # 4.提示添加成功信息
    print("成功添加 %s 的名片" % card_dict["name"])
def show_all():
    # 显示全部
    print("-" * 50)
    print("功能：显示全部")

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t\t")

    print("")

    print("-" * 50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))

def search_card():
    # 搜索名片
    print("-" * 50)
    print("功能：搜索名片")

    # 1.提示要搜索的姓名
    find_name = input("请输入要搜索的姓名：")

    # 2.遍历字典
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱\t\t\t")
            print("-" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            print("-" * 50)

            break

    else:
        print("没有找到 %s" % find_name)

