from time import *
from Main impor *
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
