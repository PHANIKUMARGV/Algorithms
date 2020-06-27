String1=input() 
String2=input()
def Subsequence(String1,String2,lenofString1,lenofString2):
     m1=lenofString1
     n1=lenofString2
     if m1==0:
          return True              #the aim is to find the possibilty of whether
     if n1==0:                     #we can obtain String1 from String2 by deleting some of
          return False             #the letters in String2..(The letters need not to be contiguos)
     if String1[m1-1]==String2[n1-1]:
          return Subsequence(String1,String2,lenofString1-1,lenofString2-1)
     return Subsequence(String1,String2,lenofString1,lenofString2-1)
if Subsequence(String1,String2,len(String1),len(String2)):
     print(String1.upper(),'is a subsequence of',String2.upper())
else:
     print(String1.upper(),'is not a subsequence of',String2.upper())
