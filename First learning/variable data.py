# a = int (input ("Enter the number3: "))
# b = str (input ("Enter the number1: "))
# d = a<b
# print(d)
# # e = type(d)
# # print(e)

#18 client above 65%
#10 clients above 60%
#19 client below 60%

#remainder of the division
from itertools import count


a = int (input ("Enter the number 1: "))
b = int (input ("Enter the number 2: "))
c = int (input ("Enter the number 2: "))
d = int (input ("Enter the number 2: "))
e = int (input ("Enter the number 2: "))
f = int (input ("Enter the number 2: "))
g = int (input ("Enter the number 2: "))
h = int (input ("Enter the number 2: "))
k = [a, b, c, d, e, f, g, h]
p = len(k)
# print(j)
j= 0
for i in range(len(k)):
    j = j + k[i]
    print(j)
    
print ("average of the numbers is: ", j/p)


    #print(j)
    
# print(len(j))
# k = len(j)
# p = i/k
# print(p)