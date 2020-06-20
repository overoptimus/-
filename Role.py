from Weapon import WoodWeapon, IronWeapon, MagicWeapon


class Role(object):
    def __init__(self, name, weapon=None):
        super(Role, self).__init__()
        self.__name = name
        self.__weapon = weapon

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getWeapon(self):
        return self.__weapon

    def setWeapon(self, weapon):
        self.__weapon = weapon

    def attack(self, monster):
        # 攻击怪兽的逻辑
        if self.__weapon == None:
            print(self.__name, '没有装备武器，请先装备武器')
        elif monster.getHealthPoint() <= 0:
            print('怪物',monster.getName(),'已死，无法攻击')
        else:
            self.__weapon.attackMonster(monster)

    def exchangeWeapon(self, weapon):
        if weapon == '木剑':
            self.__weapon = WoodWeapon()
        elif weapon == '铁剑':
            self.__weapon = IronWeapon()
        else:
            self.__weapon = MagicWeapon()
