#program to check whether given num is even or odd by using a single stance class obj with an attribute following a constructor,test case:21
class number:
    even=0
    def check(self,num):
        if num%2==0:
          self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print("num is even",num)
        else:
            print("num is odd",num)
n=number()
n.even_odd(21)


'o/p:num is odd 21'
