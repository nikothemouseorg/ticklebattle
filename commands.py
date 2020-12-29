from time import *
from Main impor *

def init_techs():
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
# Создаём списки техник
def lists():
    techs = ['Вампир', 'Феникс', 'Истребитель', 'Оружейник', 'Дракон', 'Альбатрос', 'Бык', 'Увалютор', 'Мегалодон', 'МНЖК-1', 'Майндер', 'Желе']
    
    coin = ['1','2']

    tf = choice(techs)

def w():
	sleep(0.3)
# Пробел между строками
def sp():
	print('')
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

