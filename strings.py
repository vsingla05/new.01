# str = "vansh_singla"
# print(str[::-1])

# -------------------------------(Traversing a string)------------------------------------

# str = "vansh_singla"
# ln = len(str)
# for a in range(-1,-ln-1,-1):
#     print(str[a])





# str = "vansh_singla"
# ln = len(str)
# for i in range(ln-1,-1,-1):
#     print(str[i])

# --------------------------------------------------------------------------------------

#                               (string operators)

# a = "vansh"
# b = "singla"
# c = a+b
# print(c)
# print(type(c))

# d = a*2
# e = b*2
# f = d+e
# print(f)

# str = "vansh_singla"
# if "*" in str:
#     print(True)
# else:
#     print(False)

# ----------------------------------------------------------------------------------------

#                               (ascii values in string)

#        character           ordinal values
#         0 to 9                48-57
#         A to Z                65-90
#         a to z                97-122

# ----------------------------------------------------------------------------------------

#                               (string functions)

# str = "  Vansh_Singla_18_Ai-Engineer  "
# print(len(str))
# a = str.capitalize()
# print(a)
# b = str.count("a")
# print(b)
# c = str.find("e")
# print(c)
# d = str.index("_")
# print(d)
# e = str.isalnum()
# print(e)
# f = str.isalpha()
# print(f)
# g = str.isdigit()
# print(g)
# h = str.islower()
# print(h)
# i = str.isupper()
# print(i)
# j = str.isspace()
# print(j)
# k = str.lower()
# print(k)
# l = str.upper()
# print(l)
# m = str.lstrip()
# print(m)
# n = str.rstrip()
# print(n)
# o = str.strip()
# print(o)
# p = str.startswith(" ")
# print(p)
# q = str.endswith(" ")
# print(q)
# r = str.title()
# print(r)
# s = str.istitle()
# print(s)
# t = str.replace("a","*")
# print(t)

# ---------------------------------(join)-----------------------------------------------

# t = ["1","2","3","4"]
# a = "#".join(t)
# print(a)

# t1 = ("v","a","n","s","h")
# b = "@".join(t1)
# print(b)

# t2 = {"s","i","n","g","l","a"}
# c = "$".join(t2)
# print(c)


# ------------------------------(split)------------------------------------------------

# str = "vansh singla 18 Ai engineer"
# a = str.split()
# print(a)           ----------- returns list


# ------------------------------(partition)---------------------------------------------

# str = "vansh singla 18 Ai Engineer"
# a = str.partition("18")
# print(a)          ----------- returns tuple

# ---------------------------------------------------------------------------------------

#                              (question-1)

# a = "anana"
# b = a[-1::-1]
# if a==b:
#     print("yes")
# else:
#     print("no")

# ----------------------------------------------------------------------------------------

#                                 (question-2)

# v = "ansh vansh kans pansh"
# a = "kansh"
# if a in v:
#     print("yes")
# else:
#     print("no")

# ----------------------------------------------------------------------------------------

#                              (question-3)

# str = "v a n s h s i n g l a"
# li = str.split()
# d = {}
# for i in li:
#     if i not in d.keys():
#         d[i] = 0
#     d[i]+=1
# print(d)

# ------------------------------------------------------------------------

#                          (question-4: even length words)

# data = "i am a boy"
# for word in data.split(" "):
#    if len(word) % 2 == 0:
#       print(word)
# else:
#    pass

# -------------------------------------------------------------------------

#             (question-5: acccept string which contain all vowels)

# str = input("enter string: ")
# str1 = str.lower()

# vowels = "a e i o u"
# b = vowels.split()
# d = []

# for i in str:
#     if i in b:
#         d.append(i)
# print(d)

# if len(b) == len(d):
#     print("contains all vowels")
# else:
#     print("does not contain all vowels")

# ------------------------------------------------------------------------

#                    (question-6: no. of matching character)

