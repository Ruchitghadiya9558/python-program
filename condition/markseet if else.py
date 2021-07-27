math  = int (input('enter the marks math:'))
guj   = int (input('enter the marks guj:'))
eng   = int (input('enter the marks eng:'))
soci  = int (input('enter the marks soci:'))
chem  = int (input('enter the marks chem:'))
phy   = int (input('enter the marks phy:'))
bio   = int (input('enter the marks bio:'))

total = (math + guj + eng + soci + chem + phy + bio)
per   = total/7

print('total marks=',total)
print("percentage=",per)

if per < 35:
	print('sorry you are failed')
elif per>=35 and per<60:
	#35-59
	print('second class')
elif per>=60 and per<80:
	#60-79
	print('first class')
else:
	print('discription')

	