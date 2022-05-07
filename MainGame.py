import Live as L
import GuessGame2 as G
import MemoryGame as M
import CurrencyRouletteGame as C


username = input("Enter username:")
# print("Username is: " + username)
L.welcome(username)

game, diff = L.load()

if game == "1":
    c = G.play(diff)
    if c:
        print ("you won the guessing game")
    else:
        print ("you lost the guessing game")
elif game == "2":
    c = M.play(diff)
    if c:
        print ("you won the Memory game")
    else:
        print ("you lost the Memory game")
elif game == "3":
    c = C.play(diff)
    if c:
        print ("you won the Exchange game")
    else:
        print ("you lost the Exchange game")