# str1 = input("first character: ")
# str2 = input("second character: ")
# str3 = " "
# for i in str1:
#     if i in str2:
#         str3 = str3+i
# print((str3))
# for j in str3:
#     print(str(j),end=" ")  

# --------------------------------------------------------------------------

#                         (question-7: remove all duplicates)

# str = "hello"
# str2 = " "
# st = []
# for i in str:
#     if i not in str2:
#         str2 = str2+i
#         st.append(i)
# print(st)
# str = " "
# for i in st:
#     str = str+i
# print(str)

# ------------------------------------------------------------------------

# a = input().lower()
# b = a.split()
# print(b)
# for i in range(0,len(b)):
#     x = b.count(b[i])
#     if x==1:
#         print(b[i])
#     else:
#         pass

# lst = []
# a = input()
# b = a.lower()
# lst.extend(b)
# print(lst)
# for i in set(b):
#     x = b.count(i)
#     print(i,"has frequency",x)

# for j in lst:
#     if (lst[j]) == x[j]:
#         print(lst[j])

# str = input()
# l = []
# for i in str:
#     if str.count(i)==1:
#         print(i)
#         l.extend(i)
# print(l)
# print("second non repeating char is: ",l[1])

# str = "cat"
# b=0
# for i in range(len(str)):
#     for j in range(0,i+1):
#         if x in str:


# str = "i am a boy i am"
# i = 0
# while i<len(str):
#     count = 0
#     for  j in str:
#         if str[i] == j:
#             count+=1
#     print(str[i],"has frequency = ",count)
#     i+=1

# str = "hello how are you"
# str = str.title()
# str = str.split()
# str1 = " "
# for i in str:
#     str1= str1+i[:-1]+i[-1].upper()+" "
# print(str1)

# str = "hello@#$ how% are you?"
# b = ""
# for i in str:
#     if i.isalpha() or i==" ":
#         b+=i
# print(b)

# for i in range(65,91):
#     print(chr(i),end=" ")
# print()

# for i in range(97,123):
#     print(chr(i),end=" ")

# ---------------------------------------------------------------------------------------

#                                ("my method")

# name = "mahendra singh dhoni"
# name = name.split()
# str  =""
# str2 = ""
# sname = ""
# for i in name:
#     str = str+i[0].upper()
# for j in range(len(str)-1):
#     str2 = str2+str[j]+"."
# sname = sname+name[-1].title()
# print(str2+sname)

# ----------------------------------------------------------------------------------------

#                                 ("other method")

# name = "mahendra singh dhoni"
# name = name.split()
# sname = ""
# for i in range(len(name)-1):
#     s = name[i]
#     sname = sname+s[0].upper()+"."
# sname = sname+name[-1].title()
# print(sname)

# ----------------------------------------------------------------------------------------

# str1 = "vansh"
# str2 = "aansh"
# for i in range(len(str1)):
#     count = 0
#     for j in str2:
#         if str1[i]==j:
#             count+=1
#             break
        
# if count == 1:
#     print("yes")
# else:
#     print("no")

# ----------------------------------------------------------------------------------------

#                               (method-1)

# str1 = "card"
# str2 = "hck"
# for i in range(len(str1)):
#     for j in str2:
#         if str1[i] == j:
#             print("common word is = ",str1[i])

# ----------------------------------------------------------------------------------------

#                                 (method-2)

# str1 = "card"
# str2 = "hilac"
# for i in str1:
#     if i in str2:
#         print(i)
#         break

# ----------------------------------------------------------------------------------------

# str = "hello"
# str2 = ""

# str2 = str2+str[0].upper()+str[1]+str[2].upper()+str[3]+str[4].upper()
# print(str2)

# -----------------------------------------------------------------------------------------

# str = "hello how are you"
# a = ""
# for i in range(len(str)):
#     if i%2==0:
#         a = a+str[i].upper()
#     else:
#         a = a+str[i].lower()
# print(a)    

#  ----------------------------------------------------------------------------------------

