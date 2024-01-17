# Date : 16,Jan,2024

'''
Given the names and grades for each student in a class 
of N students, store them in a nested list and print the name(s)
 of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest 
grade, order their names alphabetically and print each name on a new line.

Explanation 0 :
There are 5 students in this class whose names and grades are 
assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], 
['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.21 belongs to Tina. The second lowest grade of 37.21 
belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

'''

a=[]
z=[]
e=[]
b=int(input("Enter number of student :"))
for i in range(b):
    a1=input("Enter name :")
    b1=eval(input("Enter marks :"))
    a.append([a1,b1])
    z.append(b1)
a.sort()
z=list(set(z))
z.remove(min(z))
for j in a:
    if j[1]==min(z):
        print(j[0])