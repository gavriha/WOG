import random


def play(diff):
    diff2=int(diff)*10
    print (f'guess a number between 1 and {diff2}, good luck!')
    secret=generate_number(diff2)
    # print (f'secret is {secret}')
    i=0
    while i < 10:
        a = get_guess_from_user()
        comp = compare_results(a, secret)
        if comp == "Win":
            print (f'SUCCESS  in {i+1}  tries')
            return True
        elif comp == "Higher":
            print (f'WRONG you have {9-i} tries left - Go higher')
        else:
            print(f'WRONG you have {9 - i} tries left - Go lower')
        i=i+1
    return False


def generate_number(diff2):
    a= random.randint(1,diff2)
    # print (f'random is {a}')
    return a

def get_guess_from_user():
    valid = False
    while valid == False:
            try:
                b = int(input ('guess the number:'))
                valid = True
            except ValueError:
                print ("please enter a number")
    return b

def compare_results (guess, secret):
    if guess == secret:
        return "Win"
    elif guess < secret:
        return "Higher"
    else:
        return "Lower"
