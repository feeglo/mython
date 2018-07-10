# -*- coding:UTF-8 -*-
iddressBook={}#定义通讯录
while 1:
    temp=raw_input('请输入指令代码：')
    if not temp.isdigit():
        print("输入的指令错误，请按照提示输入")
        continue
    item=int(temp)#转换为数字
    if item==4:
        print("|---感谢使用通讯录程序---|")
        break
    name = input("输入联系人:")
    if item==1:
        if name in addressBook:
            print(name,':',addressBook[name])
            continue
        else:
            print("该联系人不存在！")
    if item==2:
        if name in addressBook:
            print("您输入的姓名在通讯录中已存在",name,":",addressBook[name])
            isEdit=input("是否修改联系人资料(Y/N）:")
            if isEdit=='Y':
                userphone = input("请输入联系人电话：")
                addressBook[name]=userphone
                print("联系人修改成功")
                continue
            else:
                continue
        else:
            userphone=input("请输入联系人电话：")
            addressBook[name]=userphone
            print("联系人加入成功！")
            continue

    if item==3:
        if name in addressBook:
            del addressBook[name]
            print("删除成功！")
            continue
        else:
            print("联系人不存在")
