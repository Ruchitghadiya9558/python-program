# 5 & 3 divisible to addition,multipliction,count
mylist=[10,20,30,40,50,55,56,15,58,59,57,56,54,95,98,87]
box=0
for i in mylist:
    if i % 5 == 0 and i % 3==0:
        box = box + i
print(box)

print("-------------------------------")

box =1
for i in mylist:
    if i % 5 ==0 and i % 3 == 0:
        box = box * i
print(box)

print("--------------------------------")

box = 0
for i in mylist:
    if i % 5 ==0 and i % 3 ==0:
        box = box + 1
print(box)