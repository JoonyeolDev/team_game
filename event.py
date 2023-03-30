from charactor import *
from sphinx import call_sphinx
from magician import call_magician
import random


#아이템 드롭
def drop_item(user):
    choose_item = random.randint(1, 4)
    event_item = item_list[choose_item]
    if choose_item == '1':
        user.mp += event_item.mp
        user.magic_power += event_item.magic_power
    elif choose_item == '2':
        user.hp += event_item.hp
        user.power += event_item.power
    elif choose_item == '3':
        user.power += event_item.power
        user.avoid += event_item.avoid
    else:
        user.hp += event_item.hp
        user.avoid += event_item.avoid
    print(f'{event_item.name}을 획득했습니다')
    print(f'hp:+{event_item.hp}/mp:+{event_item.mp}/power:+{event_item.power}/magic power:+{event_item.magic_power}/avoid:+{event_item.avoid}을 획득했습니다')
    return


# 상점
def call_shop(user):
    
    print('1.hp potion(hp +10), 2.mp potion(mp +5), 3.용의 비늘(power +10), 4.magic_power up(magic power +10)')
    print(f'1.{shopping_list[1].gold}G, 2.{shopping_list[2].gold}G, 3.{shopping_list[3].gold}G, 4.{shopping_list[4].gold}G')
    while True:
        buy = input('구매하실 아이템을 선택해주세요 : ')
        if buy in ['1','2','3','4']: break
        else : print('1,2,3,4 중 하나를 입력해주세요')
    item_shop = shopping_list[int(buy)]
    if buy == '1':
        print(f'hp:{user.hp}')
        user.hp += item_shop.hp
        user.gold -= item_shop.gold
        print(f'hp:{user.hp}')
    elif buy == '2':
        print(f'mp:{user.mp}')
        user.mp += item_shop.mp
        user.gold -= item_shop.gold
        print(f'mp:{user.mp}')
    elif buy == '3':
        print(f'power:{user.power}')
        user.power += item_shop.power
        user.gold -= item_shop.gold
        print(f'power:{user.power}')
    else:
        print(f'magic_power:{user.magic_power}')
        user.magic_power += item_shop.magic_power
        user.gold -= item_shop.gold
        print(f'magic_power:{user.magic_power}')
    print(f'{item_shop.name}을 구매하셨습니다.')
    print(f'{user.gold} gold가 남았습니다.')
    move = input('1.상점 호출, 2.스테이지 호출')
    if move == '1':
        return call_shop(user)
    elif move == '2':
        return


#스테이지 클리어 후
def stage_clear(stage, user):

    call_shop(user)

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

        minus_status = random.choice([user.hp, user.mp, user.power, user.magic_power])
        
        #일단 체력만 감소하는걸로
        if gacha <= 10:
            print(f'함정에 걸렸다! 체력이 {status_gocha} 만큼 감소합니다')
            minus_status -= status_gocha

        elif gacha <= 35:
            print(f'치유의 샘 발견 !! 체력과 마나가 최대치의 {status_gocha}%만큼 회복됩니다')
            user.hp += user.max_hp*status_gocha
            if user.hp>user.max_hp: user.hp = user.max_hp
            user.mp += user.max_mp*status_gocha
            if user.mp>user.max_mp: user.mp = user.max_mp

        else: pass
    return

    # 돌아가는 함수
    # next_floor()
