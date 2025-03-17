import random
print("Let's play a guess number game,please enter a number between 10 and 20")

x=random.randint(10,20)
y=int(input("please enter a number:"))
while x!=y: 
  print("not right,try again")
  y=int(input("please enter a number:"))
print("congratulations!!")
    
