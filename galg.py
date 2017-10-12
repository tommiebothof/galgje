import random
print ("welkom bij galgje")
fletter = ""
woord = ["game", "loop", "raar"]
gwoord = (random.choice(woord))
streep = ("_ _ _ _")
print (streep)
while True:
    letter1 = str(input("geef een letter"))
    if letter1 in gwoord:
        print("goed")
    elif len(letter1) >= 2:
        print("De letter is te lang, als je het hele woord wil invoeren vul dan ? in.")
    elif letter1 == "?":
        print("weet jij het woord")
        antwoord = str(input("typ het woord maar"))
        if antwoord != gwoord:
            print("helaas niet goed, probeer het opnieuw")
        elif antwoord == gwoord:
            print("goed gedaan")
            break
    elif letter1 != gwoord:
        counter +=1
        print ("niet goed")
        print ("dit zijn je foute letters:"+fletter)
