from random import randint
class train():
    def train_booking(ticket):
        print(f"your booking is confirmed,{ticket}")

    def train_get_status(status):
        print(f"your train ticket status is: {status}")

    def ticket_fare(fare):
        print(f"your ticket fare is:{fare}")
    
class traindetails(train):
    @cl
    def train_ticket_update(ticket):
        print(f"Your ticket has been cancelled,{ticket}")
    
    # def train_run(status):
    #     print(f"Your ticket has been cancelled,{status}")
    
    # def train_fare(fare):
    #     print(f"Your ticket fare has increased,{fare}")

a = input("Enter your travel location")
b = input("Enter your train name")
c = ("Ticket fare for the train is:",randint(100, 500))

Details = train.train_booking(a), train.train_get_status(b), train.ticket_fare(c)
# print(Details)
