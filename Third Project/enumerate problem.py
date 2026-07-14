# Write a program to print third, fifth and seventh element from a list using enumerate
# function


l1 = [1,2,5,6,7,9,10,12,1,4,5,4,547,49,74,3,697,943,1,7,314,57,641,36,9]
try:
    for index, item in enumerate(l1):

        if index == 2:
            print(item)
        elif index == 7:
            print(item)
        elif index == 3:
            print(item)
        else:
            pass
            #print("tuzhi aai ghal")

except Exception as err:
    print(err)

finally:
    print("Deepak chya aai cha bhok")
