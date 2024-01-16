#Date : 16,Jan,2024

'''
Ques: Given the participants' score sheet for your 
University Sports Day, you are required to find the 
runner-up score. You are given  scores. Store them in a 
list and find the score of the runner-up.

Sample Input 0 :
5
2 3 6 6 5

Sample Output 0 :
5

Explanation 0 :
Given list is [2,3,6,6,5] . The maximum score is 6, second maximum is 5 .
Hence, we print 5 as the runner-up score.
'''

n=int(input("Enter number of participant :"))
a=list(map(int,input("Enter score :").split()))
a.sort()
m=list(set(a))
print(f'The second runner up score is : {a[-2]}')

