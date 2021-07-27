# privet function
class Abc:
    def hello(self):
        print("i am a hello function")
        self.__demo()
        self.__computer()

    def __demo(self):
        print("i am a demo function ")

    def __computer(self):
        print("i am computer developer")
        print("i am python developer")

A = Abc()
A.hello()

