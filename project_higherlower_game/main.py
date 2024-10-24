from game_data import data
from art import vs_art
from art import logo

score = 0
for i in range(0,5):
    print(logo)
    y = i + 1

    print(f"Compare A : {data[i]["name"]}, a {data[i]["description"]} , from {data[i]["country"]}")
    print(vs_art)
    print(f"Against B : {data[y]["name"]}, a {data[y]["description"]} , from {data[y]["country"]}")
    value = input("who has more followers Type a or b\n")
    if value == "a":
        if data[i]["follower_count"] > data[y]["follower_count"]:
            score = score + 1
            print(f"you are right , current score : {score}")
        else:
            print(f"sorry you are wrong , final score : {score}")
            break
    elif value == "b":
        if data[y]["follower_count"] > data[i]["follower_count"]:
            score = score + 1
            print(f"you are right , current score : {score}")
        else:
            print(f"sorry you are wrong , final score : {score}")
            break







