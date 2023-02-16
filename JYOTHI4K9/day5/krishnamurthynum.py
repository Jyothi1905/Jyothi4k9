#krishnamurthys num/strong num using funcs
'''145=1!+4!+5!
      =1+24+120
      =145'''
def fact(r):
    if(r==1):
     return 1
    return r*fact(r-1)    
num=int(input("enter"))
x=num
s=0
while(num>0):
  y=num%10
  s+=fact(y)
  num//=10
if(s==x):
    print("KM")
else:
    print("no")
  
  
