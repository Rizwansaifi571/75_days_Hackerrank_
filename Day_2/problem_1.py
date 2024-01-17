# Date : 17,Jan,2024

'''
The provided code stub will read in a dictionary containing 
key/value pairs of name:[marks] for a list of students. Print
the average of the marks array for the student name provided,
 showing 2 places after the decimal.

Sample Input 0:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 0:
56.00
'''

n = int(input('Enter number :'))
student_marks = {}
for i in range(n):
    name=input('Enter name :')
    marks=list(map(int,input("Enter marks :").split()))
    student_marks[name]=marks
query=input("enter query name :")
a=student_marks.get(query)
result1=sum(a)/len(a)           #sum(a) buildin function take all iterable sum
result=result1
print(f"{result:.2f}")


'''                   or                       '''

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()      # take 'Krishna 67 68 69' as a single input.
    marks = list(map(float, line))
    student_marks[name] = marks
query = input()
a=student_marks.get(query)
result1=sum(a)/len(a)
result=result1
print(f"{result:.2f}")