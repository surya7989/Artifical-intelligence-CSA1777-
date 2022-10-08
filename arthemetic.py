def add(x,y):
  return x+y
def subtract(x,y):
   return x-y
def multiply(x,y):
   return x*y
def divide(x,y):
  return x/y
print("1.addition")
print("2.subtract")
print("3.multiplication")
print("4.division")

while True:
  choice=(input("enter your choice(1,2,3,4)\n"))
  if choice in ('1', '2', '3', '4'):
     num1=float(input("enter the number:"))
     num2=float(input("enter number2 :"))
                      
     if choice=='1':
          print(num1,"+",num2,"=",add(num1,num2));
     elif choice=='2':
          print(num1,"-",num2,"=",subtract(num1,num2))
     elif choice=='3':
          print(num1,"*",num2,"=",multiply(num1,num2))
     elif choice=='4':
          print(num1,"/",num2,"=",divide(num1,num2))
     next_calculation=str(input("enter yes/no for next calculation:"))
     if next_calculation=="no":
         break
     else:
           print("Invalid input")
