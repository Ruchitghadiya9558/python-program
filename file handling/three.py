name = input("enter the name:")

f = open("my file.txt","w")
f.write(name)
f.close()

f = open("my file.txt","r")
print(f.read())
f.close()


