import random
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
game_images = [rock, paper, scissors]
choice = int(input("What do you choose? 0 for rock, 1 for paper, 2 for scissor\n"))
if choice>=3 or choice<0:
    print("You Typed an invalid number, Computer Wins")
else:
    print(game_images[choice])
    
        

comp = random.randint(0, 2)
       
print(f"Computer chose\n {comp}")
print(game_images[comp])
if comp == choice:
    print("Game tied")
elif comp == 0:
    if choice == 1:
        print("You Win")
    elif choice == 2:
        print("Computer win")    
    
elif comp == 1:
    if choice==0:
        print("Computer win")
    elif choice == 2:
        print("You Win")

elif comp==2:
    if choice==0:
        print("You Win")
    else:
        print("Computer win")    



