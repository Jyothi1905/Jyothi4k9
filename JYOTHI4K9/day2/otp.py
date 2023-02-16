email=jyothi@gmail.com
pwd=123
cemail=input("enter the email:")
cpwd=int(input("enter the pwd:"))
if(email==cemail and pwd==cpwd):
     print("login success")
     otp=int(input("enter the otp"))
     if(otp==345):
         print("order placed successfully")
     else:
        print("order failed")
