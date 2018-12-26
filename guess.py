# coding=utf-8
from random import randint
name = input('请输入你的名字：')

try:
    f = open('game.txt')
    lines =f.readlines()
    f.close()
except:
    f = open('game.txt','w+')
    lines = f.readlines()
    f.close()
scores={}
for l in lines:
    s = l.split()
    scores[s[0]]=s[1:]

score = scores.get(name)
if score is None:
    score = [0,0,0]
    print('欢迎加入游戏' + name + ',祝你游戏愉快!')
else:
    print('欢迎回来' + name + ',祝你游戏愉快!')
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

num = randint(1,100)
times=0
print('猜猜数字是几?')
bingo = False
while bingo == False:
    times += 1

    while True:
        try:
            print('第%d次'% times)
            answer = float(input('请输入100以内数字:\n'))
            if 1 <= answer <= 100:
                break
            else:
                print('第%d次' % times)
                answer = float(input('请输入100以内数字:\n'))
        except:
            pass
    if answer < num:
        print('太小了!')
    if answer > num:
        print('太大了!')
    if answer == num:
        if game_times == 0 or times < min_times:
            min_times = times
        total_times += times
        game_times += 1
        if game_times > 0:
            avg_times = float(total_times) / game_times
        else:
            avg_times = 0
        print('猜中了！答案就是', answer)
        print('你猜中答案用了%d次机会' % times)
        print('你一共玩了%d次游戏' % (game_times))
        print('你平均%.2f次猜中答案' % avg_times)
        print('你的最好成绩是%d次' % min_times)
        # 把成绩更新到对应的玩家中
        scores[name] = [str(game_times), str(min_times), str(total_times)]
        result = ''
        for n in scores:  # 把成绩按照name, game_times, min_times, total_times格式化
            line = n + ' ' + ' '.join(scores[n]) + '\n'
            result += line
        f = open('game.txt', "w")
        f.write(result)
        f.close()
        print('.....................................................')
        Play_game = input('输入go再玩一次,否则输入任意字符退出游戏：')
        if Play_game == 'go':  # 让用户选择重新游戏，同时初始化猜出轮数times
            print('新游戏')
            bingo = False
            times = 0
            num = randint(1, 100)
        else:
            bingo = True

