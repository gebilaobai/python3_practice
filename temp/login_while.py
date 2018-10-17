_username = "baiyang"
_password = "abc123"

counter = 0

while counter < 3:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == _username and password == _password:
        print("欢迎 %s 登录。。。" % username)
        break
    else:
        print("用户名或密码错误~！")
    counter += 1
    if counter == 3:
        keep_going_choice = input("还想玩么？【y/n】")
        if keep_going_choice == 'y':
            counter = 0
else:
    print("别试了臭不要脸")