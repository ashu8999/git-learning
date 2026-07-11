from random import randint
class train():
    def train_booking(ticket):
        print(f"your booking is confirmed,{ticket}")

    def train_get_status(status):
        print(f"your train ticket status is: {status}")

    def ticket_fare(fare):
        print(f"your ticket fare is:{fare}")
    

a = ("Panel to Pune")
b = ("Running status of train Pragati Express on time")
c = ("Ticket fare for the train is:",randint(100, 500))

Details = train.train_booking(a), train.train_get_status(b), train.ticket_fare(c)
# print(Details)
