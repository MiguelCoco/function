#if elif 使用
guess_me = 7
start = 1
while True:
	if start < guess_me:
		print('too low')
	elif start == guess_me:
		print('found it！')
		break
	elif start > guess_me:
		print('oops')
		break
	start += start
#for遍历列表
list = [3, 2, 1, 0]
for num in list:
	print(num)
#列表推导式
list_2 = [even for even in range(10) if even % 2 == 0 ]
print(list_2)
#字典推导式
squares = {key : key**2 for key in range(10)}
print(squares)
#集合推导式
odd = {num for num in range(10) if num % 2 == 1}
print(odd)
#生成器推导式
for thing in ('Got %s' %number for number in range(10)):
	print(thing)
#定义good（）函数
def good():
	return ['Harry','Ron','Hermione']
print(good())
#定义生成器函数
def get_odds():
	for number in range(1,10,2):
		yield number
for count,number in enumerate(get_odds(),1):
	if count == 3:
		print('The third number is :',number)
		break
#定义装饰器test
def test(func):
	def new_func(*args,**kwargs):
		print('start')
		result = func(*args,**kwargs)
		print('end')
		return result
	return new_func
#应用装饰器
@test
def greeting():
	print('Greetings,Earthling')
print(greeting())


