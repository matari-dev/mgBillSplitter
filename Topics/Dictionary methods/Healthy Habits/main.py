# the list "walks" is already defined
# your code here

num_days = len(walks)  # number of days

# a list is made of
# just the distances walked by using a
# list comprehension
distances = [walks[day]['distance'] for day in range(num_days)]
total_distance = sum(distances)  # add up all the distances together

print(total_distance // num_days)
