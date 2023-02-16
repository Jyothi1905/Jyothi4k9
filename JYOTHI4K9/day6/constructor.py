'''constructor:

     syntax:_ _init_ _'''

#program
class abc:
    def __init__(self,value):
        print("this is in class")
        self.value=value         #constructing variable
        print("the value is",value)
obj=abc(100)     

'o/p:this is in class
     the value is 100'
