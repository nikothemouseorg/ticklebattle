from commands import *
from Main import *
    # Магазин
def shop():
	sp()
	print('Добро пожловать в магазин техник!')
	w()
	w()
	print('Здесь вы можете прикупить себе новенькую технику или артефакты.')
	w()
	sp()
	print('На витрине стоят:')
	w()
	w()
	sp()
	if v == '0':
		print('1. Вампир')
		w()
	if f == '0':
		print('2. Феникс')
		w()
	if i == '0':
		print('3. Истребитель')
		w()
	if o == '0':
		print('4. Оружейник')
		w()
	if d == '0':
		print('5. Дракон')
		w()
	if a == '0':
		print('6. Альбатрос')
		w()
	if b == '0':
		print('7. Бык')
		w()
	if me == '0':
		print('8. Увалютор')
		w()
	if mn == '0':
		print('9. Мегалодон')
		w()
	if md == '0':
		print('10. МНЖК-1')
		w()
	if j == '0':
		print('11. Майндер')
		w()
	if u == '0':
		print('12. Желе')
		w()
# Выбор понравившейся техники или понравившегося артефакта
	while True:
		buynum = int(input('Введите номер понравившейся вам вещи (без точки), или E чтобы уйти домой, в лобби: '))
		if buynum == 'e' or buynum == 'E' or buynum == 'е' or buynum == 'Е':
			lobby()
		if buynum == 1 or buynum == 2 or buynum == 3 or buynum == 4 or buynum == 5 or buynum == 6 or buynum == 7 or buynum == 8 or buynum == 9 or buynum == 10 or buynum == 12 or buynum == 13 or buynum == 14:
			if buynum == 1 and v == '1':
				print('Неправильный символ!')
			elif buynum == 2 and f == '1':
				print('Неправильный символ!')
			elif buynum == 3 and i == '1':
				print('Неправильный символ!')
			elif buynum == 4 and o == '1':
				print('Неправильный символ!')
			elif buynum == 5 and d == '1':
				print('Неправильный символ!')
			elif buynum == 6 and a == '1':
				print('Неправильный символ!')
			elif buynum == 7 and b == '1':
				print('Неправильный символ!')
			elif buynum == 8 and u == '1':
				print('Неправильный символ!')
			elif buynum == 9 and me == '1':
				print('Неправильный символ!')
			elif buynum == 10 and mn == '1':
				print('Неправильный символ!')
			elif buynum == 11 and md == '1':
				print('Неправильный символ!')
			elif buynum == 12 and j == '1':
				print('Неправильный символ!')
			if buynum == 1 and v == '0':
				purchace(buynum)
				break
			elif buynum == 2 and f == '0':
				purchace(buynum)
				break
			elif buynum == 3 and i == '0':
				purchace(buynum)
				break
			elif buynum == 4 and o == '0':
				purchace(buynum)
				break
			elif buynum == 5 and d == '0':
				purchace(buynum)
				break
			elif buynum == 6 and a == '0':
				purchace(buynum)
				break
			elif buynum == 7 and b == '0':
				purchace(buynum)
				break
			elif buynum == 8 and me == '0':
				purchace(buynum)
				break
			elif buynum == 9 and mn == '0':
				purchace(buynum)
				break
			elif buynum == 10 and md == '0':
				purchace(buynum)
				break
			elif buynum == 11 and j == '0':
				purchace(buynum)
				break
			elif buynum == 12 and u == '0':
				purchace(buynum)
				break
		else:
			print('Неправильный символ!')
			return buynum


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