# str = "dhevzyf"
# for i in range(len(str)):
#     for j in range(len(str)-1):
#         if str[j]<str[j+1]:
#             str[j] = str[j+1]
#             str[j+1] = str[j]
#             print(str[j])
# print(str)

# str = "BANANA"
# vowels = "AEIOU"
# i = 0
# str = ""
# while i<len(str):
#     count = 0
#     for j in str:
#         if str[i] == j:
#             count+=1
#     print(str[i],"has frequency = ",count)
#     i+=1
    # break

# str = "hello"
# str = list(str)
# max = str[0]
# for i in range(len(str)-1):
#     for j in range(len(str)-1):
#         if str[j]<str[j+1]:
#             str[j],str[j+1] = str[j+1],str[j]
# print(str)

# str = "hellz"
# str = list(str)
# max = str[0]
# for i in range(len(str)):
#     if max<str[i]:
#         max,str[i] = str[i],max
# print("max char in string is ",max)

# str = "helalz"
# str = list(str)
# min = str[0]
# for i in range(len(str)):
#     if min>str[i]:
#         min,str[i] = str[i],min
# print("min char in string is ",min)

# str = "hello how are you"
# str = str.split()
# maxi = (str[0])
# for i in range(len(str)):
#     if len(maxi)<len(str[i]):
#         maxi,str[i] = str[i],maxi
# print(maxi)

# str = "abcdafeghd"
# str2 = ""
# for i in range(len(str)):
#     if str[i] not in str2:
#         str2  =str2+str[i]
# print(str2)

# str = "anana"
# str2 = ""
# ln = len(str)
# for i in range(-1,-ln-1,-1):
#     str2 = str2+str[i]
# if str == str2:
#     print(str,"is pallidrome")
# else:
#     print(str,"is not a pallidrome")

# str = "wel15com15e10r12t7"
# num = 0
# sum = 0
# for i in str:
#     if i.isdigit():
#         num = num*10+int(i)
#     else:
#         sum = sum+num
#         num = 0
# sum = sum+num
# print(sum)

# num = 15
# str = str(num)
# # print(str)
# str = list(str)
# print(str)

# -----------------------------------------------------------------------------------------

#                                (method-1)

# str = input()
# str = list(str)
# l = []
# str[0],str[len(str)-1] = str[len(str)-1],str[0]
# for i in str:
#     l.append(i)
# str2 = ""    
# for i in l:
#     str2 = str2+i
# print(str2)

# -----------------------------------------------------------------------------------------

#                                 (method-2)

# str = input()
# print(str[-1]+str[1:-1]+str[0])

# print(str[0:2]+str[5]+str[3:5]+str[2]+str[6:8])
# str[2],str[5] = str[5],str[2]
# print(str)

# -----------------------------------------------------------------------------------------

#                                    (method-3)

# str = input()
# str = list(str)
# num1 = int(input())
# num2 = int(input())
# str[num1],str[num2] = str[num2],str[num1]
# str2 = ""
# for j in str:
#     str2 = str2+j
# print(str2)

# -----------------------------------------------------------------------------------------

# str = "_v_a_ns_h"
# str1 = ""
# str2 = ""
# for i in str:
#     if i.isalpha():
#         str1+=i
#     else:
#         str2+=i
# print(len(str1))
# print(len(str2))

# ----------------------------------------------------------------------------------------

# str = "hello how are you?"
# str = str.split()
# str2 = ""
# for i in str:
#     str2 = str2+i[0].capitalize()+i[1:len(i)]+" "
# print(str2)

# ----------------------------------------------------------------------------------------

# str = "hello"
# str2 = ""
# for i in range(len(str)):
#     if i%2==0:
#         str2 = str2+str[i]
# print(str2)

# ----------------------------------------------------------------------------------------

# str = "hello world"
# str = list(str)
# vowels = "aeiou"
# vowels = list(vowels)
# count = 0
# for i in str:
#     if i in vowels:
#         count+=1
# print(count)

# ---------------------------------------------------------------------------------------

