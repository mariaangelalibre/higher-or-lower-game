import data as d
import logo
import random

i = 1
score = 0

while i != 0 :
    data_value = d.data
    value_a = random.choice(data_value)
    followers_a = value_a['follower_count']

    data_value = d.data
    value_b = random.choice(data_value)
    followers_b = value_b['follower_count']

    if followers_a > followers_b:
        answer = "A"
    else:
        answer = "B"

    print(logo.logo)
    if score > 0:
        print("You're right! Current score:",score)
        
    print("Compare A:", value_a['name'],",a", value_a['description'],",from", value_a['country'],".", value_a['follower_count'])
    print(logo.vs)
    print("Against B:", value_b['name'],",a", value_b['description'],",from", value_b['country'],".", value_b['follower_count'])

    answer_input = input("Who has more followers? Type 'A' or 'B':").upper()
    if answer == answer_input:
        score += 1
        
    else:
        i = 0

else:
    print(logo.logo)
    print("Sorry, that's wrong. Final score:", score)