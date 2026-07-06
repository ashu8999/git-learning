a = []
# print(type(a))
for i in range (0,4):
    b = int(input("Enter the Number to be checked: "))
    a.insert(i, b)
# print(a)

# # for i in range (len(a)-1):
# #     if a[i]<a[i-1]:
# #         a.remove(a[i])
# #         j = a
# #         print (j)

# i = 0
# while i < len(a) - 1:
#     if a[i] < a[i - 1]:
#         print(len(a))
#         a.remove(a[i])
#         continue
#     i = i + 1
# #print(a)
# print(len(a))
# print(a[0])
#i = 0
maxvalue = a[0]
for i in range (len(a)):
    if a[i] > maxvalue:
        maxvalue = a[i]
print(maxvalue)