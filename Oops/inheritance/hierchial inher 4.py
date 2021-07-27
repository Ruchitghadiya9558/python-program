# hirchial inheritance

class A:
    def parent(self):
        print("i am parent ")
class B(A):
    def child(self):
        print("i am child of A")
class C(A):
    def subchild(self):
        print("i am child of B")

object = C()
object.subchild()
#object.child()
object.parent()
