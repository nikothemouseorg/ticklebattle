# Импортируем нужные библиотеки
from random import*
from time import*

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
au1 = open(r'src/saves amulet.txt', 'r+')
lit1 = open(r'src/saves literals.txt', 'r+')

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
au = au1.read(1)
lit = lit1.read(1)

# Создаём списки техник и артефактов
techs = ['Вампир', 'Феникс', 'Истребитель', 'Оружейник', 'Дракон', 'Альбатрос', 'Бык', 'Увалютор', 'Мегалодон', 'МНЖК-1', 'Майндер', 'Желе']
artifacts = ['Амулет удачи', '[Литералы]']

# Создаём переменную выбора техники у противника
tf = choice(techs)

# Пробел между строками
def sp():
	print('')

# Ожидание
def w():
	sleep(0.3)

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
		buynum = int(input('Введите номер понравившейся вам вещи (без точки): '))
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
	print('Бой!')
	w()
	w()
	sp()

# Список техник и артефактов, которыми вы владеете
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

# Лобби. Тут можно пойти в магаз, посмотреть арсенал, и пойти в бой
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

# Бой
def fight():
	cd()

# Основная программа
start()