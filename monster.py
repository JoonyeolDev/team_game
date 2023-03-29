import random


class Monster(BaseCharactor):
    def __init__(self, name, lv, hp, mp, power, magic_power, avoid):
        super().__init__(name, lv, hp, mp, power, magic_power, avoid)




# monster_dict = {
#         '1': Monster(name='Slime', 
#                 lv=1, 
#                 hp= 100, 
#                 max_hp=100, 
#                 max_mp=0, 
#                 mp=0, 
#                 power=5, 
#                 magic_power=0, 
#                 avoid=10),
    
#         '2': Monster(name = 'Skeleton',
#                 lv = 2,
#                 hp = 120,
#                 max_hp = 120,
#                 max_mp = 5,
#                 mp = 0,
#                 power = 15,
#                 magic_power = 20,
#                 avoid = 10),

        
#         '3': Monster(name = 'Zombie',
#                 lv = 3,
#                 hp = random.randrange(self.max_hp+1),
#                 max_hp = 200,
#                 max_mp = 4,
#                 mp = 0,
#                 power = random.randint(10, 15),
#                 magic_power = 0,
#                 avoid = 10,
# }








class Slime(Monster):
    def __init__(self):
        self.name = 'Slime'
        self.lv = lv
        self.max_hp = 100
        self.hp = 100
        self.max_mp = 0
        self.mp = 0
        self.power = 5
        self.magic_power = 0
        self.avoid = 10 + lv*5



class Skeleton(Monster):

    def __init__(self):
        self.name = 'Skeleton'
        self.lv = lv
        self.hp = 120
        self.max_hp = 120
        self.max_mp = 5
        self.mp = 0
        self.power = 15 + lv*3
        self.magic_power = 20
        self.avoid = 10

    def bone_magic(self, other):
        self.mana -= self.max_mana
        damage = random.randint(self.power+3, self.magic_power+self.power)
        other.hp = max(other.hp - damage, 0)
        print(
            f'마나 {self.max_mana}을 소모합니다.\n'
            f"{self.name}의 뼈 마법!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
            f'{other.name}의 현재 HP:{other.hp}')
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def skeleton_attack(self):
        # 마나 체크 후 공격 타입 지정
        if self.mana == self.max_mana:
            monster.attack_type = 3
        else:
            monster.attack_type = random.randint(1, 2)
        if monster.attack_type == 1:
            monster.attack(User)
        elif monster.attack_type == 2:
            monster.power_attack(User)
        elif monster.attack_type == 3:
            monster.bone_magic(User)


class Zombie(Monster):

    def __init__(self):
        self.name = 'Zombie'
        self.lv = lv
        self.hp = random.randrange(self.max_hp+1)
        self.max_hp = 200 + lv*10
        self.max_mp = 4
        self.mp = 0
        self.power = random.randint(10, 15)
        self.magic_power = 0
        self.avoid = 10

    def recovery(self):
        self.mana -= self.max_mana
        # 턴 수 * 2로 회복 
        recovery = round*2
        self.hp += recovery
        if self.max_hp < self.hp:
            self.hp = self.max_hp
        print(
            f'마나 {self.max_mana}을 소모합니다.\n'
            f'{self.name}의 회복! {self.name}이(가) {recovery}만큼 회복하였습니다.\n'
            f'{self.name}의 현재 HP:{self.hp}')

    def zombie_attack(self):
        # 마나 체크 후 공격 타입 지정
        if self.mana == self.max_mana:
            monster.attack_type = 3
        else:
            monster.attack_type = random.randint(1, 2)
        if monster.attack_type == 1:
            monster.attack(User)
        elif monster.attack_type == 2:
            monster.power_attack(User)
        elif monster.attack_type == 3:
            monster.recovery()


# monster_list = [Slime(), Skeleton(), Zombie()]
# # 랜덤 몬스터 생성
# monster = random.choice(monster_list)