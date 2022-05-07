'''
1. generate_sequence - Will generate a list of random numbers between 1 to 101. The list
length will be difficulty.
2. get_list_from_user - Will return a list of numbers prompted from the user. The list length
will be in the size of difficulty.
3. is_list_equal - A function to compare two lists if they are equal. The function will return
True / False.
4. play - Will call the functions above and play the game. Will return True / False if the user
lost or won
'''
import random
from random import randint
from os import system
import time

# for temp_print to run it needs to be executed from CMD!
# as a workaround for running from pycharm the program prints 20 empty lines
def temp_print(val: str):
    print(val)
    time.sleep(0.7)
    system('cls')
    for i in range (20):
        print (" ")

def generate_sequence(diff):
    arr = []
    for i in range (int(diff)):
        arr.append (random.randint(1, 101))
    temp_print (arr)
    return arr

def get_list_from_user(diff):
    inp = []
    print (f'please type {(int(diff))} numbers')
    for i in range (int(diff)):
        v= get_guess_from_user(i)
        inp.append (v)
        # inp.append (int(input (f'element {i}: ')))
    return inp

def is_list_equal(rand_list, user_list):
    if rand_list == user_list:
        return True
    else:
        return False

def play(diff):
    rand_list = generate_sequence(diff)
    user_list = get_list_from_user(diff)
    result = is_list_equal(rand_list,user_list)
    # print (result)
    return result

# play (2)

def get_guess_from_user(i):
    valid = False
    while valid == False:
            try:
                b = int(input (f'type element {i+1} :'))
                valid = True
            except ValueError:
                print ("please type a number")
    return b




'''
a = generate_sequence(2)
print (a)

b = get_list_from_user(2)
print (b)

c = is_list_equal(a,b)
print (c)
'''