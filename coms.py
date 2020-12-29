from time import *
from shop import *
from fight import *
from sys import *
from random import *
from main import*

def exit():
    exit()
def sp():
    print('')

# Ожидание
def w():
    sleep(0.3)

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

