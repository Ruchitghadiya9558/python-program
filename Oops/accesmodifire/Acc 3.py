# protected function

class A:
    def _hello(self):
        print("i am a hello function ")
        print("it is not hello function")
class B(A):
        def demo(self):
            print("i am demo function")
            print("i have not demo function")
            self._hello()
object = A()
object._hello()


