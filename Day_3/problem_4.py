# Date : 18,Jan,2024

'''
Sample Input :
1222311

Sample Output :
(1, 1) (3, 2) (1, 3) (2, 1)

Explanation :
First, the character 1 occurs only once. It is replaced by (1,1) . Then the character 2 
occurs three times, and it is replaced by (3,2) and so on.
Also, note the single space within each compression and between the compressions.
'''

from itertools import groupby

def compress_string(s):
    # Use groupby to group consecutive occurrences of characters
    grouped_characters = [(len(list(group)), int(key)) for key, group in groupby(s)]

    # Print the compressed string format
    result = ' '.join(f'({count}, {char})' for count, char in grouped_characters)
    return result

# Input
input_string = input('Enter a string: ')

# Output compressed string
output_string = compress_string(input_string)
print(output_string)