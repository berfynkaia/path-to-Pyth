'''
x = 12, 13, "yep"
y = "tikitiki"
y = x
x = y
y = x
print(x)
print(y)
'''
'''
x = input("num: ")
y = float(x)
for i in y:
    print(y * 3)

    ##INTEGERS NOT ITERABLE
'''

# x = [1, 2, 3]
# y = input("num: ")
# print(x)
# z = int(y)

# '''for i in x:
#     print(y)'''

# for i in range(z):
#     print("yi")




'''If you create a variable named "x" and then use "for x in" in a for loop, you're essentially reassigning the variable "x" in each iteration of the loop. Here's an example to illustrate what happens:

```python
x = 10
for x in range(5):
    print(x)
```

In this code, you first initialize "x" with the value 10. Then, in the for loop, you reassign "x" to each value in the range from 0 to 4. The output will be:

```
0
1
2
3
4
```

As you can see, "x" is effectively being overwritten by the loop, and it takes on the values 0 through 4 during each iteration of the loop.

It's important to note that this usage can lead to confusion and is generally not recommended. It's usually better to use a different variable name for the loop variable to avoid potential naming conflicts and make your code more readable.'''



x = []

def addEvenNum():
    while True:
        num = input("Enter an even number: ")
        number = int(num)

        if number % 2 == 0:
            x.append(number)
            print(x)
            break
        else:
            print("The number is not even. Try again.")

addEvenNum()




