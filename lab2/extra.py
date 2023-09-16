import os
import time


def esc(code):
    return f'\u001b[{code}m'


def clear_console():
    os.system("cls")


def flag_fr():
    for i in range(6):
        print(f'{BLUE}{"  " * 4}{WHITE}{"  " * 4}{RED}{"  " * 4}{END}')

def flag_ru():
    print(f'{WHITE}{"  " * 12}{END}')
    print(f'{WHITE}{"  " * 12}{END}')
    print(f'{BLUE}{"  " * 12}{END}')
    print(f'{BLUE}{"  " * 12}{END}')
    print(f'{RED}{"  " * 12}{END}')
    print(f'{RED}{"  " * 12}{END}')

def flag_nd():
    print(f'{RED}{"  " * 12}{END}')
    print(f'{RED}{"  " * 12}{END}')
    print(f'{WHITE}{"  " * 12}{END}')
    print(f'{WHITE}{"  " * 12}{END}')
    print(f'{BLUE}{"  " * 12}{END}')
    print(f'{BLUE}{"  " * 12}{END}')


RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
BLACK = esc(40)
END = esc(0)

frames = [flag_fr, flag_nd, flag_ru]

print("\nАнимация 'Три флага': ")
time.sleep(1)
for frame in frames:
    clear_console()
    frame()
    time.sleep(2)