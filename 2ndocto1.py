# dictionary 

students = {
  '123' : {
    'name' : 'mark',
    'surname' : 'johnson',
    'phone' : '2345'
  },
  '124' : {
    'name' : 'sue',
    'surname' : 'johnson',
    'phone' : '2346'
  }
}

x = input("Enter your student id: ")
y = input("Enter your name: ")
students[x] = y
z = input("Enter your surname: ")
students['surname'] = z
p = input("Enter your number: ")
students['phone'] = p


print(students)

q = input("Enter the id you want to search: ")
finito = students.get(q)


print(finito)