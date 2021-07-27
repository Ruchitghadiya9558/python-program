class Abc:
    def hello(self):
        print("hello function")
    def __str__(self):
        return "hello developer"

object = Abc()
print(object)