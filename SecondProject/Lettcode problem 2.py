# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class solution:

    def addTwoNumbers(l1,l2):
        
        # leng = (len(l1))
        if len(l1) == len(l2):
            carry = 0
            l1.reverse()
            l2.reverse()
            for i in range (len(l1)):
                add = l1[i]+l2[i] + carry
                if add >= 10:
                    carry = l3.append(carry%10)
                    carry = add//10
                else:
                    l3.append(add)


                # print (add)
        else:
            print("length of linked list does not match")

l1 = [2,4,3]
l2 = [5,6,4]
l3 = []

sol = solution.addTwoNumbers(l1,l2)
# print(l3)
final = l3[::-1]

print(final)
