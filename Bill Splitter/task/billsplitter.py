import random

print("Enter the number of friends joining (including you):")
num_friends = int(input())  # num_friends = number of friends
if num_friends < 1:
    print("No one is joining for the party")
else:
    # variable to store our friends names which
    # will become the keys to our dictionary of friends
    names = []

    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        names.append(input())

    friends = dict.fromkeys(names, 0.0)

    print("Enter the total bill value:")
    bill = float(input())
    one_share = round((bill / num_friends), 2)  # one_share = one share of the bill

    # using the `names` list again to
    # iterate through each friend in the dictionary and
    # assign each their one share of the bill
    for name in names:
        friends[name] = one_share

    possible_answers = ['Yes', 'No']
    lucky = ""
    while lucky not in possible_answers:
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        lucky = input()
    if lucky == 'Yes':
        lucky_person = random.choice(names)
        print(f'{lucky_person} is the lucky one!')
        one_share = round((bill / (num_friends - 1)), 2)
        for name in names:
            if name == lucky_person:
                friends[name] = 0
            else:
                friends[name] = one_share
        print(friends)
    else:
        print('No one is going to be lucky')
        print(friends)
