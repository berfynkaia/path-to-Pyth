
name = input("Enter your name: ")
print("Your password should be composed of all numbers expressed in 4 digits.")
password = input("Enter your password: ")
y = password.isalnum()

if (y == True) and (len(password) == 4):
    print("Great.")
else:
    print("not going to work.")
age = (input("Your age: "))
z = age.isalnum()
if (z == True) and (int(age) >= 18):
    print("You are old enough to be a member.")
else:
    print("Check your input.")
user = [name, password, age]
print(f"You are {name}. Your password is ****, and you are {age} years old.")



    


