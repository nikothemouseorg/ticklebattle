from coms import*
from shop import*
from random import *

techs = ['Вампир', 'Феникс', 'Истребитель', 'Оружейник', 'Дракон', 'Альбатрос', 'Бык', 'Увалютор', 'Мегалодон', 'МНЖК-1', 'Майндер', 'Желе']

coin = ['1','2']

tf = choice(techs)

def arith():
	opponenta = choice(techs)
	sp()
	w()
	print('Итак...')
	w()
	cd()
	print('Ваш протиник -', opponenta)
	cointhrow = choice(coin)
	if opponenta == techs[0]:
		if cointhrow == coin[0]:
			print('Вы ходите первым B)!')
			firstt = 1
		elif cointhrow == coin[1]:
			print('Вы ходите вторым :(!')
			firstt = 2
	if opponenta == techs[1]:
		if cointhrow == coin[0]:
			print('Вы ходите первым B)!')
			firstt = 1
		elif cointhrow == coin[1]:
			print('Вы ходите вторым :(!')
			firstt = 2
	if opponenta == techs[2]:
		if cointhrow == coin[0]:
			print('Вы ходите первым B)!')
			firstt = 1
		elif cointhrow == coin[1]:
			print('Вы ходите вторым :(!')
			firstt = 2
	if opponenta == techs[3]:
		if cointhrow == coin[0]:
			print('Вы ходите первым B)!')
			firstt = 1
		elif cointhrow == coin[1]:
			print('Вы ходите вторым :(!')
			firstt = 2
	if opponenta == techs[4]:
		if cointhrow == coin[0]:
			print('Вы ходите первым B)!')
			firstt = 1
		elif cointhrow == coin[1]:
			print('Вы ходите вторым :(!')
			firstt = 2
	if opponenta == techs[5]:
		if cointhrow == coin[0]:
			print('Вы ходите первым B)!')
			firstt = 1
		elif cointhrow == coin[1]:
			print('Вы ходите вторым :(!')
			firstt = 2
	if opponenta == techs[6]:
		if cointhrow == coin[0]:
			print('Вы ходите первым B)!')
			firstt = 1
		elif cointhrow == coin[1]:
			print('Вы ходите вторым :(!')
			firstt = 2
	if opponenta == techs[7]:
		if cointhrow == coin[0]:
			print('Вы ходите первым B)!')
			firstt = 1
		elif cointhrow == coin[1]:
			print('Вы ходите вторым :(!')
			firstt = 2
	if opponenta == techs[8]:
		if cointhrow == coin[0]:
			print('Вы ходите первым B)!')
			firstt = 1
		elif cointhrow == coin[1]:
			print('Вы ходите вторым :(!')
			firstt = 2
	if opponenta == techs[9]:
		if cointhrow == coin[0]:
			print('Вы ходите первым B)!')
			firstt = 1
		elif cointhrow == coin[1]:
			print('Вы ходите вторым :(!')
			firstt = 2
	if opponenta == techs[10]:
		if cointhrow == coin[0]:
			print('Вы ходите первым B)!')
			firstt = 1
		elif cointhrow == coin[1]:
			print('Вы ходите вторым :(!')
			firstt = 2
	if opponenta == techs[11]:
		if cointhrow == coin[0]:
			print('Вы ходите первым B)!')
			firstt = 1
		elif cointhrow == coin[1]:
			print('Вы ходите вторым :(!')
			firstt = 2

# Бой
def fight():
	while True:
		fch = input('Какой режим выберем? Арифметический (A), геометричемкий (G) или пойдём в рейд на босса (R)?')
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
			print('НепрОвильный симвАл!')

