str1='race'
str2='acer'
if(len(str1)==len(str2)):
    if(sorted(str1)==sorted(str2)):
        print("anagram")
    else:
        print("not a anagram")
else:
    print("not a anagram as lenght differs")
