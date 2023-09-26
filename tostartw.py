x = input("give me a num: ")
y = input("give me another num: ")
z = input("give me one last num: ")

x = int(x)
y = int(y)
z = int(z)

a = [ ]

if (x % 2) == 0:
    a.append(x)


if (y % 2) == 0:
    a.append(y)



if (z % 2) == 0:
     a.append(z)

b = sum(a)

if b > 0:
  print("I added only the even numbers. Surprise solution is: ", b)
else: 
  print("The numbers were not even.")

