import random

class Monster(object):
    def __init__(self, name, healthPoint):
        self.__name = name
        self.__healthPoint = healthPoint

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getHealthPoint(self):
        return self.__healthPoint

    def setHealthPoint(self, healthPoint):
        self.__healthPoint = healthPoint

    def attackMethod(self):
        i = random.randint(1,2)
        if i == 1:
            return '爪子'
        else:
            return '牙'

    def handle(self, healthPoint):
        if self.__healthPoint <= 0:
            print(self.__name, '已死亡，无法攻击。')
        else:
            self.__healthPoint -= healthPoint
            print('怪兽'+self.__name+'掉血-'+str(healthPoint) +
                  ',当前血量'+(str(self.__healthPoint) if self.__healthPoint > 0 else str(0)))
            if self.__healthPoint <= 0:
                print(self.getName(), "已死亡")

    def attack(self, player):
        if self.__healthPoint <= 0:
            pass
        else:
            player.setHealthPoint(player.getHealthPoint()-5)
            print(self.getName(), '用', self.attackMethod(), '攻击玩家-5')
            print(player.getName(),'当前血量为',player.getHealthPoint())
