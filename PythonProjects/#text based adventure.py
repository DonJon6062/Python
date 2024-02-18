#text based adventure
    #you're getting a head

#introductions must be had
print("It is a nice day, judging by the feeling of the sun on your skin. ")
print("You open your eyes, or you would. You don't have a head! ")
print("1. Stumble out of bed looking for one. ")
print("2. Keep laying down. How would you even find one without eyes? ")

while True:
    # if/else 1/3
    choiceOne = input("What will you do? (1 or 2): ")
        #if the user does this, it's one path
    if choiceOne == '1':
        print("You stumble around, trip, and eventually feel what may be a doorway! ")
        print("1. Are you even decent? Look for clothes, or something to protect yourself with. Anything other than just /going out unprepared/. ")
        print("2. You don't have a head! How you look is important when you can /see/! Go out to find a head, quickly! ")
        
        #choice
        choiceUn = input("What now? Is there time to prepare, or will you /head/ out? (1 or 2): ")
        #prepare
        if choiceUn == '1':
                print("Fumbling about more, you ram your foot into something hard. It is a box. ")
                print("The items inside are heavy. You can only really carry one and remember where it is. ")
                print("'Cause all you have is touch to lead you. You can't even smell it. Or taste it. It's all up to memory. ") 
                print("1. The hollow metal thing seems useful. ")
                print("2. The thick wooden thing is probably good. ")
                print("3. The heavy cloth with something inside, please! ")
                #choice within a choice; broom(weapon), pot(stealth) and sack of potatoes(friendship)
                choiceUnPtOne = input("What do you take? (1, 2 or 3): ")
        
                #choice-ception
                #pot get!
                if choiceUnPtOne == '1':
                    print("You grab it and put it on your neck, as once more, no head. ")
                    print("It's not very big, but it has a top, so maybe attackers will aim for what they think has a head. ")
                    print("Or they won't. But now is not the time for pessimism. Pessimism is for when you have a mind to feel negative. ")
                    print("And thus, you retrace your steps to the exit, and begin the search for your head. ")
        
                #broom get!
                elif choiceUnPtOne == '2':
                    print("Giving it a few swings, you're fairly certain that if someone approaches you can scare them off. ")
                    print("Swinging like a madman and all. 'Cause you can't see them and can only flail, hoping to hit /something/. ")
                    print("Only if they wack you first of course. You can't hear them. ")
                    print("And thus, you retrace your steps to the exit, and begin the search for your head. ")
        
                #potato sack get!
                elif choiceUnPtOne == '3':
                    print("The hefty item has what feels like multiple smaller items making up the weight. ")
                    print("The oblong items are grainy. Did you have a bag of stones? You can't remember much, with your hippocampus detatched. ")
                    print("You hope they're stones. Or. Something. Something useful. Please let this be useful. ")
                    print("And thus, you retrace your steps to the exit, and begin the search for your head. ")

        #rush
        elif choiceUn == '2':
            print("With urgency, you push open the door. ")
            print("There's no time for prep! You need to find your head, quickly! ")
        
        #catchall
        else:
            print("Please, the number keys! ")

        #choose your path
        print("Without a brain, you can't remember where.. anything is. Welp, the only way is forward. ")
        choiceUnPtTwo = input("Where is forward? (N, NW or NE) (please use caps lock): ")
        
        #farm(pumpkin)
        if choiceUnPtTwo == "N":
            print("After a bit of walking, you feel vines around your feet, and moist soil. ")
            print("Using your hand to trail up one of the vines, you feel a hard surface. ")
            print("A pumpkin! Placing it on your lead leads you to realize; no eyeholes, but you can hear, at least. ")
    
        #forest(hive)
        elif choiceUnPtTwo == "NW":
            print("Soon enough, dried leaves crunch around you, and the occasional patch of grass tickles your ankle. ")
            print("You trip over a root, and ram into a tree trunk. HARD. ")
            print("Something falls on your head! You can see! ")
            print("The bugs whose hive is on your neck don't seem as happy.. ")
        #pond(bucket)
        elif choiceUnPtTwo == "NE":
            print("The unmistakable feeling of mud sticks to the soles of your feet. ")
            print("Suddenly, you step right in something cold and.. mettalic? ")
            print("Aside from adjusting your vision for the many, many holes in the bucket, this is a great head! ")
            print("Whoever had that probably didn't need it anywhoo. This'll do, for now! ")

        else:
            print("Please. It's spelled out for you! ")
        

        #another path
    elif choiceOne == '2':
        print("What will you do then, rot? You can't do anything with that mindset! ")
        print("I suppose if you wish to give up, I can't stop you. ")
        print("You coward. Go to bed. Stay headless, and spineless. ")

        #the catchall
    else: 
        print("You know the number keys, right? At the top of the keyboard? ")
        print("Press one of the ones listed! ")

    #ask user to play again
    playAgain = input("Play Again? (Y or N?) ")

    #go back
    if playAgain == 'Y':
        print("It is a nice day, judging by the feeling of the sun on your skin. ")
        print("You open your eyes, or you would. You don't have a head! ")
        print("1. Stumble out of bed looking for one. ")
        print("2. Keep laying down. How would you even find one without eyes? ")
        continue

    #end game
    elif playAgain == 'N':
        print("Thanks for playing! ")
        break

    #catchall
    else:
        print("Please type one of those nifty letters in the parenthases! ")