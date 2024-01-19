# Date : 19, Jan, 2024

'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines 
of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.

'''

n=int(input('time :'))
i=0
lis1=[]
while i<n:
    i+=1
    inp=input('Enter :').split()
    if len(inp)==1:
        op=inp[0]
        if op=='sort':
            lis1.sort()
        elif op=='print':
            print(lis1)
        elif op=='append':
            lis1.pop()
        elif op=='reverse':
            lis1.reverse()
        elif op=='pop':
            lis1.pop()
    
    elif len(inp)==2:
        op=inp[0]
        val=int(inp[1])
        if op=='append':
            lis1.append(val)
        elif op=='remove':
            lis1.remove(val)