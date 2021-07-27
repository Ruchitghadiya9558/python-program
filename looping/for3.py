# 1-50  5 and 7 div.
x=range(1,51)
for i in x:
    if (i%5==0) and (i%7==0):
        print(i)
for j in x:
    if (j%5==0) or (j%7==0):
        print(j)