# str = "hello"
# str = list(str)
# j = 0
# str2 = ""
# str2 = list(str2)
# for i in str:
#     if i not in str2:
#         str2+=i
# while j<len(str2):
#     count = 0
#     for x in str2:
#         if str2[j] == x:
#             count+=1
#     print(str2[j],"has frequency = ", count)
#     j+=1

# ---------------------------------------------------------------------------------

# str = "compteruter"
# str1 = "ter"
# f = 0
# for i in range(len(str)):
#     for j in range(len(str1)):
#         if str[i] == str[j]:
#             j = j+1
#         else:
#             j = 0
    
#     if j == len(str1):
#         f = f+1
#         print("substring",str1,"is found at index = ",i-len(str1)+1)
# if f == 0:
#     print("not found")
# else:
#     print("substring frequency = ",f)

# ----------------------------------------------------------------------------------------

# str = "hello how are you"
# str = str.split()
# count = 0
# for i in str:
#     if len(i) != 0:
#         count+=1
# print(count)




# -----------------------------------------------------------------------------------------
# str = "compteruter"
# str1 = "uter"
# a = str.find(str1)
# if a == -1:
#     print("not found")
# else:
#     print("found")

# ----------------------------------------------------------------------------------------

# str = "compteruter"
# str1 = "terute"
# if str1 in str:
#     print("found")
# else:
#     print("not found")

# ----------------------------------------------------------------------------------------

# str = "hello how are you"
# count = 0
# ch = 0
# n = 0
# for i in str:
#     if i == " ":
#         n+=1
#     else:
#         count+=1
#         if n!=0:
#             ch+=1
# a = n+ch
# print(a) 
# print(n) 
# print(ch)  

# ----------------------------------------------------------------------------------------

# str = "pyt123ho45n6"
# str2 = ""
# sum = 0
# for i in range(len(str)):
#     if str[i].isdigit():
#         str2 = str2+str[i]
#         sum = sum+int(str[i])
# print(sum) 

# -----------------------------------------------------------------------------------------

# str1 = "tamana"
# str2 = "manata"
# str3 = ""
# if len(str1) == len(str2):
#     for i in range(len(str1)):
#         for j in str2:
#             if str1[i] == j:
#                 if str1[i] not in str3:
#                     str3 = str3+str1[i]
# if len(str3) == len(str1):
#     print("yes")
# else:
#     print("no")

# -----------------------------------------------------------------------------------------

# str = "welcome"
# n = 4
# str1 = ""
# for i in range(len(str)):
#     if str[i] == str[n]:
#         continue
#     else:
#         str1 = str1+str[i]
# print(str1)

# ----------------------------------------------------------------------------------------

# str = "  vab dij dmcd  "
# str1 = ""
# for i in range(len(str)):
#     if str[i] == " ":
#         continue
#     else:
#         str1 = str1+str[i]
# print(str1)

# str = "hello    how are  you "
# str = str.split()
# str1 = ""
# for i in range(len(str)):
#     str1 = str1+str[i]+" "
# print(str1)

# ----------------------------------------------------------------------------------------

#                           (**All Substrings Of Given string**)
#                                  (stored in string)

# str = "welcome"
# i = 0
# while i<len(str):
#     str1 = ""
#     for j in range(len(str)-i):
#         str1 = str1+str[i:i+j+1]+" "
#     print(str1)
#     i+=1

# ----------------------------------------------------------------------------------------

#                               (stored in list)

# str = "welcome"
# i = 0
# a = []
# while i<len(str):
#     l = []
#     for j in range(len(str)-i):
#         l.append(str[i:i+j+1])
#     i+=1
#     a.append(l)
# print(a)

# ----------------------------------------------------------------------------------------

#                        (longest pallidromic substring )

