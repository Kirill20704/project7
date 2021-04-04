''' написать упрощённую версию игры в карты
нажать от 0 до 5 для выбора карты, если несколько карт, то ввести через пробел
ввести 6, чтобы принять карты во время хода противника'''
from random import *
s = [ [i + j for i in 
	['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	] for j in '♤♡◇♧']
v = ['l']
def cor(a, c, d):
	''' выбор наименьшей карты для действия '''
	b = c.index(min(a))
	while True:
		if p2[b][-1] != d[-1] or p2[b][-1] != flag[-1]:
			break
		b += 1
	return b
def filt():
	''' Достать случайную карту из колоды '''
	r2 = 'l'
	while r2 in v:
		r1 = choice(s)
		r2 = choice(r1)
	v.append(r2)
	return r2

def autoselect1():
	''' ответ на ход игрока '''
	ch = 1
	pr = []
	for j in range(len(cds)):
		m = [i[-1] for i in p2]
		nums = [int(i[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')) for i in p2]
		cds1 = [int(i[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')) for i in cds]
		ind = [nums[i] for i in range(len(nums)) if m[i] == cds[j][-1] if nums[i] > cds1[j]]
		fl = [nums[i] for i in range(len(nums)) if m[i] == flag[-1]]
		if len(ind) > 0  :
			e = cor(ind, nums, cds[j])
			pr.extend([cds[j], p2.pop(e)])
		elif cds[j][-1] != flag[-1] and flag[-1] in m:
			e = cor(fl, nums, cds[j])
			pr.extend([cds[j], p2.pop(e)])
		else:
			ch = 0
		if ch == 0:
			p2.extend(cds)
			n += 1
			print('Ваш ход')
			break
	if ch == 1:
		print(pr)
		h.extend(pr)

def autoselect2():
	''' ход программы '''
	h1 = []
	m = [i[-1] for i in p2]
	nums = [int(i[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')) for i in p2]
	ind = [nums[i] for i in range(len(nums)) if m[i] != flag[-1]]
	fl = [nums[i] for i in range(len(nums)) if m[i] == flag[-1]]
	if len(fl) > 0:
		pn = p2[cor(ind, nums, flag)]
	else:
		pn = p2[nums.index(min(nums))]
	for i in range(p2.count(pn)):
		z = p2.pop(p2.index(pn))
		print(z)
		h.append(z)
		h1.append(z)
	return h1

def apend(a):
		''' добор карт '''
		while len(a) < 6:
			a.append(filt())

p1 = [filt() for i in range(6)]
print(p1)
p2 = [filt() for i in range(6)]
flag = filt()
print(flag[-1])
chn = 1
n = 0
m = 0
h = []
while True:
	if len(p1) == 0 or len(p2) == 0:
		break
	c = filt()
	if n % 2 == 0:
		cdsn = list(map(int, input().split()))
		cds = [p1[i] for i in cdsn] 
		for u in cds:
			p1.remove(u)
		autoselect1()
		apend(p1)
		apend(p2)
	if n % 2 != 0:
		h1 = autoselect2()
		ans = list(map(int, input().split()))
		if ans[0] == 6:
			p1.extend(h1)
			n += 1
			apend(p1)
			apend(p2)
		else:
			h.extend(h1)
			h.extend([p1[i] for i in ans])
			for i in [p1[i] for i in ans]:
				p1.remove(i)
			apend(p1)
			apend(p2)
	apend(p1)
	apend(p2)
	print(p1)
	n += 1
	m += 1
if len(p1) == 0:
	print('Вы победили')
else:
	print('Вы проиграли')
print('ходов:', m)
