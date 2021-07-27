#multi level inheritance
class A:
    def parent(self):
        print("i am father")
        print("i am ramesh bhai")
class B(A):
    def child(self):
        print("i am child A")
        print("i am ruchit")
class C(B):
    def subchild(self):
        print("i am subchild of B")

object = C()
object.subchild()
object.child()
object.parent()