# str = "bananas"
# i = 0
# while i<len(str):
#     l = []
#     for j in range(len(str)-i):
#         l.append((str[i:i+j+1]+" "))
#     print(l)
#     i+=1
    # str2 = l[::-1]
    # print(str2)

    # for i in range(len(str1)):
    #     if str1[i] == str2[i]:
    # ln = len(str1)
    # str2 = ""
    # str3 = ""
    # for x in range(-1,-ln-1,-1):
    #     str2 = str2+str1[x]+" "
    # print(str2)
    
    # for y in range(len(str1)):
    #     if str1[y] == str2[y]:
    #         str3 = str3+str1[y]
    # print(str3)


# ln = len(str1)
# str2 = ""
# str3 = ""
# for x in range(len(str1)):
#     str2 = str2+str1[x]
#     print(str2)

# if len(str1) == len(str2):
#     for i in range(len(str1)):
#         if str1[i] == str2[i]:
#             str3 = str3+str1[i]+" "
#         print(str3)


# --------------------------------------------------------------------------

# str = "paypalishiring"
# str1 = ""
# str2 = ""
# str3 = ""
# for i in range(len(str)):
#     if i%4==0:
#         str1 = str1+str[i]+" "
# for i in range(1,len(str)):
#     if i%2!=0:
#         str2 = str2+str[i]
# for i in range(2,len(str)):

# print(str1)
# print(str2)

# ---------------------------------------------------------------------------

# str = "paypalishiring"
# for i in range(len(str)):
#     if i%4==0:
#         print(str[i],end="   ")
# print()
# for i in range(len(str)):
#     if i%2!=0:
#         print(str[i],end=" ")
# print()
# for i in range(len(str)):
#     if (i+2)%4==0:
#         print(str[i],end="   ")
# print()

# -------------------------------------------------------------------------

# str = "hello how are you"
# l = []
# temp = ""
# for i in str:
#     if i == " ":
#         l.append(temp)
#         temp = ""
#     else:
#         temp = temp+i
# ---------------------------------------------------------------------
# temp = temp.split()
# a = l+temp
# print(a)
# ----------------------------------------------------------------------
# l.append(temp)
# print(l)

# -----------------------------------------------------------------------

#                            (method-1)

# str = "welcome to computer"
# str1 = ""
# temp = ""
# for i in str:
#     if i == " ":
#         str1 = str1+temp+" "
#         temp = ""
#     else:
#         temp = temp+i
#         ln = len(temp)//2
#         temp = temp[0:ln].lower()+temp[ln:len(temp)].upper()
# str1 = str1+temp
# print(str1) 

#                           (method-2)

# str = "welcome to python"
# str = str.split()
# str1 = ""
# for i in str:
#     str2 = ""
#     for j in range(len(i)):
#         ln = len(i)//2
#         if j>=ln:
#             str2+=i[j].upper()
#         else:
#             str2+=i[j].lower()
#     str1+=str2+" "
# print(str1)

# -------------------------------------------------------------------------------

# str = "hello how are you hello are you hello"
# str = str.split()
# str1 = ""
# for i in str:
#     if i not in str1:
#         str1+=i+" "
# print(str1)

# ------------------------------------------------------------------------------

# str = "hello how are you"
# str = str.split()
# str1 = ""
# for i in str:
#     str1+=i[0].upper()+i[1:len(i)].lower()+" "
# print(str1)

# ------------------------------------------------------------------------------

# str = "hello hey"
# str1 = ""
# vowels = "aeiou"
# for i in str:
#     if i in vowels:
#         i = "#"
#         str1+=i
#     else:
#         str1+=i
# print(str1)

# -------------------------------------------------------------------------------
    
# str1 = "hello all how are you"
# str1 = str1.split()
# str2 = "are you happy"
# str2 = str2.split()
# l1 = []
# l2 = []
# for i in str1:
#     for j in str2:
#         if i == j:
#             l1.append(i)
#             str2.remove(i)
#             break
#     else:
#         l2.append(i)
# print("common words : ",l1)
# print(l2)
# print(str2)
# ------------------------------------------------------------------------------

#                           (method-1)

