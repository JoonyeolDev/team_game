from charactor import *
from event import *
from monster import *
from script import *

# 전역변수 정의
stage = 0
turn = 3
user = User()
mob = Slime(1)
mob2 = Skeleton(1)
mob3 = Zombie(1)
item = Item()
inventory = Inventory()
# 게임 인트로
#intro()

# 난이도 선택 > 쉬움 몹1, 보통 몹2, 어려움 몹3
# 
# 게임 소개 
# job_table(user.job_dict)

# 유저 정보 받기
user.input_id()
user_charactor = user.job_select()

# 정보 확인
# user_charactor.show_status()
# mob.show_status()
# mob2.show_status()
# mob3.show_status()

# 공격 확인
# ui_main(user_charactor.attack(mob))
# ui_main(mob.attack(user_charactor))
# ui_main(mob2.attack(user_charactor))
# ui_main(mob3.attack(user_charactor))

# 몬스터 스킬확인
# ui_main(mob.attack(user_charactor))
# ui_main(mob2.bone_magic(user_charactor))
# ui_main(mob3.recovery(turn))

# 아이템 드랍
# drop_item()

# ui 테이블 첫 파라메터는 turn 그 이후는 유저와 몹들
# ui(turn, user_charactor, mob, mob2, mob3)

# 스테이지 클리어 이벤트
# stage_clear(stage,user_charactor)

# 다음 층으로
# next_floor()