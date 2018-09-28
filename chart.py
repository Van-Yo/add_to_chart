# Author:Vanyo
# 列表，for, while, if
# 需求：做一个类似于购物车的判断小脚本，用户先输入自己账户存款，然后在给出的商品列表里去挑选商品并完成循环购买，中途客退出
# 商品列表
products = [['bicycle',888],['iphone',5888],['cloth',688],['coffee',68],['python book',50]]
# 购物车
chart = []
# 用户输入账户存款
salary = int(input("please input your salary:"))
# 打印出商品名称及价格给用户看
print("Our products list:")
for product in products:
    print(products.index(product)+1,".",product[0],"------",product[1])
# 循环，让用户选择是否继续购物
while True:
    # 用户输入的数字与商品列表下标对应
    choice = int(input("Your best choice,please input products number to shopping:"))
    choice = choice -1
    # 先判断用户输入的数字（其他字符-待改进：try:except:）是否在商品列表的下标中
    if choice in list(range(len(products))):
        # 判断余额是否足够，如果够，直接购买，如果不够，输出提示语句
        if salary >= products[choice][1]:
            salary = salary-products[choice][1]
            chart.append(products[choice][0])
            print("product:",products[choice][0],"is added to chart")
        else:
            print("your money is not enough")
        # 向用户剔提出是否继续购买循环
        quit_or_continue = input("continue? input Y/N:")
        if quit_or_continue == "N":
            break
    else:
        print("wrong choice")
# 最后输出用户购物车列表和账户余额
print("your chart is:",chart)
print("your money remains:",salary)
