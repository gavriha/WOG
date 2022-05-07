from forex_python.converter import CurrencyRates
import random


def get_money_interval(amt : int, diff: int):
    c = CurrencyRates()
    rate = c.get_rate('ILS', 'USD')
    # print ("rate", rate)
    low = round((amt / rate) - (5-int(diff)))
    high = round((amt / rate) + (5-int(diff)))
    return low, high


def get_guess_from_user():
    amount = random.randint(1, 100)
    print (f'please guess how much is ${amount} in Israeli Shekels')
    valid = False
    while valid == False:
        try:
            guess = int (input ('enter your guess :'))
            valid = True
        except ValueError:
            print("please enter a number")
    return amount, guess




def play(diff:int):
    amount, guess = get_guess_from_user()
    low, high = get_money_interval(amount, diff)
    if int(low) <= int(guess) <= int(high):
        print (f'success!  the range was {low} - {high} and you made it')
        return True
    else:
        print(f'OOPS!  the range was {low} - {high} and you missed it')
        return False

