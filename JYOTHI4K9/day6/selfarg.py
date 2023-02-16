#program to create self argument and access an obj
class abc:
    attribute1=10
    def display(self):
        print("this is in class")
obj=abc()     
print(obj.attribute1)
obj.display()
 'o/p:-10
       this is in class'