# str = "van12sh sing56l3a"
# str1 = ""
# for i in str:
#     if i.isdigit():
#         continue
#     else:
#         str1+=i
# print(str1)     

#                            (method-2)

# str = "van12sh sin1g56l3a"
# str1 = ""
# for i in str:
#     if i>="0" and i<="9":
#         continue
#     else:
#         str1+=i
# print(str1)

# -----------------------------------------------------------------------------

# str = "madam"
# str1 = ""
# for i in range(-1,-len(str)-1,-1):
#     str1+=str[i]
# if str == str1:
#     print("given string is pallidrome")
# else:
#     print("given string is not pallidrome")

# -----------------------------------------------------------------------------

#                              (roman number into integer)

# n = input().upper()
# a = 0
# pre = 0
# dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
# if len(n)>1:
#     for i in range(-1,-len(n)-1,-1):
#         cur = dic[n[i]]
#         if cur<pre:
#             a-=cur
#         else:
#             a+=cur 
#         pre = cur      
#     print(a)

# else:
#     print(dic[n])

# -----------------------------------------------------------------------

# str1 = "listen"
# str2 = "silent"
# if sorted(str1) == sorted(str2):
#     print("anagram")
# else:
#     print("not anagram")

# ---------------------------------------------------------------------------------------

#                                  (unique character)

# str = "leetcode"
# f = 0
# for i in range(len(str)):
#     count = 0
#     # a = 0
#     for j in range(len(str)):
#         if str[i] == str[j]:
#             count+=1
#     if count == 1:
#         a = i
#         f = 1
#         unique = str[i]
#         print("unique character is ",str[i],"with index ",a)
#         break
# if f == 1:
#     print("first unique character is ",unique,"with index = ",a)
     
# else :
#    print(-1)

# ---------------------------------------------------------------------------------------
     
#                                 (reverse a sentense)

# str = input()
# str = str.split()
# str2 = ""
# for i in str:
#     str1 = "" 
#     for j in range(-1,-len(i)-1,-1):
#         str1 = str1+i[j]
#     str2 = str2+str1+" "
# print(str2,end=" ")

# ---------------------------------------------------------------------------------------

#                                 (isomorphic string)

# a = "aab"
# b = "xxy"
# str2 = ""
# for i in range(len(a)):
#     count = 0
#     str1 = ""
#     for j in range(len(b)):
#         if a[i] == a[j]:
#             count+=1
            
#     if a[i] not in str1:
        
#         for c in range(count):
#             if count>1:
#                 b = a[c].replace(a[i],"x")
#                 str1+=b+""
#         else:
#             b = a.replace(a[i],"y")
#             str2+=b+" "
# print(str1+str2)

# str = "hello how are you"
# str = str.split()
# str2 = ""
# str3 = ""
# for i in range(len(str)):
#     if i%2!=0:
#         str1 = ""
#         for j in range(-1,-len(str[i])-1,-1):
#             str1+=str[j]
#         str2+=str1
# else:
#     str2+=str[i]

# str = "hello how are you"
# str = str.split()
# str2 = ""
# for i in str:
    # if i%2!=0:
    #     str2+=str[i[::-1]]+" "
    # else:
    #     str2+=str[i]+" "
    # a = i[::-1]
    # print(a)

# --------------------------------------------------------------------------------------

# str = "42"
# str = int(str)
# print(str)

# str = "    -42"
# str2 = ""
# for i in range(len(str)):
#     if str[i].isspace():
#         continue
#     else:
#         str2+=str[i]
# print(str2)

# str = "4193 with words"
# str2 = ""
# for i in range(len(str)):
#     if str[i].isalpha() or str[i].isspace():
#         continue
#     else:
#         str2+=str[i]
# print(str2)

# ---------------------------------------------------------------------------------------

#                                (unique string (method-1))

# str = "computerr"
# for i in range(len(str)):
#     count = 0
#     for j in range(i+1,len(str)):
#         if str[i] == str[j]:
#             count+=1
#     if count>=1:
#         print("given string is not unique")
#         break
# else:
#     print("given string is unique")

