#global and local variables
var='jyothi'
def show():
    global var1
    var1='tall'
    print("in function var cis",var)
show()
print("outside func var is",var1)
print("var is ",var)
