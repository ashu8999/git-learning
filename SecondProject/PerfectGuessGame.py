from random import randint

# class perfectguess:

#     def __init__(self, number):
#         # the secret number the user picked
#         self.number = number
#         self.attempts = 5
#         self.low = 0
#         self.high = 100

#         i = 0
#         while i < self.attempts:
#             # computer's guess, within current range
#             guess = randint(self.low, self.high)   
#             print(f"Attempt {i+1}: Computer guesses {guess}")

#             if guess == self.number:
#                 #if the guessed by computer is equal tot he number which user added
#                 print(f"Computer found the number: {guess}")
#                 break
#             elif guess < self.number:
#                 #if the gueses by computer is less than the number user added it increment the value of and set the new low value
#                 print(f"Computer's guess {guess} is too low")
#                 self.low = guess + 1
#             else:  # guess > self.number
#                 #if the gueses by computer is less than the number user added it increment the value of and set the new High value
#                 print(f"Computer's guess {guess} is too high")
#                 self.high = guess - 1    # lower the upper bound

#             i += 1

#     def show(self):
#         print(f"Number was: {self.number}")
# user = int(input("Enter the number: "))
# a = perfectguess(user)
# a.show()

class perfectguess:

    def __init__(self, number):
        # the secret number the user picked
        self.number = number
        self.attempts = 5
        self.low = 0
        self.high = 100
        self.guess = randint(self.low, self.high)
        i = 0
        while i <= self.attempts:
                if i == self.attempts:
                    print(f"You have lost the round and the number was {self.guess}")
                    
                else:
                    #print(f"in else{i}")
            # computer's guess, within current range
                    print(f"Attempt {i+1}: user guesses {self.number}")
                    print(f"Computer number {self.guess}")

                    if self.guess == self.number:
                        #if the guessed by computer is equal tot he number which user added
                        print(f"You have guessed the number correctly: {self.guess}")
                        inp = self.number
                        break
                    elif self.number< self.guess:
                        #if the gueses by computer is less than the number user added it increment the value of and set the new low value
                        print(f"User guess {self.number} is too low")
                        inp = int(input("Enter the number: "))
                        self.number = inp
                        self.low = inp + 1
                    else:  # guess > self.number
                        #if the gueses by computer is less than the number user added it increment the value of and set the new High value
                        print(f"Computer's guess {self.number} is too high")
                        inp = int(input("Enter the number: "))
                        self.high = inp - 1
                        self.number = inp
                
                i += 1
                print(i)

    def show(self):
        print(f"Number was: {self.number},")

user = int(input("Enter the number: "))
a = perfectguess(user)
a.show()