from sphinx import call_sphinx
from magician import call_magician
import random
from main import BaseCharactor

# 스테이지가 넘어갈 때 stage_clear 함수를 호출
# 받아와야 할 것, 몇 스테이지?, 유저 상태


# 음... 아예 메인에서 아이템 클래스를 생성하고 가져오는게 나은가?
class Item(BaseCharactor):
    def __init__(self, name, lv, hp, mp, power, magic_power, avoid):
        super().__init__(name, lv, hp, mp, power, magic_power, avoid)

# 얘는 물약 보관소


class Inventory(BaseCharactor):
    def __init__(self, name, lv, hp, mp, power, magic_power, avoid):
        super().__init__(name, lv, hp, mp, power, magic_power, avoid)


# 아이템 할거면 유저가 아이템도 들어야 함 ㅠㅠㅠㅠㅠㅠㅠㅠㅠ
# 1.인벤토리에서 언제든 꺼내 먹게 설정할 건지?
# 2.아니면 바로 적용하게 유저정보를 수정할 건지

# -----스크립트로------
# if monster.hp <= 0:
# 아이템 드롭 안할거면 밑에는 삭제
# ((
# item_random = random.randint(1, 100)
#   if item_random < 확률:
#       drop_item(???)
# ))
# stage_clear(round, user)
# ----------------------


# 아이템을 직업별로 사용불가 기능을 넣을 것인가....음....
def drop_item():
    item_sort = ['1', '2', '3', '4']
    choose_item = random.choices(item_sort)
    item_choosen = item_list[choose_item]

item_list = {
    '1': Item('wand', None, None, random.randint(1, 3), None, random.randint(3, 5), None),
    '2': Item('greatsword', None, random.randint(1, 3), None, random.randint(3, 5), None, None),
    '3': Item('knife', None, None, None, random.randint(1, 3), None, random.randint(3, 5)),
    '4': Item('bow', None, random.randint(3, 5), None, None, None, random.randint(1, 3)),
}

# 아이템의 user 변수와 user의 직업 정보가 일치하지 않으면 아이템을 꺼낼 수 없다?
# class Item(BaseCharactor):
#     item_sort = {}


# (name, lv, hp, mp, power, magic_power, avoid)

shopping_list = {
    '1': Inventory('hp potion', None, 10, None, None, None, None),
    '2': Inventory('mp potion', None, None, 5, None, None, None),
    '3': Inventory('용의 비늘(power +5)', None, None, None, 10, None, None),
    '4': Inventory('magic_power up', None, None, None, None, 10, None),
}


# 상점
def call_shop():
    buy = input('1.hp potion, 2.mp potion, 3.용의 비늘(power +5), 4.magic_power up')
    item_shop = shopping_list[buy]
    print(item_shop)
    move = input('1.상점 호출, 2.스테이지 호출')

    if move == 1:
        return call_shop()
    elif move == 2:
        return


def stage_clear(stage, user):

    call_shop()

    if stage == 5:
        call_sphinx()
        # print(f'스핑크스 호출')

    elif stage == 10:
        call_magician()
        # print(f'매지션 호출')

    else:
        # 일정 확률로 만나는 스테이지
        gacha = random.randint(1, 100)
        status_gocha = random.randint(5, 10)

        #이거 몰라!!!!! 안들어가 ㅠㅠ
        minus_status = random.choices([hp, mp, power, magic_power])

        if gacha <= 10:
            print(f'trap 발생')
            user.minus_status -= status_gocha
            # 하나? 두개?

        elif gacha <= 35:
            print(f'healing spot 발생')
            user.hp = user.max_hp*status_gocha
            user.mp = user.max_mp*status_gocha

            # 모든 이벤트 발생이 아니라고 판단하면 레벨업 함수로 넘어가게 한다.
            # 렙업 함수에서 특별히 할게 없으면 걍 return으로 나가기
            # else:
            # level_up()

    return

    # 돌아가는 함수
    # home()


# stage_clear(10, 'user')
