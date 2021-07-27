# list 4 divisible to addition

mylist=[10,20,30,40,50,60,70,80,90,100,110,120,130]
box=0
for i in mylist:
    if i % 4 == 0:
        box = box + i
	print(box)