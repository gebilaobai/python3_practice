# password = "baiyang"
# i = 0
# while i <= 3:
#     username = input("请输入用户名：")
#     pw = input("请输入密码：")
#     if pw == password:
#         print("登录成功")
#         break
#     else:
#         print("请重新输入。。。")
#     i += 1



# for i in range(0,100):
#     if i % 2 != 0:
#         print(i)

# for i in range(0,100):
#     if i in range(50,71):
#         continue
#     else:print(i)

# _username = "baiyang"
# _password = "abc123"
#
# passed_authentication = False
#
# for i in range(3):
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#
#     if username == _username and password == _password:
#         passed_authentication = True
#         print("欢迎 %s 登录。。。" % username)
#         break
#     else:
#         print("用户名或密码错误~！")
#
# if  not passed_authentication :
#     print("别试了臭不要脸")
#


_username = "baiyang"
_password = "abc123"
for i in range(3):
    username = input("请输入用户名：")
    password = input("请输入密码：")

    if username == _username and password == _password:
        print("欢迎 %s 登录。。。" % username)
        break
    else:
        print("用户名或密码错误~！")

else:
    print("别试了臭不要脸")