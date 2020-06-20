from abc import ABCMeta, abstractmethod
from Monster import Monster


class IWeapon(metaclass=ABCMeta):
    @abstractmethod
    def attackMonster(self, monster):
        pass


class WoodWeapon(IWeapon):
    def __init__(self):
        self.name = "木剑"

    def attackMonster(self, monster):
        print(self.name,'攻击成功')
        monster.handle(20)


class IronWeapon(IWeapon):
    def __init__(self):
        self.name = '铁剑'

    def attackMonster(self, monster):
        # 怪兽掉血的处理handle
        print(self.name,'攻击成功')
        monster.handle(50)


class MagicWeapon(IWeapon):
    def __init__(self):
        self.name = '魔剑'

    def attackMonster(self, monster):
        # 怪兽掉血的处理handle
        print(self.name,'攻击成功')
        monster.handle(100)
