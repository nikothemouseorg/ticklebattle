from time import *
from random import *

# Открываем файлы сохранения
v1 = open(r'src/saves vamp.txt', 'r+')
f1 = open(r'src/saves ph.txt', 'r+')
i1 = open(r'src/saves i.txt', 'r+')
o1 = open(r'src/saves oruzh.txt', 'r+')
d1 = open(r'src/saves dr.txt', 'r+')
a1 = open(r'src/saves alb.txt', 'r+')
b1 = open(r'src/saves bull.txt', 'r+')
me1 = open(r'src/saves megal.txt', 'r+')
mn1 = open(r'src/saves mnzhk.txt', 'r+')
u1 = open(r'src/saves uv.txt', 'r+')
md1 = open(r'src/saves minder.txt', 'r+')
j1 = open(r'src/saves jelly.txt', 'r+')
y1 = open(r'src/yaliya-techs.txt', 'r+')

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
	if u == '0':
		print('8. Увалютор')
		w()
	if me == '0':
		print('9. Мегалодон')
		w()
	if mn == '0':
		print('10. МНЖК-1')
		w()
	if md == '0':
		print('11. Майндер')
		w()
	if j == '0':
		print('12. Желе')
		w()
# Выбор понравившейся техники или понравившегося артефакта
	while True:
		buynum = input('Введите номер понравившейся вам вещи (без точки), или можете вернуться в лобби (999): ')
		if buynum == '999':
			lobby()
			break
		if buynum == '666':
			print('Ты чего удумал, сатанист???')
		if buynum == '1' or buynum == '2' or buynum == '3' or buynum == '4' or buynum == '5' or buynum == '6' or buynum == '7' or buynum == '8' or buynum == '9' or buynum == '10' or buynum == '11' or buynum == '12' or buynum == '13':
			if buynum == '1' and v == '1':
				print('Ты уже купил меня!')
			elif buynum == '2' and f == '1':
				print('Ты уже купил меня!')
			elif buynum == '3' and i == '1':
				print('Ты уже купил меня!')
			elif buynum == '4' and o == '1':
				print('Ты уже купил меня!')
			elif buynum == '5' and d == '1':
				print('Ты уже купил меня!')
			elif buynum == '6' and a == '1':
				print('Ты уже купил меня!')
			elif buynum == '7' and b == '1':
				print('Ты уже купил меня!')
			elif buynum == '8' and u == '1':
				print('Ты уже купил меня!')
			elif buynum == '9' and me == '1':
				print('Ты уже купил меня!')
			elif buynum == '10' and mn == '1':
				print('Ты уже купил меня!')
			elif buynum == '11' and md == '1':
				print('Ты уже купил меня!')
			elif buynum == '12' and j == '1':
				print('Ты уже купил меня!')
			elif buynum == '13' and y == '1':
				print('Ты уже купил Илью!')
			if buynum == '1' and v == '0':
				purchace(buynum)
				break
			elif buynum == '2' and f == '0':
				purchace(buynum)
				break
			elif buynum == '3' and i == '0':
				purchace(buynum)
				break
			elif buynum == '4' and o == '0':
				purchace(buynum)
				break
			elif buynum == '5' and d == '0':
				purchace(buynum)
				break
			elif buynum == '6' and a == '0':
				purchace(buynum)
				break
			elif buynum == '7' and b == '0':
				purchace(buynum)
				break
			elif buynum == '8' and u == '0':
				purchace(buynum)
				break
			elif buynum == '9' and me == '0':
				purchace(buynum)
				break
			elif buynum == '10' and mn == '0':
				purchace(buynum)
				break
			elif buynum == '11' and md == '0':
				purchace(buynum)
				break
			elif buynum == '12' and j == '0':
				purchace(buynum)
				break
			elif buynum == '13' and y == '0':
				purchace(buynum)
		else:
			print('Неправильный символ!')
			return buynum


