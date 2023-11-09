x = [1, 3, 9, 12, 5, 18, 10, 7, 6]
search = [ ]
for num in x:
    if num % 3 == 0:
        continue
    search.append(num)
print(search)




names = ["John", "Alice", "Bob", "Anna", "Eve"]
initial = "A"

for name in names:
    if name.startswith(initial):
        print(name)
        break


# name, i, item, num