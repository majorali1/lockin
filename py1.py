import random
print("an apple fell on the princesses head")
print("The kingdom of Kinskonskuans assigned you the hero of this world a mission to save the princess")
print("KiNSKOnSKUans GAME game game game.")
print("tutorial timee!!!")

tries = 0
range1 = int(input("whats the lower num? "))
range2 = int(input("whats the higher num? "))
randomnum = random.randint(range1,range2)


while True:
    try:
        answer = int(input("\n game time!, what is the chosen num?: "))
        tries += 1 
        if answer > randomnum:
            print("\n wrong!!, your guess was higher")
        if answer < randomnum:
            print("\n wrong!!, your guess was lower")
        if answer == randomnum:
            print("\n Correct!, {} was the right number it took {} tries".format(randomnum,tries))
            break

    except ValueError:
        print("NOPE")
print("kiyaaaaaaahhhh")
print("i am useful at being useless")
print("HAHAHHA ZZA WWAAAARRDOOOO *bushhwhhshshhsdh*")