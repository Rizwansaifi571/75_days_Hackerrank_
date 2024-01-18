# Date : 18,Jan,2024

'''
When users post an update on social media,such as a URL, image, status 
update etc., other users in their network are able to view this new post on 
their news feed. Users can also see exactly when the post was published, i.e, 
how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can 
be confusing. You are given two timestamps of one such post that a user 
can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
'''

from datetime import datetime, timedelta

# Function to convert timestamp to seconds
def timestamp_to_seconds(timestamp):
    dt = datetime.strptime(timestamp, "%a %d %b %Y %H:%M:%S %z")
    return int(dt.timestamp())

# Function to calculate absolute difference in seconds
def calculate_time_difference(timestamp1, timestamp2):
    seconds1 = timestamp_to_seconds(timestamp1)
    seconds2 = timestamp_to_seconds(timestamp2)
    return abs(seconds1 - seconds2)

# Input number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Input timestamps
    timestamp1 = input().strip()
    timestamp2 = input().strip()

    # Calculate and print the absolute difference in seconds
    result = calculate_time_difference(timestamp1, timestamp2)
    print(result)
