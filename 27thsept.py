# theString = "berfynkaia"
# print(len(theString))
# print(theString[0:4])
# print(theString[-4:])
# print(theString[0:4] , theString[-4:])
# reverso = theString[10::-1] #or [::-1]
# print(reverso)


x = input("Create a password: ")
y = x.isalpha()

if y is True:
  print("That's a valid password.")
else:
  print("Use the alphabet. Try again.")




name = input("enter your name: ")
def greet(name):
  print(f"Hello, {name}. I hope you are doing well.") 
greet(name)





age = input("enter your age: ")
age = int(age)

def calculate(age):
  userAge = (2023 - age)
  print(f"You were born in {userAge}.")
calculate(age)
