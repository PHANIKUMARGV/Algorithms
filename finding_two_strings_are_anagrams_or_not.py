from collections import Counter
String1=input()
String2=input()
if Counter(String1)==Counter(String2):
    print(String1.upper(),'and',String2.upper(),'are anagrams')
else:
    print(String1.upper(),'and',String2.upper(),'are not anagrams')
