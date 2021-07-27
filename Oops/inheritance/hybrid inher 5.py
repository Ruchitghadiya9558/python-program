# hybrid inheritance

class A:
    def parent(self):
        print("i am parent")
class B:
    def child(self):
        print("i am child A")
class C(A,B):
    def subchild(self):
        print("i am child B")
class X(C):
    def child2(self):
        print("i am child of A")
class Y(C):
    def child3(self):
        print("i am child of B")

object = C()
object.parent()
object.subchild()
object.child()

