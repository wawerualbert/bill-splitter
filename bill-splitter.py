# write your code here
import random
friends = dict()
user_input = int(input("Enter the number of friends joining (including you): "))

if user_input < 1:
    print()
    print("No one is joining for the party")
else:
    print()
    print("Enter the name of every friend (including you),each on a new line:")
    for _ in range(user_input):
        name = input()
        friends[name] = 0
    print("Enter the total bill value: ")
    value = int(input())
    bill = round(value / user_input, 2)
    friends.update({name: bill for name in friends})
    print("Do you want to use the \"Who is lucky\"? feature? Write Yes/No:")
    lucky = input()
    if lucky == "Yes":
        lucky_friend = random.choice(list(friends))
        print(f"{lucky_friend} is the lucky one!")
        new_bill = round(value / (user_input -1), 2)
        friends.update({name: (new_bill if name != lucky_friend else 0) for name in friends.keys()})
    else:
        print("No one is going to be lucky")
    print(friends)
    
