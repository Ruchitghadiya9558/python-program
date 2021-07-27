class A:
    def hello(self):
        print("hello parent function")

class B(A):
    def hello(self):
        print("child hello function")
    def demo(self):
        print("child demo function")

object = B()
object.demo()
object.hello()

