import random

# your sentence is assigned to the variable
sentence = input().split()

# write your python code below
seed_number = 43
random.seed(seed_number)
random.shuffle(sentence)

# shows the message
print(' '.join(sentence))
