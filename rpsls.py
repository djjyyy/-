#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��Ž���
���ڣ�2022/5/10
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
import random
def name_to_number(name):
 if name=='ʯͷ':
    number=0
 elif name=='ʷ����':
    number=1
 elif name=='��':
    number=2
 elif name=='����':
    number=3
 elif name=='����':
    number=4
 return number
def number_to_name(number):
  if number==0:
      name='ʯͷ'
  elif number==1:
      name='ʷ����'
  elif number==2:
      name='��'
  elif number==3:
      name='����'
  else:
      name='����'
  return name
def rpsls(player_choice):
    comp_number=random.randrange(0,4)
    computer_choice = number_to_name(comp_number)
    print("�������ѡ��Ϊ��%s" % computer_choice)
    player_choice_number=name_to_number(player_choice)
    if player_choice_number==comp_number:
      print("���ͼ��������һ����")
    elif player_choice_number-comp_number==1 or player_choice_number-comp_number==2:
      print("��Ӯ��")
    elif comp_number==3 and player_choice_number==0:
      print("��Ӯ��")
    elif comp_number==4 and player_choice_number==0:
      print("��Ӯ��")
    elif comp_number==4 and player_choice_number==1:
      print("��Ӯ��")
    else:
      print("�����Ӯ��")
    return

if choice_name=='ʯͷ' or choice_name=='����' or choice_name=='ʷ����' or choice_name=='��' or choice_name=='����':
 print("------------")
 print("����ѡ��Ϊ��%s" % choice_name)
 rpsls(choice_name)
else:
 print('Error: No Correct Name')

