# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# # Rock crushes Scissors
# Scissors ──cuts────► Paper
# Paper ──covers────► Rock
# Rock ──crushes───► Lizard
# Lizard ──poisons──► Spock
# Spock ──smashes──► Scissors

# Scissors ──decapitates──► Lizard
# Lizard ──eats──────────► Paper
# Paper ──disproves──────► Spock
# Spock ──vaporizes──────► Rock
# Rock ──crushes─────────► Scissors

def RockGame (): 
    Rules = {
            "Scissors" : ["Lizard","Paper"],
            "Paper"  : ["Spock", "Rock"],
            "Rock"   : ["Scissors", "Lizard"],
            "Spock"  : ["Rock", "Scissors"],
            "Lizard" : ["Paper", "Spock"]
        }
    
    return(Rules)


rules = RockGame()
Ash = input("Enter your Choice: ")
Friend = input("Enter your Choice: ")

if Ash ==  Friend:
    print("Game Draw, Restart")

elif Friend in rules.get(Ash):
    print ("GG")

else:
    print("Fuck sake")

