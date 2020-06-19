from abc import ABCMeta, abstractmethod
from Monster import Monster


class IWeapon(metaclass=ABCMeta):
    @abstractmethod
    def attackMonster(self, monster):
        pass



class WoodWeapon(IWeapon):
    def attackMonster(self, monster):
        monster.handle(20)


class IronWeapon(IWeapon):
    def attackMonster(self, monster):
        # 怪兽掉血的处理handle
        monster.handle(50)


class MagicWeapon(IWeapon):
    def attackMonster(self, monster):
        # 怪兽掉血的处理handle
        monster.handle(100)
