def welcome(name):
    print (f'Hello { name } and welcome to the World of Games(WoG).')
    print("Here you can find many cool games to play.")

# welcome('gh')

def load():

    print ('please choose a game to play: ')
    print ('   1. Guess game')
    print ('   2. Memory game')
    print ('   3. Currency Roullete')

    x=0
    while x not in ["1", "2", "3"]:
        x = input('Enter your choice: ')

    y=0
    while y not in ["1","2","3","4","5"]:
        y = input('Please choose difficulty Level (1-5): ')

    # print (f'game- {x}  and diff level- {y}')
    return x, y