#                             (unique string (method-2))

# str = "madam"
# str = sorted(str)
# for i in range(len(str)-1):
#     if str[i] == str[i+1]:
#         print("not unique")
#         break
# else:
#     print("unique")

# ---------------------------------------------------------------------------------------

#                                (ascii)

# str = "65"
# for i in range(len(str)):
#     print(ord(str[i]))

# print(chr(int(str)))

# ---------------------------------------------------------------------------------------

#                 (**addition of srting without using int function**)

# str1 = input()
# str2 = input()
# i = len(str1)-1
# j = len(str2)-1
# carry = 0
# a = []
# while i>=0 or j>=0:
#     sum = carry
#     if i>=0:
#         sum+=ord(str1[i])-ord("0")
#     if j>=0:
#         sum+=ord(str2[j])-ord("0")
#     i-=1
#     j-=1
#     a.append(sum%10)
#     carry = sum//10
# if carry!=0:
#     a.append(carry)
# str3 = ""
# for i in range(-1,-len(a)-1,-1):
#     str3+=str(a[i])
# print(str3)

# ---------------------------------------------------------------------------------------

#                             (using for loop)

# str = "the sky is blue"
# str = str.split()
# str1 = ""
# for i in range(-1,-len(str)-1,-1):
#     str1+=str[i]+" "
# print(str1)

#                              (using while loop)

# str = "the sky is blue"
# str = str.split()
# str1 = ""
# i = len(str)-1
# while i>=0:
#     str1+=str[i]+" "
#     i-=1
# print(str1)

# -------------------------------------------------------------------------------------

#                      (largest word in string (method-1))

# str = "hello how vanshsinglasss are you vnsingla vanshsingla"
# str = str.split()
# maxi = str[0]
# for i in range(len(str)):
#         for j in range(i+1,len(str)):
#             if len(str[j])>=len(maxi):
#                 str[j],maxi = maxi,str[j]
# print(maxi)

#                       (largest word in string (method-2))

# str = "hello how vanshsinglasss are you vnsingla vanshsingla"
# str = str.split()
# maxi = str[0]
# for i in range(len(str)):
#     if len(str[i])>len(maxi):
#         str[i],maxi = maxi,str[i]
# print(maxi)

# ---------------------------------------------------------------------------------

# str = "VaNsH SiNgLa"
# str2 = ""
# for i in range(len(str)):
#     if str[i].isupper():
#         str2+=str[i].lower()
#     else:
#         str2+=str[i].upper()
# print(str2)

# ----------------------------------------------------------------------------------

# str = "hello how are youare"
# str1 = "ara"
# f = 0
# count = 0
# for i in range(len(str)):
#     for j in range(len(str1)):
#         if str[i] == str[j]:
#             j+=1
#         else:
#             j = 0
#     if j == len(str1):
#         f+=1
#         print("substring is found")
# if f == 0:
#     print("substring is not found")
# else:
#     print("frequency of substring is",f)

# def check_substring(sentence, substring):
#     len_sentence = len(sentence)
#     len_substring = len(substring)
    
#     for i in range(len_sentence - len_substring + 1):
#         found = True
#         for j in range(len_substring):
#             if sentence[i + j] != substring[j]:
#                 found = False
#                 break
#         if found:
#             return True
    
#     return False

# Example usage
# sentence = "hello how are youare"
# substring_to_find = "are"

# if check_substring(sentence, substring_to_find):
#     print("Substring found!")
# else:
#     print("Substring not found.")

# ----------------------------------------------------------------------------------------

#                        (**number of words in string**)

# str = "hello   how are you"
# c = 0
# ch = 0
# for i in range(len(str)):
#     if str[i] == " ":
#         if ch!=0:
#             c+=1
#         ch = 0
#     else:
#         ch+=1
# print(c)
# if ch!=0:
#     c+=1
# print(c)

# ---------------------------------------------------------------------------------------
    
