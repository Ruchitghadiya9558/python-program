# list for the max and min number

mylist=[10,20,30,40,80,40,70,85,65,45]
max = 0
min = 90
for i in mylist:
    if i > max:
        if i < min:
            min = i
        max = i
print("max=",max)
print("min=",min)
