# dict1 = {
#     "Gu": "Shit",
#     "Bandar": "Monkey",
#     "Ladka": "Boy",
#     "Ladki":"Girl",
# }
# a = input("Enter the word to be searched: ")

# print(dict1.get(a))

# set1 = set()
# set2 = set()
# print (type(set1))

# for i in range(1, 8):
#     a = input("Enter the Value: ")
#     set1.add(a)
# print(set1)

# for i in range(1, 8):
#     b = input("Enter the Value: ") 
#     set2.add(b)
# #print(set1.union(set2))
# # print(set1, set2)
# print(set1.intersection(set2))

dict2 ={}

for i in range(1,3):
    a = input("Enter the language:")
    b = input("Enter the freinds Name:")
    dict2.update({b:a})

print (dict2.get("ash"))