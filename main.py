from charactor import *
from event import *
from monster import *
from script import *

# 전역변수 정의
stage = 0
turn = 3
user = User()
mob = Slime(stage)
mob2 = Skeleton(stage)
mob3 = Zombie(stage)
item = Item()
inventory = Inventory()
# 게임 인트로
intro()

# 난이도 선택 > 쉬움 몹1, 보통 몹2, 어려움 몹3
difficulty = select_difficulty()

# 게임 소개
job_table(user.job_dict)

# 유저 정보 받기
user.input_id()
user_charactor = user.job_select()

# 정보 확인
user_charactor.show_status()
mob.show_status()
mob2.show_status()
mob3.show_status()

# 몬스터 조우

# 행동 정하기
# 공격시


# 난이도 따라서 몬스터 출현 개채 정하고
# 공격 시 어떤 몬스터를 칠것인가
# 유저테이블 몬스터 테이블 따로

def select_action(difficulty, *args):
    while True:
        print('공격 : 1, 스킬 : 2')
        action = input('무엇을 하시겠습니까? : ')
        if action in [1, 2]:
            break
        else:
            typing('1,2 중에 하나를 골라주세요')
    for arg in args:
        pass
    return action


# 공격
ui_main(user_charactor.attack(mob))
ui_main(mob.attack(user_charactor))
ui_main(mob2.attack(user_charactor))
ui_main(mob3.attack(user_charactor))
# 직업 스킬 테스트
ui_main(user_charactor.warrior_skil_1(mob))
ui_main(user_charactor.wizard_skil_1())
ui_main(user_charactor.thief_skil_1())
ui_main(user_charactor.archer_skil_1(mob))

# 몬스터 스킬
ui_main(mob.attack(user_charactor))
ui_main(mob2.bone_magic(user_charactor))
ui_main(mob3.recovery(turn))
# 아이템 드랍
drop_random = random.randint(1, 100)
if drop_random < 10:
    drop_item(user_charactor)

# ui 테이블 첫 파라메터는 turn 그 이후는 유저와 몹들
ui(turn, user_charactor, mob, mob2, mob3)

# 스테이지 클리어 이벤트
stage_clear(stage,user_charactor)

# 다음 층으로
next_floor()
