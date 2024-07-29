rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors : "))
if choice==0:
  print(rock)
elif choice==1:
  print(paper)
else:
  print(scissors)
print("Computer chose : \n")
comp_choice=random.randint(0,2)
if comp_choice==0:
  print(rock)
elif comp_choice==1:
  print(paper)
else:
  print(scissors)
if (choice==0 and comp_choice==1) or(choice==1 and comp_choice==2):
  print("You lose")
elif (choice==2 and comp_choice==1) or(choice==0 and comp_choice==2):
  print("You Win")
elif (choice==1 and comp_choice==0):
  print("You Win")
elif (choice==2 and comp_choice==0):
  print("You lose")  
else :
  print("Try Again")
