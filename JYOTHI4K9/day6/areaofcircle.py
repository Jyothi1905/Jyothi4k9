#program that has a class named cicle,use a class variable to define the values of constant pi.use this class variable to calculate area and circumference of the circle with specified radius where radius=7.5
class circle:
    pi=3.14159
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        return circle.pi*self.rad*self.rad
    def circum(self):
        return 2*circle.pi*self.rad
c= circle(7.5)
print("area=",c.area())
print("circumference=",c.circum())


'o/p:area= 176.7144375
     circumference= 47.12385'
