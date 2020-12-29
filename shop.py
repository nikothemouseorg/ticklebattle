from coms import *

# Открываем файлы сохранения
v1 = open(r'src/saves vamp.txt', 'r+')
f1 = open(r'src/saves ph.txt', 'r+')
i1 = open(r'src/saves istr.txt', 'r+')
o1 = open(r'src/saves oruzh.txt', 'r+')
d1 = open(r'src/saves dr.txt', 'r+')
a1 = open(r'src/saves alb.txt', 'r+')
b1 = open(r'src/saves bull.txt', 'r+')
me1 = open(r'src/saves megal.txt', 'r+')
mn1 = open(r'src/saves mnzhk.txt', 'r+')
u1 = open(r'src/saves uv.txt', 'r+')
md1 = open(r'src/saves minder.txt', 'r+')
j1 = open(r'src/saves jelly.txt', 'r+')
y1 = open(r'src/yaIiya-techs', 'r+')

gold = open(r'src/golds.txt', 'r+')

# Читаем файлы имения тех или иных техник
g = gold.readline()
g = int(g)
v = v1.read(1)
f = f1.read(1)
i = i1.read(1)
o = o1.read(1)
d = d1.read(1)
a = a1.read(1)
b = b1.read(1)
me = me1.read(1)
mn = mn1.read(1)
u = u1.read(1)
md = md1.read(1)
j = j1.read(1)
y = y1.read(1)

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
	if y == '0':
		print('13. YaIiya')
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
			elif buynum == 13 and y = '1':
				print('Ты уже купил меня.')
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
		print('Проффесиональная техника направленная на уничтожениия соперников с медлительной техникой. Мало здоровья, большой урон.')
		w()
		sp()
		print('Скорость х./т. :')
		print('2.')
		w()
		sp()
		print('Урон от коронного приёма и особый эффект:')
		print('Укус вампира - 9 (при попдании восстанавливает 5 здоровья).')
		w()
		sp()
		print('Урон от обычного приёма:')
		print('Кровавая шпага - 7.')
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
		print('Огненный ветер - 20.')
		w()
		sp()
		print('Урон от обычного приёма:')
		print('Языки пламени - 15.')
		w()
		sp()
		print('Здоровье:')
		print('150.')
		w()
		sp()
		print('Стоимость:')
		print('650 щерублей.')
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

	if techname == 3:
		print('Вы выбрали технику Истребителя')
		w()
		sp()
		print('Описание:')
		print('Очень рисковая техника! Очень-очень мало здоровья, и очень-очень много урона! Не покупай! Эта техника ужасна!.')
		w()
		sp()
		print('Скорость х./т. :')
		print('2.')
		w()
		sp()
		print('Урон от коронного приёма и особый эффект:')
		print('Раеактивная ракета - 25 (при тройном комбо шанс 50%, что нанесёт доп. 25 урона).')
		w()
		sp()
		print('Урон от обычного приёма:')
		print('Пулемётная очередь - 20.')
		w()
		sp()
		print('Здоровье:')
		print('35 (ха-ха-ха!).')
		w()
		sp()
		print('Стоимость:')
		print('0 щерублей.')
		w()
		sp()
		if g >= -1:
			buying = input('Берём? Тогда нажми B. Нет? Жми что угодно (не бери): ')
			if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в':
				print('Что ты наделал! Ведь теперь вы владеете самой плохой техникой Истребителя!')
				goldistrebitel = g - 0
				goldistrebitel = str(goldistrebitel)
				gold = open(r'src/golds.txt', 'r+')
				gold.seek(0)
				gold.close()
				gold = open(r'src/golds.txt', 'r+')
				gold.write(goldistrebitel)
				i1.seek(0)
				i = v1.write('1')
				shop()
			else:
				w()
				w()
				w()
				w()
				sp()
				print('МОЛОДЕЦ!!! :D')
				w()
				shop()
		else:
			print('Всм? У тебя отрицательный счёт?! Непон...')
	elif techname == 4:
		print('Вы выбрали технику Оружейника')
		w()
		sp()
		print('Описание:')
		print('Универсльнейшая из универсальнейших! Универсальней некуда!')
		w()
		sp()
		print('Скорость х./т.:')
		print('1')
		w()
		sp()
		print('Урон от коронного приёма:')
		print('Нейтронная бомба - 30 (замораживает владельца техники на 2 такта).')
		w()
		sp()
		print('Урон от обычного приёма:')
		print('СВД - 15.')
		w()
		sp()
		print('Урон от ещё одного обычного приёма:')
		print('Пистолет - 10.')
		w()
		sp()
		print('Урон от ещё одного обычного приёма:')
		print('Автомат - 17.')
		w()
		sp()
		print('Здоровье:')
		print('150.')
		w()
		sp()
		print('Стоимость:')
		print('600 щерублей.')
		w()
		sp()
		if g >= 600:
			buying = input('Берём? Тогда нажми B. Нет? Жми что угодно: ')
			if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в' and g >= 600:
				print('Здорово, ведь теперь вы владеете техникой Оружейника!')
				goldgunshop = g - 600
				goldgunshop = str(goldgunshop)
				gold = open(r'src/golds.txt', 'r+')
				gold.seek(0)
				gold.close()
				gold = open(r'src/golds.txt', 'r+')
				gold.write(goldgunshop)
				o1.seek(0)
				o = f1.write('1')
			else:
				shop()
		else:
			print('У вас недостаточно щерублей для покупки :(')
			shop()

def ars():
	sp()
	print('У вас есть:')
	w()
	sp()
	if v == '1':
		print('Вампир')
	if f == '1':
		print('Феникс')
	if i == '1':
		print('Истребитель')
	if o == '1':
		print('Оружейник')
	if d == '1':
		print('Дракон')
	if a == '1':
		print('Альбатрос')
	if b == '1':
		print('Бык')
	if u == '1':
		print('Увалютор')
	if me == '1':
		print('Мегалодон')
	if mn == '1':
		print('МНЖК-1')
	if md == '1':
		print('Майндер')
	if j == '1':
		print('Желе')
	if au == '1':
		print('Aмулет удачи')
	if lit == '1':
		print('[Литералы]')
	w()
	w()
	w()
	w()
	sp()
	lobby()
