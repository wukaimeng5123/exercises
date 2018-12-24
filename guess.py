


import os
import random

# 用户信息存档
def data_write(user_file_path,time):
    time = str(time)
    with open(user_file_path, 'a', encoding='UTF-8') as f_user:
        f_user.writelines(time+'\n')


#用户存档读取
def data_read(user_file_path):
    with open(user_file_path, 'r', encoding='UTF-8') as f_user:
        round = f_user.read().split()
        for time in round:
            time = int(time)
    return round


import random
def guess_game(user_file_path):
    total = 0
    time = 0
    while True:
        choice = input('1.start;2.quit\n')
        if str(choice)=='1':
            total += 1
            num = random.randint(1,5)
            print('猜一个1-5的整数：')
            while True:
                time += 1
                answer = int(input())
                if answer < num:
                    print('你猜得小了')
                elif answer > num:
                    print('你猜得大了')
                else:
                    print('BINGO')
                    data_write(user_file_path, time - 1)
                    break
        elif str(choice)=='2':
            break
        if total > 0:
            print('玩家%s共猜了%d次，平均%.1f次猜中\n'%(username,total,float(time)/total))
    print('游戏结束\n%s,您累计猜了%d次，平均%.1f次猜中\n' % (username, total, float(time) / total))
    round = data_read(user_file_path)



username = input('username:')
data_path = os.getcwd()+ '/game_data'
folder = os.path.exists(data_path)
if not folder:
    os.makedirs(data_path)
user_list = os.listdir(data_path)
user_file_path = 'game_data/' + username + '.txt'
username_1 = username+'.txt'
if username_1 in user_list:
    print('来啦老弟 {} ,祝您游戏愉快!'.format(username))
    print('猜猜数字是几？')
    guess_game(user_file_path)
elif username_1 not in user_list:
    print('欢迎加入游戏 {} ,祝您游戏愉快!'.format(username))
    with open(user_file_path, 'a', encoding='UTF-8') as f_user:
        time = 1
        print('猜猜数字是几？')
        guess_game(user_file_path)