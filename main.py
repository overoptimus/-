from Monster import Monster
from Role import Role
from Weapon import WoodWeapon, IronWeapon, MagicWeapon
import time
import os


monsters = []
role = None


def initMonster():
    global monsters
    print('初始化怪物...')
    monster1 = Monster('哥不灵', 50)
    monster2 = Monster('僵尸', 50)
    monster3 = Monster('牛头人', 50)
    monster4 = Monster('孙铭琦', 200)
    monster5 = Monster('纳什男爵', 1000)
    monsters.append(monster1)
    monsters.append(monster2)
    monsters.append(monster3)
    monsters.append(monster4)
    monsters.append(monster5)


def initRole():
    global role
    roleName = input('您好，请输入您的名字：')
    print('初始化玩家...')
    role = Role(roleName)


def showMonsters(monsters):
    for m in monsters:
        print(m.getName(), m.getHealthPoint())


def attack(sM):
    global role
    role.attack(monsters[sM - 1])


def success():
    global monsters
    health = []
    for i in range(5):
        if monsters[i].getHealthPoint() <= 0:
            health.append(False)
        else:
            health.append(True)
    if not any(health):
        return True

def main():
    global role
    global monsters
    ws = ['木剑', '铁剑', '魔剑']
    print('欢迎来到地下城与勇士')
    initMonster()
    initRole()
    print('进入游戏...')
    time.sleep(2)
    while True:
        os.system('clear')
        print('1.查看怪物信息。 2.攻击怪物。 3.装备武器(可选木剑、铁剑、魔剑)。')
        selected = int(input('请选择:'))
        if selected == 1:
            showMonsters(monsters)
            time.sleep(2)
        elif selected == 2:
            # 选择怪物攻击
            while True:
                sM = int(input('请选择1-5:'))
                attack(sM)
                time.sleep(1)
                sC = int(input('是否继续攻击(1.是 2.否)：'))
                if sC == 1:
                    continue
                elif sC == 2:
                    break
                else:
                    print('请正确选择...')
                    time.sleep(1)
        elif selected == 3:
            # 选择装备武器
            sW = int(input('请选择(1.木剑 2.铁剑 3.魔剑):'))
            role.exchangeWeapon(ws[sW - 1])
        else:
            print('请选择1-3...')
            time.sleep(1)


        if success():  # 判断是否所有的怪都死了
            # os.system('clear')
            print('恭喜，通关地下城...')
            break


if __name__ == "__main__":
    main()
