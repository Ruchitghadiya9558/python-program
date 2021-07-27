# nested if 3 number larjest

a = int (input('enter the number a ='))
b = int (input('enter the number b ='))
c = int (input('enter the number c ='))

if a>b:
	if a>c:
		print('a is maximum number')
	else:
		print('c is maximum number')
else:
	if b>c:
		print('b is maximum number')
	else:
		print('c is maximum number')
