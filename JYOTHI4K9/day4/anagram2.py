from collections import Counter
def check(str1,str2):
    if(Counter(str1)==Counter(str2)):
        print("true")
    else:
        print("not ")
str1='silent'
str2='listen'
check(str1,str2)
