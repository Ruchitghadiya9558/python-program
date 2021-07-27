class employee:
        empid = 0
        empname =""

        def setvaluse(self,id,name):
            self.__empid = id
            self.__empname=name
        def getvaluse(self):
            print("employee id =",self.__empid)
            print("employee name =",self.__empname)

id = int(input("enter the id :"))
name = input("enter the empname :")

object = employee()
object.setvaluse(id,name)
object.getvaluse()





