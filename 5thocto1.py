# nums = []
# for i in range(5):
#   add_input = input("Enter a number: ")
#   b= int(add_input)
#   nums.append(b)
# def calculate_avarage():
#   x = sum(nums)
#   print(x / 5)
# calculate_avarage()


numbers = []
for i in range (5):
  x = input("Enter a number: ")
  y = int(x)
  numbers.append(y)
def find_max_min():
  for i in numbers:
    numbers.sort()
    print("Maximum number is: ", numbers[-1], "Minimum number is: ", numbers[0])
find_max_min()


