import random 

x="""
Which Game Level would you like to Play?
     
    Easy
    Medium
    Hard
    Extra Hard
"""
print(x)
z=input("Enter: " )
i = 0

if z.lower() == "easy":
    print("\nWrite any number between 1 and 10\n")
    while i <= 9:
        guess=input("Make a guess: ")
        if guess.isdigit():
            guess=int(guess)
            if guess <= 10:
                random_number=random.randrange(0, 11)
                x = random_number
            else:
                print("Please Write number between 1 and 10\n")
                continue
            print(f"The Correct Number is {x}")
            Score=0
            if x == guess:
                print("Congratulation!\n")
                Score += 1
                i += 1
            else:
                i += 1
                if guess > x:
                    print("You were above the number!")
                    print("Try Again!\n")
                else:
                    print("You were below the number!")
                    print("Try Again!\n")
                
            while i == 10:
                if Score >= 6:
                    print(f"You Gain {Score} Score out of 10!")
                    print("YOU WON!\n")
                    i += 1
                else:
                    print(f"You Gain {Score} Score out of 10!")
                    print("YOU LOSE!\n")
                    i += 1
        else:
            print("Please Enter a Number\n")   
            continue

    
    
if z.lower()=="medium":
    print("\nWrite any number between 1 and 30\n")
    while i <= 9:
        guess=input("Make a guess: ")
        if guess.isdigit():
            guess=int(guess)
            if guess <= 30:
                random_number=random.randrange(0, 31)
                x = random_number
            else:
                print("Please Write number between 1 and 30\n")
                continue
            print(f"The Correct Number is {x}")
            Score=0
            if x == guess:
                print("Congratulation!\n")
                Score += 1
                i += 1
            else:
                print("Try Again!\n")
                i += 1
                
            while i == 10:
                if Score >= 6:
                    print(f"You Gain {Score} Score out of 10!")
                    print("YOU WON!\n")
                    i += 1
                else:
                    print(f"You Gain {Score} Score out of 10!")
                    print("YOU LOSE!\n")
                    i += 1
            
        else:
            print("Please Enter a Number\n")   
            continue
    

    
if z.lower()=="hard":
    print("\nWrite any number between 1 and 50\n")
    while i <= 9:
        guess=input("Make a guess: ")
        if guess.isdigit():
            guess=int(guess)
            if guess <= 50:
                random_number=random.randrange(0, 51)
                x = random_number
            else:
                print("Please Write number between 1 and 50\n")
                continue
            print(f"The Correct Number is {x}")
            Score=0
            if x == guess:
                print("Congratulation!\n")
                Score += 1
                i += 1
            else:
                print("Try Again!\n")
                i += 1
            
            while i == 10:
                if Score >= 6:
                    print(f"You Gain {Score} Score out of 10!")
                    print("YOU WON!\n")
                    i += 1
                else:
                    print(f"You Gain {Score} Score out of 10!")
                    print("YOU LOSE!\n")
                    i += 1
                        
        else:
            print("Please Enter a Number\n")   
            continue
    
            

# print(f"You Gain {Score} Score out of 10!")

if z.lower()=="extra hard":
    print("\nWrite any number between 1 and 100\n")
    while i <= 9:
        guess=input("Make a guess: ")
        if guess.isdigit():
            guess=int(guess)
            if guess <= 100:
                random_number=random.randrange(0, 101)
                x = random_number
            else:
                print("Please Write number between 1 and 100\n")
                continue
            print(f"The Correct Number is {x}")
            Score=0
            if x == guess:
                print("Congratulation!\n")
                Score += 1
                i += 1
            else:
                print("Try Again!\n")
                i += 1
            
            while i == 10:
                if Score >= 6:
                    print(f"You Gain {Score} Score out of 10!")
                    print("YOU WON!\n")
                    i += 1
                else:
                    print(f"You Gain {Score} Score out of 10!")
                    print("YOU LOSE!\n")
                    i += 1    
                
        else:
            print("Please Enter a Number\n")   
            continue
            
    
