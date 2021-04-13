import random
import math

def game():
   
    print("what is your name?")
    name=input("")
    number=random.randrange(1,50)
    username="Welcome {} to the random number game"
    print(username.format(name),"\n let'ts start")
    
    i=0
    r=1

    while i <7 :# user has 6 chance 
        guess = int(input("Please enter your guess: "))
        if guess<number:
            print("you have choose low number \n")
            print("you have only "+ str(6-i) + "chances left")
            i += 1
    
        elif guess>number:
            print("you have choose high number \n")
            print("you have only "+ str(6-i) + "chances left")
            i += 1
        elif guess == number:
            print("\nCongratulations "+name+"!! You have guessed the correct number!")
        
            break
        else :
            print("better luck next time")
    else:
        print("Sorry you lost the game!!")
        print("My number was = " + str(number))
        
    
            
    
       
        
def main():
    game()
    while True:
        another_game = input("Do you wish to play again?(y/n): ")
        if another_game == "y":
            game()
        else:
            break
main()
print("\nEnd of the Game! Thank you for playing!")
