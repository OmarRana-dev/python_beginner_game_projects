# >>>>>Quiz Game>>>>>>>

print("Welcome to the Game")
play=input("Do you want to play Game? ")
if play.lower() == 'yes':
    print("lets go to the Game :)")
elif play.lower() == "no":
    print("Ok! as you wish")
    quit()
    
Score_Gain=0


x = """
What Dose CUP stand for?
    
    1: Center process unity
    2: Central Permition Unit
    3: Central Processing Unit
"""
print(x)
ans=input("Enter: ")
if ans.lower() == "central processing unit":
    Score_Gain += 10
    print("Correct!")
else:
    print("InCorrect!")

x="""
Is Omar Handsome?
     
    1: Yes
    2: No
"""
print(x)
ans=input("Enter: ")
if ans.lower() == "yes":
    Score_Gain += 10
    print("Correct!")
else:
    print("InCorrect!")

x="""
When was Omar born?
    
    1: 2000
    2: 2003
    3: 1998
"""
print(x)
ans=input("Enter: ")
if ans == "2003":
    Score_Gain += 10
    print("Correct!")
else:
    print("InCorrect!")
    
x="""
Who is the Founder of Pakistan!

    1: Alama Iqbal
    2: Engraz
    3: Qaid e Azam 
"""
print(x)
ans=input("Enter: ")
if ans.lower() == "engraz":
    Score_Gain += 10
    print("Correct!")
else:
    print("InCorrect!")
    
x="""
Which Year Imran Khan Won the Elition?
    
    1: 2018
    2: 2013 
    3: 2009
"""
print(x)
ans=input("Enter: ")
if ans.lower() == "2018":
    Score_Gain += 10
    print("Correct!\n")
else:
    print("InCorrect!\n")
    
if Score_Gain >= 30:
    print("Congratulations You WON the Game! ")
else:
    print("Please Try Again!")
print(f"You Gain {Score_Gain} Score out of 50!")

if Score_Gain >= 30:
    print("YOU WON!")
else:
    print("YOU LOSE!")
