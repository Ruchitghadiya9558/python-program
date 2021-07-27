from customarerror import mycustomarerror

n = input("enter the number:")

try:
    if n<=0:
        raise mycustomarerror("number is either zero or negative ");
except mycustomarerror as e:
    print(e)
finally:
    print("good bye....")



