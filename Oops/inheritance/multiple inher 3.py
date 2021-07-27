# multiple inheritance

class A:
    def parent(self):
        print("i am father ")

class B:
    def child(self):
        print("i am child of A")

class C(A,B):
    def subchild(self):
        print("i am child of B")

object = C()
object.subchild()
object.child()
object.parent()