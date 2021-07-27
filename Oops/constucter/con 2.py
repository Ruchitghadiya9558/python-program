class Abc:
    def hello(self):
        print("i am a hello function")
        print("it is hello function")
    def __init__(self):
        print("i am a constucter ")
        print("it is not constucter")
object = Abc()
object.hello()