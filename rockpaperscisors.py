import random
print(    " welcome to rock paper scissors game   ")
user_socre = 0
comp_score = 0
ties = 0
name = input("enter your name : ")

print("""
WINNING RULES : 
1. Paper vs Rock --> paper
2. Rock vc Scissors --> Rock
3. Scissors vc Paper --> Scissors """)

print(""" choices are  :
1. Rock
2. Paper
3. Scissors """ )
print()
choice = int(input("enter your choice 1/2/3 :  "))
print()
while choice > 3 or choice < 1 :
    choice = int(input("enter valid input"))
if choice == 1:
    user_choice = "Rock"
elif choice == 2:
    user_choice = "Paper"
else:
    user_choice = "Scissors"

print("The user's choice is : " , user_choice)
print("Now it is computer's turn ")
computer = random.randint(1,3)
if computer == 1:
    comp_choice = "Rock"
elif computer ==2:
    comp_choice = "Paper"
else:
    comp_choice = "Scissors"
    print("the computer's choice is : ",comp_choice)
if((user_choice == "Paper" and comp_choice == "Rock") or (user_choice =="Rock" and comp_choice == "Paper") ):
    print("Paper wins ")
    result = "Paper"
elif((user_choice == "Scissors" and comp_choice == "Rock") or (user_choice =="Rock" and comp_choice == "Scissors") ):
    print("Rock wins ")
    result = "Rock"
elif(user_choice == comp_choice):
    print("It's a Tie")
    result = "Tie"
else:
    print("Scissors wins ")
    result = "Scissors"
if result == "Tie":
        Tie +=1
elif result == user_choice:
    print("user wins ")
    user_socre +=1
else :
    print("computer wins ")
    comp_score +=1
print("scores are")
print(name, "s score is" ,user_socre)
print("computer's score is" ,comp_score)
print("ties are", ties)