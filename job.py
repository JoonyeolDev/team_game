from main import User
import random
# 직업
# 직업 스킬


class Job():
    def __init__(self, job=None):
        #     self.name = name
        self.job = job


    job_dict = {
        '1': {
            'job': '전사',
            'hp': 300,
            'mp': 200,
            'power': 20,
            'magic_power': 10,
            'avoid': 10
        },
        '2': {
            'job': '마법사',
            'hp': 100,
            'mp': 200,
            'power': 10,
            'magic_power': 30,
            'avoid': 10
        },
        '3': {
            'job': '궁수',
            'hp': 150,
            'mp': 100,
            'power': 15,
            'magic_power': 20,
            'avoid': 10
        },
        '4': {
            'job': '도적',
            'hp': 150,
            'mp': 100,
            'power': 20,
            'magic_power': 15,
            'avoid': 40
        },
    }

    def job_select(self, name):
        while True:
            print('전사:1 마법사:2 궁수:3 도적:4')
            self.job = input('직업을 선택해주세요 : ')
            if self.job in self.job_dict.keys():
                # user = Job.job_dict[job_select]
                user = User(
                    name,
                    1,
                    self.job_dict[self.job]['job'],
                    self.job_dict[self.job]['hp'],
                    self.job_dict[self.job]['mp'],
                    self.job_dict[self.job]['power'],
                    self.job_dict[self.job]['magic_power'],
                    self.job_dict[self.job]['avoid']
                )
                break
            else:
                print('올바른 입력 값 X')
                continue
        return user


# class Warrior:
#     def warrior_skil_1(self, other):
#         mana_consum = 5
#         if self.mana < mana_consum:
#             print('마나가 모자랍니다')
#         else:
#             self.mana -= mana_consum
#             damage = random.randint(self.magic_power, self.magic_power + 5)
#             other.hp = max(other.hp - damage, 0)
#             print(
#                 f'마나 {mana_consum}을 소모합니다.\n'
#                 f"{self.name}의 마법 공격!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
#                 f'{other.name}의 현재 HP:{other.hp}')
#             if other.hp == 0:
#                 print(f"{other.name}이(가) 쓰러졌습니다.")


# class Wizrad:
#     def thief_skil_1(self, other):
#         mana_consum = 5
#         if self.mana < mana_consum:
#             print('마나가 모자랍니다')
#         else:
#             self.mana -= mana_consum
#             damage = random.randint(self.magic_power, self.magic_power + 5)
#             other.hp = max(other.hp - damage, 0)
#             print(
#                 f'마나 {mana_consum}을 소모합니다.\n'
#                 f"{self.name}의 마법 공격!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
#                 f'{other.name}의 현재 HP:{other.hp}')
#             if other.hp == 0:
#                 print(f"{other.name}이(가) 쓰러졌습니다.")


# class Thief:
#     def thief_skil_1(self, other):
#         mana_consum = 5
#         if self.mana < mana_consum:
#             print('마나가 모자랍니다')
#         else:
#             self.mana -= mana_consum
#             damage = random.randint(self.magic_power, self.magic_power + 5)
#             other.hp = max(other.hp - damage, 0)
#             print(
#                 f'마나 {mana_consum}을 소모합니다.\n'
#                 f"{self.name}의 마법 공격!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
#                 f'{other.name}의 현재 HP:{other.hp}')
#             if other.hp == 0:
#                 print(f"{other.name}이(가) 쓰러졌습니다.")


# class Archer:
#     def archer_skil_1(self, other):
#         mana_consum = 5
#         if self.mana < mana_consum:
#             print('마나가 모자랍니다')
#         else:
#             self.mana -= mana_consum
#             damage = random.randint(self.magic_power, self.magic_power + 5)
#             other.hp = max(other.hp - damage, 0)
#             print(
#                 f'마나 {mana_consum}을 소모합니다.\n'
#                 f"{self.name}의 마법 공격!  {other.name}에게 {damage}의 데미지를 입혔습니다.\n"
#                 f'{other.name}의 현재 HP:{other.hp}')
#             if other.hp == 0:
#                 print(f"{other.name}이(가) 쓰러졌습니다.")
