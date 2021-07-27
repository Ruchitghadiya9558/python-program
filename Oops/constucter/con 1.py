class Abc :

	def __init__(self,id,name):
		self.__a = id 
		self.__b = name 
	def getvaluse(self):
		print("enter the id=",self.__a)
		print("enter the name=",self.__b)
		

id = int(input("enter the id :"))
name = input("enter the name :")

object = Abc(id,name)
object.getvaluse()