# Покупка товара
-def purchace(techname):
	sp()
	# Вампир
	if techname == '1':
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
		print('Коронный приём:')
		print('Укус вампира - 15 (при попдании восстанавливает 5 здоровья).')
		w()
		sp()
		print('Обычный приём:')
		print('Кровавая шпага - 6.')
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

	elif techname == '2':
		print('Вы выбрали технику Феникса')
		w()
		sp()
		print('Описание:')
		print('Очень большые здоровье и урон. Всё портит лишь то, что он ходит 1 раз в 2 такта. Так-то!')
		w()
		sp()
		print('Скорость х./т.:')
		print('0.5.')
		w()
		sp()
		print('Коронный приём:')
		print('Огненный ветер - 20.')
		w()
		sp()
		print('Обычный приём:')
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
				f = f1.write('1')
			else:
				shop()
		else:
			print('У вас недостаточно щерублей для покупки :(')
			shop()

	if techname == '3':
		print('Вы выбрали технику Истребителя')
		w()
		sp()
		print('Описание:')
		print('Очень. Мощная. Техника.')
		w()
		sp()
		print('Скорость х./т. :')
		print('2.')
		w()
		sp()
		print('Коронный приём:')
		print('Раеактивная ракета - 25 (при тройном комбо шанс 50%, что нанесёт доп. 25 урона).')
		w()
		sp()
		print('Обычный приём:')
		print('Пулемётная очередь - 20.')
		w()
		sp()
		print('Здоровье:')
		print('190.')
		w()
		sp()
		print('Стоимость:')
		print('1500 щерублей.')
		w()
		sp()
		if g >= 1500:
			buying = input('Берём? Тогда нажми B. Нет? Жми что угодно: ')
			if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в' and g >= 1500:
				print('Теперь вы владеете очень мощной техникой Истребителя!')
				goldistrebitel = g - 1500
				goldistrebitel = str(goldistrebitel)
				gold = open(r'src/golds.txt', 'r+')
				gold.seek(0)
				gold.close()
				gold = open(r'src/golds.txt', 'r+')
				gold.write(goldistrebitel)
				i1.seek(0)
				i = i1.write('1')
			else:
				w()
				w()
				w()
				w()
				sp()
				print('А что не купил???')
				w()
				shop()
		else:
			print('Ничего! Подкопи чуть щерублей!')
	elif techname == '4':
		print('Вы выбрали технику Оружейника')
		w()
		sp()
		print('Описание:')
		print('Универсльнейшая из универсальнейших! Универсальней некуда!')
		w()
		sp()
		print('Скорость х./т.:')
		print('1.')
		w()
		sp()
		print('Коронный приём:')
		print('Нейтронная бомба - 30 (замораживает владельца техники на 2 такта).')
		w()
		sp()
		print('Обычный приём::')
		print('СВД - 15.')
		w()
		sp()
		print('Урон от ещё одного обычного приёма:')
		print('Пистолет - 10.')
		w()
		sp()
		print('Another обычный приём:')
		print('Автомат - 17.')
		w()
		sp()
		print('Здоровье:')
		print('150.')
		w()
		sp()
		print('Стоимость:')
		print('700 щерублей.')
		w()
		sp()
		if g >= 700:
			buying = input('Берём? Тогда нажми B. Нет? Жми что угодно: ')
			if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в' and g >= 700:
				print('Здорово, ведь теперь вы владеете техникой Оружейника!')
				goldgunshop = g - 700
				goldgunshop = str(goldgunshop)
				gold = open(r'src/golds.txt', 'r+')
				gold.seek(0)
				gold.close()
				gold = open(r'src/golds.txt', 'r+')
				gold.write(goldgunshop)
				o1.seek(0)
				o = o1.write('1')
			else:
				shop()
		else:
			print('У вас недостаточно щерублей для покупки :(')
			shop()
	elif techname == '5':
		print('Вы выбрали технику Дракона')
		w()
		sp()
		print('Описание:')
		print('Быстрая, мощная, но уязвимая.')
		w()
		sp()
		print('Скорость х./т.:')
		print('2.')
		w()
		sp()
		print('Коронный приём:')
		print('Растерзание - 30.')
		w()
		sp()
		print('Обычный приём:')
		print('Драконий пыл - 15.')
		w()
		sp()
		print('Здоровье:')
		print('85.')
		w()
		sp()
		print('Стоимость:')
		print('700 щерублей.')
		w()
		sp()
		if g >= 700:
			buying = input('Берём? Тогда нажми B. Нет? Жми что угодно: ')
			if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в' and g >= 700:
				print('Здорово, ведь теперь вы владеете техникой Дракона!')
				goldragon = g - 700
				goldragon = str(goldragon)
				gold = open(r'src/golds.txt', 'r+')
				gold.seek(0)
				gold.close()
				gold = open(r'src/golds.txt', 'r+')
				gold.write(goldragon)
				d1.seek(0)
				d = d1.write('1')
			else:
				shop()
		else:
			print('У вас недостаточно щерублей для покупки :(')
			shop()

	elif techname == '6':
		print('Вы выбрали технику Альбатроса')
		w()
		sp()
		print('Описание:')
		print('Shall I go now? GAS! GAS! GAS! (ну вы поняли).')
		w()
		sp()
		print('Скорость х./т.:')
		print('4.')
		w()
		sp()
		print('Коронный приём:')
		print('Клювок судьбы и взлёт в небо - 7 (при попадании вы взлетаете в небо, ПРОСТО ВЗЛЕТАЕТЕ).')
		w()
		sp()
		print('Обычный приём:')
		print('Сами знаете что - 6.')
		w()
		sp()
		print('Здоровье:')
		print('70.')
		w()
		sp()
		print('Стоимость:')
		print('750 щерублей.')
		w()
		sp()
		if g >= 750:
			buying = input('Берём? Тогда нажми B. Нет? Жми что угодно: ')
			if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в' and g >= 750:
				print('Здорово, ведь теперь вы владеете техникой Альбатроса!')
				goldbatros = g - 750
				goldbatros = str(goldbatros)
				gold = open(r'src/golds.txt', 'r+')
				gold.seek(0)
				gold.close()
				gold = open(r'src/golds.txt', 'r+')
				gold.write(goldbatros)
				a1.seek(0)
				a = a1.write('1')
			else:
				shop()
		else:
			print('У вас недостаточно щерублей для покупки :(')
			shop()
	elif techname == '7':
		print('Вы выбрали технику Быка')
		w()
		sp()
		print('Описание:')
		print('Если попадёт - пеняйте на себя...')
		w()
		sp()
		print('Скорость х./т.:')
		print('1.')
		w()
		sp()
		print('Коронный приём:')
		print('Минус один - 32.')
		w()
		sp()
		print('Обычный приём:')
		print('Копыто - 12.')
		w()
		sp()
		print('Здоровье:')
		print('150.')
		w()
		sp()
		print('Стоимость:')
		print('700 щерублей.')
		w()
		sp()
		if g >= 700:
			buying = input('Берём? Тогда нажми B. Нет? Жми что угодно: ')
			if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в' and g >= 700:
				print('Здорово, ведь теперь вы владеете техникой Быка!')
				goldbull = g - 700
				goldbull = str(goldbull)
				gold = open(r'src/golds.txt', 'r+')
				gold.seek(0)
				gold.close()
				gold = open(r'src/golds.txt', 'r+')
				gold.write(goldbull)
				b1.seek(0)
				b = b1.write('1')
			else:
				shop()
		else:
			print('У вас недостаточно щерублей для покупки :(')
			shop()
	elif techname == '8':
		print('Вы выбрали технику Увалютора')
		w()
		sp()
		print('Описание:')
		print('Осторожно! Не давайте ему ва завалить, а то придёт конец!')
		w()
		sp()
		print('Скорость х./т.:')
		print('1.')
		w()
		sp()
		print('Коронный приём:')
		print('Завал (может дать 3 доп. тычки обычным приёмом).')
		w()
		sp()
		print('Обычный приём:')
		print('Лови кулак - 10.')
		w()
		sp()
		print('Здоровье:')
		print('110.')
		w()
		sp()
		print('Стоимость:')
		print('700 щерублей.')
		w()
		sp()
		if g >= 700:
			buying = input('Берём? Тогда нажми B. Нет? Жми что угодно: ')
			if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в' and g >= 700:
				print('Здорово, ведь теперь вы владеете техникой Увалютора!')
				goldval = g - 700
				goldval = str(goldval)
				gold = open(r'src/golds.txt', 'r+')
				gold.seek(0)
				gold.close()
				gold = open(r'src/golds.txt', 'r+')
				gold.write(goldval)
				u1.seek(0)
				u = u1.write('1')
			else:
				shop()
		else:
			print('У вас недостаточно щерублей для покупки :(')
			shop()
	elif techname == '9':
		print('Вы выбрали технику Мегалодона')
		w()
		sp()
		print('Описание:')
		print('Древняя акула тебя порвёт!')
		w()
		sp()
		print('Скорость х./т.:')
		print('0.25.')
		w()
		sp()
		print('Коронный приём:')
		print('Поедание - 45')
		w()
		sp()
		print('Обычный приём:')
		print('Хвостовой плавник - 35')
		w()
		sp()
		print('Здоровье:')
		print('230.')
		w()
		sp()
		print('Стоимость:')
		print('800 щерублей.')
		w()
		sp()
		if g >= 800:
			buying = input('Берём? Тогда нажми B. Нет? Жми что угодно: ')
			if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в' and g >= 800:
				print('Здорово, ведь теперь вы владеете техникой Мегалодона!')
				goldaladon = g - 800
				goldaladon = str(goldaladon)
				gold = open(r'src/golds.txt', 'r+')
				gold.seek(0)
				gold.close()
				gold = open(r'src/golds.txt', 'r+')
				gold.write(goldaladon)
				me1.seek(0)
				me = me1.write('1')
			else:
				shop()
		else:
			print('У вас недостаточно щерублей для покупки :(')
			shop()
	elif techname == '10':
		print('Вы выбрали технику МНЖК-1')
		w()
		sp()
		print('Описание:')
		print('Злой робот-призрак. Довольно быстрый чел. Короче, читай хар-ку и поймешь!')
		w()
		sp()
		print('Скорость х./т.:')
		print('3.')
		w()
		sp()
		print('Коронный приём:')
		print('Моя ножка - 15.')
		w()
		sp()
		print('Обычный приём:')
		print('Хех - 1.')
		w()
		sp()
		print('Здоровье:')
		print('110.')
		w()
		sp()
		print('Стоимость:')
		print('800 щерублей.')
		w()
		sp()
		if g >= 800:
			buying = input('Берём? Тогда нажми B. Нет? Жми что угодно: ')
			if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в' and g >= 800:
				print('Здорово, ведь теперь вы владеете техникой МНЖК-1!')
				goldka = g - 800
				goldka = str(goldka)
				gold = open(r'src/golds.txt', 'r+')
				gold.seek(0)
				gold.close()
				gold = open(r'src/golds.txt', 'r+')
				gold.write(goldka)
				mn1.seek(0)
				mn = mn1.write('1')
			else:
				shop()
		else:
			print('У вас недостаточно щерублей для покупки :(')
			shop()
	elif techname == '11':
		print('Вы выбрали технику Майндера')
		w()
		sp()
		print('Описание:')
		print('Он - матиматек вышшей степини. Но па рускому у него двойка.')
		w()
		sp()
		print('Скорость х./т.:')
		print('1.')
		w()
		sp()
		print('Коронный приём:')
		print('Корень из 25 минус 6 факториал делить на 9 плюс 112 - 37.')
		w()
		sp()
		print('Обычный приём:')
		print('Лёгкая задачка - 30.')
		w()
		sp()
		print('Здоровье:')
		print('75.')
		w()
		sp()
		print('Стоимость:')
		print('800 щерублей.')
		w()
		sp()
		if g >= 800:
			buying = input('Берём? Тогда нажми B. Нет? Жми что угодно: ')
			if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в' and g >= 800:
				print('Здорово, ведь теперь вы владеете техникой Майндера!')
				goldner = g - 800
				goldner = str(goldner)
				gold = open(r'src/golds.txt', 'r+')
				gold.seek(0)
				gold.close()
				gold = open(r'src/golds.txt', 'r+')
				gold.write(goldner)
				md1.seek(0)
				md = md1.write('1')
			else:
				shop()
		else:
			print('У вас недостаточно щерублей для покупки :(')
			shop()
	elif techname == '12':
		print('Вы выбрали технику Желе')
		w()
		sp()
		print('Описание:')
		print('Всегда мечтале о баночке вкусного, малинового желе? Получите её по щеке! ООООЧЕНЬ НАЗОЙЛИВАЯ ТЕХНИКА!!!')
		w()
		sp()
		print('Скорость х./т.:')
		print('5.')
		w()
		sp()
		print('Коронный приём:')
		print('Желейная пытка - 4.')
		w()
		sp()
		print('Обычный приём:')
		print('Хочешь желе? - 3.')
		w()
		sp()
		print('Здоровье:')
		print('70.')
		w()
		sp()
		print('Стоимость:')
		print('800 щерублей.')
		w()
		sp()
		if g >= 750:
			buying = input('Берём? Тогда нажми B. Нет? Жми что угодно: ')
			if buying == 'B' or buying == 'b' or buying == 'В' or buying == 'в' and g >= 750:
				print('Здорово, ведь теперь вы владеете техникой Желе!')
				goldele = g - 750
				goldele = str(goldele)
				gold = open(r'src/golds.txt', 'r+')
				gold.seek(0)
				gold.close()
				gold = open(r'src/golds.txt', 'r+')
				gold.write(goldele)
				j1.seek(0)
				j = j1.write('1')

			else:
				shop()
		else:
			print('У вас недостаточно щерублей для покупки :(')
			shop()
	elif techname == '13':
		print('Пивоваров Илья Сергеевич (Yaliya)')
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
	w()
	w()
	w()
	w()
	sp()
	lobby()

