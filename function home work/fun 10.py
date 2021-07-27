# (1-10) 3 divisible

def divi():
    box=0
    for i in range(1,11):
        if (i % 3 ==0):
            box=box + 1
    print("count=",box)
divi()
