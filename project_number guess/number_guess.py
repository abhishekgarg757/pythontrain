import random
#from xml.sax.handler import property_interning_dict

print("welcome to a number guessing game ")
print("i am thinking of a number between 1 to 100")
list1 =[]
for i in range(0,101):
    list1.append(i)
level = input("choose a difficult level : easy or hard\n")
final_num = random.choice(list1)
print(final_num)
def game(attempts):
    for i in range(0,attempts):
        guess = int(input("make a guess\n"))
        if guess == final_num:
            print("you re right")
            break
        elif guess < final_num:
            attempts = attempts-1
            print("your guess is too low number")
            print(f"you have {attempts} attempts left")
            print("guess again")
        elif guess > final_num:
            attempts = attempts-1
            print("your guess is too high number")
            print(f"you have {attempts} attempts left")
            print("guess again")


if level == "easy":
    attempts = 10
    game(attempts)

else:
    attempts = 5
    game(attempts)







