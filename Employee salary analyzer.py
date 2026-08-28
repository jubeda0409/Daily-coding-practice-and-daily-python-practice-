salaries = []
for i in range(10):
    salary = int(input("Enter salary: "))
    salaries.append(salary)
print("Original salaries:", salaries)
total = 0

for salary in salaries:
    total += salary

print("Total salary:", total)
average = total / len(salaries)

print("Average salary:", average)
highest = salaries[0]

for salary in salaries:
    if salary > highest:
        highest = salary

print("Highest salary:", highest)
lowest = salaries[0]

for salary in salaries:
    if salary < lowest:
        lowest = salary

print("Lowest salary:", lowest)
above_average = []

for salary in salaries:
    if salary > average:
        above_average.append(salary)

print("Salaries greater than average:", above_average)
below_average = []

for salary in salaries:
    if salary < average:
        above_average.append(salary)
    print("salries greater then average:",above_average)
below_average=[]
for salary in salaries:
    if salary<average:
        below_average.append(salary)
print("salaries less than average:",below_average)
print("total:",total)
print("average:",average)
print("highest:",highest)
print("lowest:",lowest)
