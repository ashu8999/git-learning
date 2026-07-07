# sum of greatest numbers using function

# def greatest(a,b,c):

#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     elif c>a and c>b:
#         return c  


# a = int (input("first number" ))
# b = int (input("first number" ))
# c = int (input("first number" ))

# print(greatest(a,b,c))
# Input: nums = [3,2,4], target = 6
# # Output: [1,2]
#         for i in range(len(nums)):
#                 if i <= (len(nums)-1):
#                         if i <= len(nums):          
#                             if nums[i] + nums[i-1] == target:
#                                 result = [i-1, i]
#                                 return result
#                                 #result.append([i-1, i])
                                
#                         else:
#                             break
                        

# nums = [3,3]
# target = 6

# def twoSum(nums, target):
#     for i in range(len(nums)):
#          for j in range(i+1, len(nums)):
#             # print(j)
#             if nums[j] + nums[i+1] == target:
#                 # print(j)
#                 result = i, j
#                 return(result)



                
# print(twoSum(nums, target))

#function to calculate frahenhiet to celcius
#(franheneit - 32) × 5/9

# def calculation(frahen):
#     celcius = (frahen - 32) * 5 / 9
#     return celcius

# frahen = float (input("Enter the franheight value:"))
# c = calculation(frahen)
# print(f"degree is {round(c)}")