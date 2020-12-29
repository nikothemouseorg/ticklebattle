from commands import *
from Main import *


# Покупка товара
def purchace(techname):
    sp()
    # Вампир
    if techname == 1:
        print('Вы выбрали технику Вампира')
        w()
        sp()
        print('Описание:')
        print(
            'Проффесиональная техника направленная на уничтожениия соперников с медлительной техникой. Мало здоровья, большой урон.')
        w()
        sp()
        print('Скорость х./т. :')
        print('2.')
        w()
        sp()
        print('Урон от коронного приёма и особый эффект:')
        print('9  (при попдании восстанавливает 5 здоровья).')
        w()
        sp()
        print('Урон от обычного приёма:')
        print('7.')
        w()
        sp()
        print('Здоровье:')
        print('100.')
        w()
        sp()
        print('Стоимость:')
        print('650 щерублей.')
        w()
        sp()
        if g >= 650:
            buying = input('Берём? Тогда нажми B. Нет? Жми что угодно: ')
            if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в' and g >= 650:
                print('Здорово, ведь теперь вы владеете техникой Вампира!')
                goldvampire = g - 650
                goldvampire = str(goldvampire)
                gold = open(r'src/golds.txt', 'r+')
                gold.seek(0)
                gold.close()
                gold = open(r'src/golds.txt', 'r+')
                gold.write(goldvampire)
                v1.seek(0)
                v = v1.write('1')
            else:
                shop()
        else:
            print('У вас недостаточно щерублей для покупки :(')

    elif techname == 2:
        print('Вы выбрали технику Феникса')
        w()
        sp()
        print('Описание:')
        print('Очень большые здоровье и урон. Всё портит лишь то, что он ходит 1 раз в 2 такта. Так-то!')
        w()
        sp()
        print('Скорость х./т.:')
        print('0.5')
        w()
        sp()
        print('Урон от коронного приёма:')
        print('25')
        w()
        sp()
        print('Урон от обычного приёма:')
        print('15')
        w()
        sp()
        print('Здоровье:')
        print('190')
        w()
        sp()
        print('Стоимость:')
        print('650 щерублей')
        w()
        sp()
        if g >= 650:
            buying = input('Берём? Тогда нажми B. Нет? Жми что угодно: ')
            if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в' and g >= 650:
                print('Здорово, ведь теперь вы владеете техникой Феникса!')
                goldpheonix = g - 650
                goldpheonix = str(goldpheonix)
                gold = open(r'src/golds.txt', 'r+')
                gold.seek(0)
                gold.close()
                gold = open(r'src/golds.txt', 'r+')
                gold.write(goldpheonix)
                f1.seek(0)
                p = f1.write('1')
            else:
                shop()
        else:
            print('У вас недостаточно щерублей для покупки :(')
            shop()


    elif techname == 3:
        print('Вы выбрали технику Истребителя')
        w()
        sp()
        print('Описание:')
        print('По названию видно, что эта техника - для истребления. Большие скорость и урон. "А не слишком ли читерная эта техника?" - Создатель')
        w()
        sp()
        print('Скорость х./т.:')
        print('3.25')
        w()
        sp()
        print('Урон от коронного приёма:')
        print('32')
        w()
        sp()
        print('Урон от обычного приёма:')
        print('17')
        w()
        sp()
        print('Здоровье:')
        print('220')
        w()
        sp()
        print('Стоимость:')
        print('800 щерублей')
        w()
        sp()
        if g >= 800:
            buying = input('Берём? Тогда нажми B. Нет? Жми что угодно: ')
            if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в' and g >= 650:
                print('Здорово, ведь теперь вы владеете техникой Истребителя!')
                goldfight = g - 800
                goldfight = str(goldfight)
                gold = open(r'src/golds.txt', 'r+')
                gold.seek(0)
                gold.close()
                gold = open(r'src/golds.txt', 'r+')
                gold.write(goldfight)
                i1.seek(0)
                i = i1.write('1')
            else:
                shop()
        else:
            print('У вас недостаточно щерублей для покупки :(')
            shop()
