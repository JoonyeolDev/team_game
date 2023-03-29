from charactor import *
import random


class Monster(BaseCharactor):
    def __init__(self, name, lv, hp, mp, power, magic_power, avoid):
        super().__init__(name, lv, hp, mp, power, magic_power, avoid)


class Slime(Monster):
    def __init__(self,lv):
        self.name = 'Slime'
        self.lv = lv
        self.max_hp = 100
        self.hp = self.max_hp
        self.max_mp = 0
        self.mp = self.max_mp
        self.power = 5
        self.magic_power = 0
        self.avoid = 10 + lv*5

class Skeleton(Monster):
    def __init__(self,lv):
        self.name = 'Skeleton'
        self.lv = lv
        self.max_hp = 120
        self.hp = self.max_hp
        self.max_mp = 5
        self.mp = self.max_mp
        self.power = 15 + lv*3
        self.magic_power = 20
        self.avoid = 10
        self.attack_type = 3

    def bone_magic(self, other):
        self.mp -= self.mp
        damage = random.randint(self.power+3, self.magic_power+self.power)
        other.hp = max(other.hp - damage, 0)
        text = [f'''마나 {self.max_mp}을 소모합니다.
        {self.name}의 뼈 마법!  {other.name}에게 {damage}의 데미지를 입혔습니다.
        {other.name}의 현재 HP:{other.hp}''']
        if other.hp == 0:
            text = f"{other.name}이(가) 쓰러졌습니다."
        return text

    def skeleton_attack(self,other):
        # 마나 체크 후 공격 타입 지정
        if self.mp == self.max_mp:
            self.attack_type = 3
        else:
            self.attack_type = random.randint(1, 2)
        if self.attack_type == 1:
            self.attack(other)
        elif self.attack_type == 2:
            self.power_attack(other)
        else:
            self.bone_magic(other)


class Zombie(Monster):
    def __init__(self,lv):
        self.name = 'Zombie'
        self.lv = lv
        self.max_hp = 200 + lv*10
        self.hp = random.randrange(self.max_hp+1)
        self.max_mp = 4
        self.mp = self.max_mp
        self.power = random.randint(10, 15)
        self.magic_power = 0
        self.avoid = 10
        self.attack_type = 3

    def recovery(self,turn):
        self.mp -= self.max_mp
        # 턴 수 * 2로 회복 
        recovery = turn*2
        self.hp += recovery
        if self.max_hp < self.hp:
            self.hp = self.max_hp
        text = [f'''마나 {self.max_mp}을 소모합니다.
        {self.name}의 회복! {self.name}이(가) {recovery}만큼 회복하였습니다.
        {self.name}의 현재 HP:{self.hp}''']
        return text

    def zombie_attack(self,other):
        # 마나 체크 후 공격 타입 지정
        if self.mp == self.max_mp:
            self.attack_type = 3
        else:
            self.attack_type = random.randint(1, 2)
        if self.attack_type == 1:
            self.attack(other)
        elif self.attack_type == 2:
            self.power_attack(other)
        else:
            self.recovery()

# monster_list = [Slime(), Skeleton(), Zombie()]
# # 랜덤 몬스터 생성
# monster = random.choice(monster_list)