# str1 = ["eat","tea","tan","ate","nat","bat"]
# x1 = []
# x2 = []
# for i in range(len(str1)):
#     x1.append("".join(sorted(str1[i])))
# print(x1)
# for x in range(len(x1)-1):
#     x3 = []
#     for j in range(x+1,len(x1)):
#         if (x1[x]) == (x1[j]):
#             if x1[j] not in x3:
#              x3.append(x1[j])
#     x2.append(x3)
# print(x2)

# ---------------------------------------------------------------------------------------

#              (**longest pallidromic substring of given string**)
#                            (*vansh`s method*`)

# str = input("enter substring:")
# i = 0
# str2 = ""
# while i<len(str):
#     str1 = ""
#     for j in range(len(str)-i):
#         str1+=str[i:i+j+1]+" "
#     str2+=str1
#     i+=1
# str2 = str2.split()

# print(str2)

# str4 = ""
# for i in str2:
#     str3 = ""
#     for j in range(-1,-len(i)-1,-1):
#         str3+=i[j]
#     str4+=str3+" "
# str4 = str4.split()

# print(str4)

# x = 0
# b = ""
# while x<len(str2):
#     a = ""
#     if str2[x] == str4[x]:
#         a+=str2[x]
#     x+=1
#     b+=a+" "
# b = b.split()

# print(b)

# leng = b[0]
# for i in range(len(b)):
#     if len(leng)<len(b[i]):
#         leng,b[i] = b[i],leng

# print(leng)

# print("longest pallidromic substring of a given string is:",leng)

# ------------------------------------------------------------------------------

# str = "computEr"
# for i in range(len(str)):
#     a = 0
#     if str[i].isupper():
#         a = i
#         print("first uppercase character is:",str[i],"with index:",a)
#         break
# else:
#     print("no")

# -------------------------------------------------------------------------------

# str = input().upper()
# d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
# sum = 0
# prev = 0
# curr = 0
# for i in range(-1,-len(str)-1,-1):
#     curr = d[str[i]]
#     if curr<prev:
#         sum-=curr
#     if curr>=prev:
#         sum+=curr
#     prev = curr
# print(sum)

# -------------------------------------------------------------------------------

# str = "aabb"
# f = 0
# for i in range(len(str)):
#     count = 0
#     a = 0
#     for j in range(len(str)):
#         if str[i] == str[j]:
#             count+=1
#     if count == 1:
#         a = i
#         f = 1
#         print("unique character is:",str[i],"with index:",a)

# if f != 1:
#     print(-1)

# -------------------------------------------------------------------------------

#                        (string to integer under given ranges)

# str = "     -3147483645 hello"
# str = str.lstrip()
# a = 1
# result = 0
# for i in range(len(str)):
#     if str[i] == "+":
#         if len(str) == 1:
#             break
#     elif str[i] == "-":
#         if len(str) == 1:
#             break
#         else:
#             a = -1
#     elif not str[i].isdigit():
#         break
#     else:
#         result = result*10+ord(str[i])-ord("0")
# result = result*a
# if result>2**31-1:
#     b = 2**31-1
#     print(b)
# elif result<=-2**31:
#     b = -2**31
#     print(b)
# else:
#     print(result)

# --------------------------------------------------------------------------------------

#                      (multiply two strings without int function)

# str1 = "16"
# str2 = "15"
# temp1 = 0
# temp2 = 0
# for i in range(len(str1)):
#     temp1 = temp1*10+ord(str1[i])-ord("0")
# print(temp1)
# for j in range(len(str2)):
#     temp2 = temp2*10+ord(str2[j])-ord("0")
# print(temp2)
# b = temp1*temp2
# print(b)

# --------------------------------------------------------------------------------------

a = ["flower","flow","flight"]
str1 = ""
for i in a:
    str1+=i+" "
print(str1)


  
          




      
                
        

                







    


 

   

                    

                
       
                



       




           

        



     














      








       
 
            



    















   



        

