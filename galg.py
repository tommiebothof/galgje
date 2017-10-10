import random
woord = ["game", "loop", "raar"]
gwoord = (random.choice(woord))
streep = ("_ _ _ _")
print (streep)
while True:
    letter1 = str(input("geef een leter"))
    if letter1 in gwoord:
        print("goed")
    elif letter1 == "?":
        print("weet jij het woord")
        antwoord = str(input("typ het woord maar"))
        if antwoord == gwoord:
            print("goed gedaan")
            break
    elif letter1 != gwoord:
        print ("niet goed")
