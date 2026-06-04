import random
item=["Rock","Paper","Scissor"]
user_choice =input("choose yours: 1.Rock 2.Paper 3.Scissor : ")
comp_choice=random.choice(item)
print(f"user choice = {user_choice}  Computer choice ={comp_choice}")

if user_choice==comp_choice:
    print("its a tie!")
elif user_choice=="Rock":
    if comp_choice=="Paper":
     print("Paper Wins! ")
    else:
       print("Scissor Wins!")

elif user_choice=="Paper":
    if comp_choice=="Rock":
     print("Paper Wins!")
    else:
       print("Scissor Wins!") 


elif user_choice=="Scissor":
    if comp_choice=="Rock":
     print("Rock Wins!")
    else:
       print("Scissor Wins!")        
           
           

           



