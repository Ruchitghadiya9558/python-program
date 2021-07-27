# there are four type function 1.store 2.delete 3.copy 4.change val

mylist = [10,20,30,40,50,55,88,77,66,99]
print(mylist)
total = len (mylist)
print(total)
print(mylist[5])

print(mylist[2:6])
print((mylist[:5]))
print(mylist[5:])

print(mylist[-2])
print(mylist[-7:-2])

# store val
mylist.append(90)
print(mylist)
mylist.insert(3,100)
print(mylist)

# delete val
mylist.pop()
print(mylist)
mylist.remove(10)
print(mylist)

# copy

x=mylist.copy()
print(x)
x.clear()
print(x)

# change val

mylist[5] =100
print(mylist)