def exit():
    exit()

def sp():
    print('')

# Ожидание
def w():
    sleep(0.3)

# Магазин

# Обратный отсчёт от начала боя
def cd():
    print('3')
    w()
    w()
    sp()
    w()
    print('2')
    w()
    w()
    sp()
    w()
    print('1')
    w()
    sp()
    print('Бой!')
    w()
    w()
    sp()

def lobby():
	print('Вы в лобби')
	w()
	print('У вас', g, 'щерублей')
	w()
	while True:
		ch = input('Чтобы пойти в бой нажмите F; магазин техник - S; посмотреть свой арсенал - A: ')
		if ch == 'F' or ch == 'f' or ch == 'Ф' or ch == 'ф':
			fight()
			return ch
		elif ch == 'S' or ch == 's' or ch == 'Ы' or ch == 'ы':
			shop()
			return ch
		elif ch == 'a' or ch == 'A' or ch == 'а' or ch == 'А':
			ars()
			return ch
		elif ch != 'a' or ch != 'A' or ch != 'а' or ch != 'А' or ch != 'S' or ch != 's' or ch != 'Ы' or ch != 'ы' or ch != 'F' or ch != 'f' or ch != 'Ф' or ch != 'ф':
			print('Неверный символ!')
			sp()
		return ch

