# single inheritance
class A:
    def parent(self):
        print("i am father")
        print("i am nareshbhai")

class B(A):
    def child(self):
        print("a am son")

object = B()
object.child()
object.parent()
