import time, os
from rich.console import Console
from rich.table import Table
from rich import print
from charactor import *
# 인트로
def intro():
    print("-"*53)
    typing("안녕하세요, 무지성 탑에 어서오세요 !")
    time.sleep(1)

def select_difficulty():
    typing('난이도에 따라 몬스터의 수가 바뀝니다')
    typing('쉬움 : 1, 보통 : 2, 어려움 : 3')
    while True:
        difficulty = input('난이도를 선택해주세요(1,2,3) : ')
        if difficulty in ['1','2','3']:
            break
        else: typing('1,2,3 중에 하나를 골라주세요')
    return difficulty


def job_table(job_dict):
    console = Console()
    table = Table(show_header=True)
    column_list = ['Class', 'H P', 'M P', 'Power', 'Magic', 'Avoid']
    for column in column_list:
        table.add_column(column, justify='center', width=10)
    # for row in job.Job.job_dict
    for job in job_dict:
        # table.add_row(job_dict[job])
        table.add_row(job_dict[job]["job"], 
                      str(job_dict[job]["hp"]),
                      str(job_dict[job]["mp"]), 
                      str(job_dict[job]["power"]),
                      str(job_dict[job]["magic_power"]),
                      str(job_dict[job]["avoid"]),
                      )
    return console.print(table)

# 타이핑치는 효과 str
def typing(text):
    for i in range(len(text)):
        print(text[i], end='', flush=True)
        time.sleep(0.03)
    print('')

# 타이핑치는 효과 list
def list_typing(list):
    for item in list:
        typing(item)


def ui_main(text):
    console = Console()
    table = Table(show_header=False, width=92)
    for i in text:
        table.add_row(i)
    return console.print(table)


def ui(round, *args):
    console = Console()
    table = Table(show_header=True)
    column_list = ['Turn '+str(round), 'Name', 'H P', 'M P', 'Power', 'Magic', 'Avoid']
    for i in column_list:
        table.add_column(i, justify='center', width=10)
    for arg in args:
        table.add_row(
            str(arg.lv),
            arg.name,
            str(arg.hp)+" / "+str(arg.max_hp),
            str(arg.mp)+" / "+str(arg.max_mp),
            str(arg.power),
            str(arg.magic_power),
            str(arg.avoid),
        )
    return console.print(table)



def next_floor():
    typing("당신은 조심해서 다음 층으로 향합니다")
    time.sleep(2)
    os.system('cls')
    typing("왠지 불길한 기운이 앞에 있습니다")
    time.sleep(2)
    os.system('cls')
    typing("이런 !! 몬스터를 만났습니다 !")
    typing("전투가 시작됩니다 준비해주세요 !")
    typing("3  .   .   2  .   .   1  .   .   ")
    time.sleep(1)
    os.system('cls')