try:
    num = 10/0
    print(num)
except ZeroDivisionError as e:
    print("error",e)
finally:
    print("i am else")
    print("thank you")
try:
    my,list = [10,20,30,40]
    print([4])
except ValueError as e:
    print("error",e)
finally:
    print("thank you")