#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：杜金阳
日期：2022/5/10
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
import random
def name_to_number(name):
 if name=='石头':
    number=0
 elif name=='史波克':
    number=1
 elif name=='布':
    number=2
 elif name=='蜥蜴':
    number=3
 elif name=='剪刀':
    number=4
 return number
def number_to_name(number):
  if number==0:
      name='石头'
  elif number==1:
      name='史波克'
  elif number==2:
      name='布'
  elif number==3:
      name='蜥蜴'
  else:
      name='剪刀'
  return name
def rpsls(player_choice):
    comp_number=random.randrange(0,4)
    computer_choice = number_to_name(comp_number)
    print("计算机的选择为：%s" % computer_choice)
    player_choice_number=name_to_number(player_choice)
    if player_choice_number==comp_number:
      print("您和计算机出的一样呢")
    elif player_choice_number-comp_number==1 or player_choice_number-comp_number==2:
      print("您赢了")
    elif comp_number==3 and player_choice_number==0:
      print("您赢了")
    elif comp_number==4 and player_choice_number==0:
      print("您赢了")
    elif comp_number==4 and player_choice_number==1:
      print("您赢了")
    else:
      print("计算机赢了")
    return

if choice_name=='石头' or choice_name=='剪刀' or choice_name=='史波克' or choice_name=='布' or choice_name=='蜥蜴':
 print("------------")
 print("您的选择为：%s" % choice_name)
 rpsls(choice_name)
else:
 print('Error: No Correct Name')

