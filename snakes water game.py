#Snake drinks Water → Snake wins
#Water drowns Gun → Water wins
#Gun shoots Snake → Gun wins
#Same choice by both players → Draw


def snakegame():
        
        game = {
            "Snake" : "Water",
            "Water" : "Gun",
            "Gun" : "Snake" 
        }
        return(game)
        
game = snakegame() 

a = input("Enter the Game name:" )
comp = input ("Enter the game name :")

if a == comp:
        print("Game draw, Go Again")

elif game.get(a) == comp:
        print("Ash Wins", game.get(a))

else:
        print("computer wins")