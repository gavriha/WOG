import random


def play(diff):
    diff2=int(diff)*10
    secret=generate_number(diff2)
    print (f'secret is {secret}')
    i=0
    while i < 10:
        a = get_guess_from_user()
        if compare_results(a, secret):
            print (f'SUCCESS  in {i+1}  tries')
            return True
        else:
            print (f'WRONG you have {9-i} tries left')
        i=i+1
    return False


def generate_number(diff2):
    a= random.randint(1,diff2)
    print (f'random is {a}')
    return a

def get_guess_from_user():
    b = int(input ('guess the number:'))
    return b

def compare_results (guess, secret):
    if guess == secret:
        return True
    else:
        return False
