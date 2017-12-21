import time # learn more: https://python.org/pypi/time
import json
import sys
def convert(a,b):
	add = a%b
	if a<=1:
		return str(a)
	else:
		return str(convert(a//b,b)) + ',' + str(add)

def add_one(number, system):
	number = number[:]
	index = -1
	goon = True
	while goon:
		if number[index] < system:
			goon = False
		else:
			index = index - 1
	number[index] = number[index] + 1
	for i in range(index + 1, 0):
		number[i] = 1
	return number

def is_last_number(number, system):
	for zahl in number:
		if zahl < system:
			return False
	return True

def get_combinations(start, sys):
	print(start, sys)
	weiter = True
	combs = [start]
	while weiter:
		if is_last_number(combs[-1], sys):
			weiter = False
		else:
			combs.append(add_one(combs[:][-1], sys))
	return combs

def get_all_combinations(quersumme):
	alle = []
	for i in range(quersumme):
		cur = get_combinations([1 for j in range(i+1)], quersumme)
		for each in cur:
			alle.append(each)
	return alle

def get_filtered_combinations(quersum, le):
	alle = get_all_combinations(quersum)
	eq = []

	for array in alle:
		if len(array) == le and quersumme(array) == quersum:
			eq.append(array)
	# print('QS ', quersumme, ':', len(eq))
	return eq

def quersumme(array):
	sume = 0
	for i in array:
		sume = sume + i
	return sume	

def is_littlist(array):
	return 0 in array

def get_highest(array):
	highest = array[0]
	for number in array:
		if number > highest:
			highest = number
	return highest

def convert_to_decimal(array, system):
	array = array[:]
	while not is_littlist(array):
		for x in range(len(array)):
			array[x] = array[x] - 1
	
	#system = get_highest(array) + 1
	converted = 0
	for i in range(-len(array), 0):
		converted = converted + (array[i] * (system ** ((0 - i) - 1)))
	return converted

def convert_from_decimal(num, system):
	print(num, system)
	converted = []
	while num > 0:
		converted.append(int(num % system))
		num = (num - (num % system)) / system
	converted.reverse()
	return converted

def fill_up(num, length):
	while len(num) < length:
		num.reverse()
		num.append(0)
		num.reverse()
	return num

def count_up_to(num, to):
	while quersumme(num) < to:
		for i in range(len(num)):
			num[i] = num[i] + 1
	return num

def from_number_to_string(num):
	string = ''
	for each in num:
		string += chr(each-1)
	return string

def make_readable(num):
	converted = [int(i) for i in convert(num, 255).split(',')]
	for each in range(len(converted)):
		converted[each] = chr(converted[each])
	return converted
	
# dic = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZäüöÄÜÖ,.;:-_<>|^°!"§$%&/()=?\\}][{@€#\'~+*'
# string = 'Hallo ich bin Basti und ich probiere hier etwas herumdiedeldum'
# str_array = []

# for char in string:
# 	if char in dic:
# 		str_array.append(dic.index(char) + 1)
# c = quersumme(str_array)
# le = len(str_array)
# key = convert_to_decimal(str_array, c-le+1)

# print('-- HIDDEN --')
# print(str_array)
# print('System:', c-le+1)
# print('-- HIDDEN --')
# print('')

# converted_key = convert(key, len(dic)).split(',')
# utf_8_key = ''.join([dic[int(i)] for i in converted_key])

# print('Key', utf_8_key)
# print('Lenght', le)
# print('Quersumme', c)
# print('')

# system = c - (le - 1)
# rawest = convert(key, system)
# raw = [int(i) for i in rawest.split(',')[1:]]
# in_system = count_up_to(fill_up(raw, le), c)
# print(len(in_system))
# print('System', system)
# print('In System ', in_system)
# print('String', from_number_to_string(in_system))
# print(quersumme(in_system))


# print('Array:', str_array)
# print('Quersumme:', c)

# filtered = sorted(get_filtered_combinations(c, le))

# print('Filtered: (', len(filtered), ')', filtered)

def encrypt(string):
	dic = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZäüöÄÜÖ,.;:-_<>|^°!"§$%&/()=?\\}][{@€#\'~+*1234567890'
	str_array = []
	for char in string:
		str_array.append(ord(char) + 1)
	c = quersumme(str_array)
	le = len(str_array)
	key = convert_to_decimal(str_array, c-le+1)
	# converted_key = convert(key, len(dic)).split(',')
	# utf_8_key = ''.join([dic[int(i)] for i in converted_key])

	return c, le, key

def decrypt(c, length, key):
	dic = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZäüöÄÜÖ,.;:-_<>|^°!"§$%&/()=?\\}][{@€#\'~+*1234567890'
	system = c - (length - 1)
	rawest = convert(key, system)
	raw = [int(i) for i in rawest.split(',')[1:]]
	in_system = count_up_to(fill_up(raw, length), c)
	return from_number_to_string(in_system)

dic = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZäüöÄÜÖ,.;:-_<>|^°!"§$%&/()=?\\}][{@€#\'~+*1234567890'

string = 'Hallo'
c, length, key = encrypt(string)
print('Cross sum:', c)
print('Length:', length)
print('Key:', key)

count = {}

for num in str(key):
	if str(num) in count:
		count[str(num)] = count[str(num)] + 1
	else:
		count[str(num)] = 1

for num in sorted(count):
	print(num, ':', count[num])

[sys.stdout.write(i) for i in make_readable(key)]
print('')
print(len(make_readable(key)))
print(len(string))

open('raw.json', 'w').write(json.dumps({'string': string}))
open('key.json', 'w').write(json.dumps({'string': ''.join(make_readable(key))}))

# converted_key = convert(key, len(dic)).split(',')
# utf_8_key = ''.join([dic[int(i)] for i in converted_key])
# print(len(str(utf_8_key)))
# c2, length2, key2 = encrypt(str(utf_8_key))
# converted_key2 = convert(key2, len(dic)).split(',')
# utf_8_key2 = ''.join([dic[int(i)] for i in converted_key2])
# print(len(str(utf_8_key2)))
# print(decrypt(c,length, key))

# key = 'Hallo Hallo Hallo Hallo Hallo Hallo Hallo Hallo '
# for i in range(10):
# 	c, length, key2 = encrypt(key)
# 	converted_key = convert(key2, len(dic)).split(',')
# 	key = ''.join([dic[int(i)] for i in converted_key])
# 	print(len(key))