# Запуск программы, копирайт и згрузка
def start():
	print('ЩЕКОТАЛЬНЫЙ БОЙ')
	w()
	w()
	sp()
	w()
	w()
	print('(c) Niko the mouse')
	w()
	w()
	sp()
	w()
	print('Загрузка...')
	w()
	w()
	w()
	w()
	sp()
	w()
	w()
	lobby()

techs = ['Вампир', 'Феникс', 'Истребитель', 'Оружейник', 'Дракон', 'Альбатрос', 'Бык', 'Увалютор', 'Мегалодон', 'МНЖК-1', 'Майндер', 'Желе']

coin = ['1','2']

tf = choice(techs)
def ct():
	cointhrow = choice(coin)
	if cointhrow == coin[0]:
		print('Вы ходите первым B)!')
		firstt = 1
	elif cointhrow == coin[1]:
		print('Вы ходите вторым :(!')

def ch_op():
	opponenta = choice(techs)
	sp()
	w()
	print('Итак...')
	w()
	cd()
	print('Ваш протиник -', opponenta)

def arith():
	cd()
	ch_op()
	ct()

# Бой
def fight():
	while True:
		print('Отправимся в арифметический бой (A), в геометричесский (G) или пойдём в рейд на босса (R)?')
		if fch == 'a' or fch == 'a' or fch == 'a' or fch == 'a':
				arith()
				break
		elif fch == 'a' or fch == 'a' or fch == 'a' or fch == 'a':
				geom()
				break
		elif fch == 'a' or fch == 'a' or fch == 'a' or fch == 'a':
				bossraid()
				break
		else:
			print('Ниправельный симвал!!! [тут был Майндер)]')

shop()
