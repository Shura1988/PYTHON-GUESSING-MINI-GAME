from random import *

print('Доборо пожаловать в игру "УГАДАЙКА"!')
print('Задайте левую границу диапазона: ')
start = input()
while not start.isdigit():
    print(f'А может быть все-таки введем целое число?')
    start = input()
start = int(start)
print('Задайте левую границу диапазона: ')
end = input()
while not end.isdigit():
    print(f'А может быть все-таки введем целое число?')
    end = input()
end = int(end)
while start >= end:
    print(f'Правая граница добжна быть тольше левой!! Введите целое число больше {start}')
    end = input()
    while not end.isdigit():
        print(f'А может быть все-таки введем целое число?')
        end = input()
    end = int(end)

new_game = 'да'
num = randint(start, end)


def is_valid(n):
    if n.isdigit() and start <= int(n) <= end:
        return True
    else:
        return False

print(f'Введите число от {start} до {end}:\n')
count = 0
while True:
    n = input()
    if is_valid(n) == True:
        n = int(n)
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
        else:
            print('Вы угадали, поздравляем!')
            print(f"Спасибо, что играли в числовую угадайку. Еще увидимся...")
            count += 1
            break
    else:
        print(f'А может быть все-таки введем целое число от {start} до {end}?')
        count += 1
print(f'Количество ваших попыток = {count}')
