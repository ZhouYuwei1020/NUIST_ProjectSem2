x=int(input("enter a number for its factorial:"))
y=int(1)
res=int(1)
while(x>1):
  y=x-1
  res= res*x
  x=y
print("the factorial is:")
print(res)
