import random


def guess(diff):
    diff2=int(diff)*10
    secret=generate_number(diff2)
    print (f'secret is {secret}')
    i=0
    while i < 10:
        a = int(input ('guess the number:'))
        if a == secret:
            print (f'SUCCESS  in {i+1}  tries')
            return
        else:
            print (f'WRONG you have {9-i} tries left')
        i=i+1


def generate_number(diff2):
    a= random.randint(1,diff2)
    print (f'random is {a}')
    return a

def get_guess_from_user():
    b=  int(input ('guess the number:'))
    return b