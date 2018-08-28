import random
# version 0.2

choose = {1: "Rock", 2: "Paper", 3: "Scissors"}

# sets win condition
win_set = {1: 3, 2: 1, 3: 2}

user = input("Select 1 for  rock : ")
com = random.randint(1, 3)

# checks is number and between 1 and 3
def check_entry(n):
    if n.isdigit():
        user = int(n)
        if user in range(1,4):
            return user
        else:
            print("Only choose between 1 and 3")
    else:
        print("please enter number")


def ai_selection():
    ai_result = random.randint(1,3)
    return ai_result

user_selection = check_entry(user)
ai_select = ai_selection()


def win_Cat(u,c):
    if u == c:
        print("Its a draw")
    elif c == win_set[user_selection]:
        print("Well done, you win. \nI do like the " + choose[user_selection] + " myself")
    else:
        print("Opps the phone won")

print("You Selected " + choose[user_selection] + ", the computer selected " + choose[ai_select])

win_Cat(user_selection,ai_select)





