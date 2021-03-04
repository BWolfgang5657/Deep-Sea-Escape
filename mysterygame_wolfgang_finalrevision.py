'''
Brandon Wolfgang
December 11, 2018


Deep Sea Escape
Trapped on the luxury cruise liner, The Deep Sea Escape, you and 12 others are forced into a killing game. If someone wants to leave, they have to kill someone, and get away with it.
Bring the culprit to light, and they will be punished. If the culprit gets away, the culprit lives and well, I'll leave that for later.
'''
import random, sys, time
global evidence, exploprecount, deckexplored, waterparkexplored, cabinsexplored
#https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
def slowtype(t,pause = 0): #defines the function slow_type of variable t
    for l in t: #for every letter in the inputted variaable
        sys.stdout.write(l) #for each letter in variable, print that letter
        time.sleep(.001) #.05
    time.sleep(.5+pause)
def slowtype1(t,pause = 0):
    for l in t:
        sys.stdout.write(l)
        time.sleep(.001) #.2
    time.sleep(.5+pause)
def fasttype(t,pause = 0):
    for l in t:
        sys.stdout.write(l)
        time.sleep(.001) #.02
    time.sleep(.5+pause)
def explorecheck(x):
    while str(x.lower()) not in ['cabins','water park','deck']:
        if explorecount == 0:
            slowtype("I don't think that is a place I can go.\n")
            x = input("\n\nWhere would you like to explore?\nDeck     Water Park     Cabins\n   -> ")
        elif explorecount == 1:
            slowtype("I don't think that's a place I can go.\n")
            if deckexplored == True:
                x = input("\n\nWhere would you like to explore?\nWater Park     Cabins\n   -> ")
            elif waterparkexplored == True:
                x = input("\n\nWhere would you like to explore?\nDeck     Cabins\n   -> ")
            elif cabinsexplored == True:
                x = input("\n\nWhere would you like to explore?\nDeck     Water Park\n   -> ")
def hearvoice(x):
    if str(x.lower()) == 'review evidence':
        print("You hear a voice in your head telling you to look up a few lines, as you will see the evidence again.")

def printevidence(x):
    if str(x.lower()) == 'review evidence':
        print("\nEvidence")
        print(evidence)
playthrough = 0
explorecount = 0
deckexplored = False
cabinsexplored = False
waterparkexplored = False
investigatecount = 0
tryinvestigateagain = 'yes'
waterslideavailable = 'no'
waterparkinvestigated = ['Lazy River', 'Water Slide', 'Normal pool']
waterparkinterrogate = ['Bruno Bucciarati','R. Renji','Josuke Higashikata','Speed Wagon']
giornoroominterrogate = ['Trish','Serranity','Eldniw']
giornoroominterrogatel = ['trish','serranity','eldniw']
trishinterrogated = 'no'
eldniwinterrogated = 'no'
serranityinterrogated = 'no'
brunointerrogated = 'no'
speedwagoninterrogated = 'no'
renjiinterrogated = 'no'
josukeinterrogated = 'no'
lazyriverinvestigated = 'no'
waterslideinvestigated = 'no'
poolinvestigated = 'no'
askrenji = 'stay'
asktrish = 'stay'
askrobert = 'stay'
evidence = ["Layout of Water Park","Layout of Deck", "Layout of Cabins", "Rule 1", "Rule 2", "Rule 3", "Rule 4", "Rule 5", "Survivors Guide to Surviving","R. Renji's Alibi",
            "Speed Wagon's Testament", "Bruno Bucciarati's Alibi","Three Sets of Footsteps","Time of Murder", "Josuke Higashikata's Alibi", "Cause of Death","Location of Giorno's Body",
            "Mysterious Strands","Multiple Scratch Marks","Trish's Testament","Giorno and Bruno's Weapons", "Letter to Giorno"]
evidencel = ["layout of water park","layout of deck", "layout of cabins", "rule 1", "rule 2", "rule 3", "rule 4", "rule 5", "survivors guide to surviving","r. renji's alibi",
            "speed wagon's testament", "bruno bucciarati's alibi","three sets of footsteps","time of murder", "josuke higashikata's alibi", "cause of death","location of giorno's body",
            "mysterious strands","multiple scratch marks","trish's testament","giorno and bruno's weapons", "letter to giorno"]
hp = 3
pooloptions = 'stay'
attemptagain = 'yes'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''MAIN'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
slowtype1("Deep Sea Escape\n")
play=input("Would you like to play?\n   -> ")
while str(play.lower()) not in ['yes','no']:
	slowtype1("???\n")
	play=input("Would you like to play\n   -> ")
if str(play.lower()) == 'no':
    print("Okay then")
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''INTRO'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

while str(play.lower()) == 'yes':
    if playthrough == 0:
        time.sleep(1.5)
        slowtype("\nWe stood in silence, staring at Giorno's body.")
        slowtype("\nIt's hard to believe that just yesterday he was so full of life.",.5)
        sys.stdout.write("\nR. Renji: ")
        slowtype1("He's...")
        slowtype(" Dead.",.5)
        slowtype("\nHow? ")
        slowtype("How did it come to this? ")
        slowtype("This can't be real.\n\n",2.5)
        sys.stdout.write("Boat Employee: ")
        slowtype("Last call. Now boarding the Deep Sea Escape!\n",.5)
        sys.stdout.write("???: ")
        fasttype("Wait! Don't leave!",.5)
        sys.stdout.write("\nBoat Employee: ")
        slowtype("We're not leaving just yet. But I'm gonna need to see your ID before you board.\n")
        sys.stdout.write("???: ")
        slowtype("Oh yeah no problem. ",.5)
        slowtype("Here.\n")
        sys.stdout.write("Boat Employee: ")
        slowtype("This... ",.5)
        slowtype("This is just a piece of bread.")
        slowtype(" Ooo-kay then. ",.5)
        slowtype("Just tell me your name and gender and I'll mark you as present and boarded.\n\n")
        name = input("Tell the boat employee your name\n   -> ")
        nameans = input("\nSo your name is {}?\n   -> ".format(name))
        if str(nameans.lower()) == 'no':
            sys.stdout.write("Boat Employee: ")
            slowtype("Ah I get it. Very funny...",.5)
            fasttype(" Please tell me your name and board.\n")
            name = input("\n Tell the boat employee your name\n   -> ")
            slowtype("Alright. Your name is, {}\n".format(name))
        if str(nameans.lower()) not in ['yes','no']:
            sys.stdout.write("Boat Employee: ")
            slowtype1("... ")
            slowtype("I'm just gonna take that as a yes.\n")
        elif str(nameans.lower()) == 'yes':
            sys.stdout.write("\nBoat Employee: ")
            slowtype("Got it. ")
        slowtype("For your gender, should I put down Male or Female?\n\n")
        gendermain = input("Tell the Boat Employee your gender\n   -> ")
        if str(gendermain.lower()) not in ['male','female']:
            slowtype("I'm sorry if you don't identify as either, but I have to write down one of those two.\n\n")
            gendermain = input("Tell the Boat Employee your gender\n   -> ")
            if str(gendermain.lower()) not in ['male','female']:
                slowtype("I'm just gonna put down male. ")
                gendermain = "male"
        if str(gendermain.lower()) == "male":
            slowtype("\nOkay so you're a male. Got it.\n")
            gendermain = 'male'
            genderside = 'girl'
        elif str(gendermain.lower()) == 'female':
            slowtype("\nOkay so you're a female. Got it.\n")
            gendermain = 'female'
            genderside = 'guy'
        slowtype("\nAlright, you're all set. Welcome aboard.\n\n",1)
    save = input("Where would you like to begin playing from?\nBeginning     Speed Wagon Joins     Exploring     ???     ???     ???\n   -> ")
    while save not in ['beginning', 'speed wagon joins','exploring','start of killing game','investigation','trial','???']:
        print("That is not a valid save point.")
        save = input("Where would you like to begin playing from?\nBeginning     Speed Wagon Joins     Exploring     ???     ???     ???\n   -> ")
    if save == '???':
        print("You must play the game to unlock those save points\n")
        save = input("Where would you like to begin playing from?\nBeginning     Speed Wagon Joins     Exploring     ???     ???     ???")
    if str(save.lower()) == 'exploring' or str(save.lower()) == 'start of killing game':
        sidegain = 'yes'
    time.sleep(1.5)
    print("")

    ''''''''''''''''''''''''''''''''''''''''''''''''''''BOARDING THE DEEP SEA ESCAPE'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    if str(save.lower()) == 'beginning':
        print("PART I\nACT I: The Deep Sea Escape")
        time.sleep(1.5)
        slowtype("\nI never imagined riding a luxurious boat meant only for rich the wealthy.")
        slowtype(" Everyone's in formal attire but I'm wearing a sweatshirt and sweatpants.\n",.5)
        sys.stdout.write("???: ")
        fasttype("Hey! ",.5)
        slowtype("Who let some randoe on board?\n",.5)
        slowtype1("... ")
        if str(genderside.lower()) == 'girl':    
            fasttype("Oh god, she's definitely talking about me.")
        elif str(genderside.lower()) == 'guy':
            fasttype("Oh god, he's definitely talking about me.",.5)
        slowtype(" Uuuugh. I just got on board and someone's already calling me out.")
        if str(genderside.lower()) == 'girl':
            slowtype(" I mean I could confront her... Or I could just ignore her and go somewhere else.\n")
        elif str(genderside.lower()) == 'guy':
            slowtype("I mean I could confront him... Or I could just ignore him and go somewhere else.\n")
        conign = input("Confront      Ignore\n   -> ")
        if str(conign.lower()) not in ['confront','ignore']:
            if str(genderside.lower()) == 'girl':
                slowtype("Unable to make a valid choice, the girl walked over to you.")
            elif str(genderside.lower()) == 'guy':
                slowtype("Unable to make a valid choice, the guy walked over to me")
            conign = 'confront'
        if str(conign.lower()) == 'confront':
            if str(genderside.lower()) == 'girl':
                slowtype("I guess I'm confronting her. ")
                slowtype("She's already screaming and waving her fists at me... ")
            elif str(genderside.lower()) == 'guy':
                slowtype("I guess I'm confronting him. ")
                slowtype("He's already screaming and waving his fists angrily at me... ",.5)
            slowtype("This'll go well\n",.5)
            sys.stdout.write("???: ")
            slowtype("Excuse me. Are you even listening?\n")
            listening = input("Were you listening?\n   -> ")
            if str(listening.lower()) not in ['yes','no']:
                sys.stdout.write("???: ")
                slowtype("I didn't understand anything that you just said. Are you some kind of foreigner or something?")
                slowtype(" Regardless, I don't know how in the world you got on this boat, but I think you're in the wrong place.\n")
            if str(listening.lower()) == 'yes':
                sys.stdout.write("???: ")
                slowtype("Then we're on the same page.")
                slowtype(" I don't know how in the world you got on this boat, but I think you're in the wrong place.\n")
            elif str(listening.lower()) == 'no':
                sys.stdout.write("???: ")
                slowtype("How rude! ")
                slowtype("... ")
                slowtype("But I guess I respect your honesty.")
                slowtype(" Anyway, I don't know how you got on this boat, but I think you're in the wrong place.\n")
            slowtype("... ")
            if str(genderside.lower()) == 'girl':
                slowtype("Who the hell even is this girl?\n")
            elif str(genderside.lower()) == 'guy':
                slowtype("Who the hell even is this guy?\n")
            sys.stdout.write("???: ")
            slowtype("Thats the face of someone who doesn't know of the illustrious me. ")
            slowtype("Allow me to introduce myself.")
            slowtype(" I am Speed Wagon, esteemed member of the R.E.O. Speedwagon company.\n")
            sys.stdout.write("{}: ".format(name))
            slowtype("Wow. ")
            slowtype("Riveting.")
            slowtype(" And as exciting as what you're telling me is, I won my ticket in a raffle.\n")
            save = 'speed wagon joins'
        
        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''IGNORING SPEED WAGON'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        
        if str(conign.lower()) == 'ignore':
            if str(genderside.lower()) == 'girl':
                slowtype("I guess I'll just ignore her.\n")
            elif str(genderside.lower()) == 'guy':
                slowtype("I guess I'll just ignore him.\n")
            slowtype("As I start walking away, I notice that I'm being followed.")
            slowtype(" I decide to walk faster.\n")
            slowtype("I hear running behind me and make a break for it.\n")
            slowtype1("...\n",.5)
            slowtype("Finally made it to my cabin. I just hope that I lost th-\n")
            slowtype("Before I could finish my thought, the loudspeaker turned on.\n")
            sys.stdout.write("Boat Employee: ")
            if gendermain == 'male':
                slowtype("Attention please. Is there a Mr. Commoner on board? Mr. Commoner? We have a Mrs. Speed Wagon calling for you. ")
            elif gendermain == 'female':
                slowtype("Attention please. Is there a Mrs. Commoner on board? Mrs. Commoner? We have a Mr. Speed Wagon calling for you. ")
            slowtype("Please come to the deck.\n",.5)
            slowtype("Alright... I guess I'll go to the deck.\n",1.5)
            sys.stdout.write("Speed Wagon: ")
            slowtype("Ah, there you are. ")
            slowtype("Now... I'll have you kn-\n")
            sys.stdout.write("{}: ".format(name))
            slowtype("Let me stop you right there. ")
            slowtype("I know exactly what you're going to say.")
            slowtype(" I won my ticket in a raffle at my workplace now please stop following me. ",.5)
            slowtype("Also my name is {}, not commoner\n".format(name))
            save = 'speed wagon joins'

    '''''''''''''''''''''''''''''''''''''''''''''''''''SPEED WAGON JOINS?'''''''''''''''''''''''''''''''''''''''''''''''''''''
    if str(save.lower()) == 'speed wagon joins':
        sys.stdout.write("Speed Wagon: ")
        slowtype("Oh... I See. ",.5)
        slowtype("I sincerely apologize, I thought you were some sort of stowaway.")
        slowtype(" Oh, I know! Allow me to make ammends for my rudeness by showing you around the boat.\n\n")
        sidegain = input("Allow Speed Wagon to show you around?\n   -> ")
        if str(sidegain.lower()) not in ['yes','no']:
            sys.stdout.write("Speed Wagon: ")
            slowtype("I'm just going to take that as a yes.\n")
        elif str(sidegain.lower()) == 'yes':
            sys.stdout.write("Speed Wagon: ")
            slowtype("Fantastic! Now come with me.\n")
        elif str(sidegain.lower()) == 'no':
            sys.stdout.write("Speed Wagon: ")
            slowtype("I see. That's understandable. ",.5)
            slowtype("Well I apologize, once again, for my rudeness and will leave you with a recommendation. I hear that the cabins, indoor water park, and deck are all exquisite places to be.",.5)
        save = 'exploring'
    '''''''''''''''''''''''''''''''''''''''''''''''''''EXPLORATION'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    if str(save.lower()) == 'exploring':
        while explorecount < 3:
            if explorecount == 0:
                explore1 = input("\n\nWhere would you like to explore?\nDeck     Water Park     Cabins\n   -> ")
                explorecheck(explore1)
            elif explorecount == 1:
                if deckexplored == True:
                    explore1 = input("\n\nWhere would you like to explore?\nWater Park     Cabins\n   -> ")
                elif waterparkexplored == True:
                    explore1 = input("\n\nWhere would you like to explore?\nDeck     Cabins\n   -> ")
                elif cabinsexplored == True:
                    explore1 = input("\n\nWhere would you like to explore?\nDeck     Water Park\n   -> ")
                explorecheck(explore1)            
            elif explorecount == 2:
                if waterparkexplored == False:
                    slowtype("I guess it's time to head to the water park.\n")
                    explore1 = 'water park'
                elif cabinsexplored == False:
                    slowtype("I guess it's time to head to the cabins.\n")
                    explore1 = 'cabins'
                elif deckexplored == False:
                    slowtype("I guess it's time to head to the deck.\n")
                    explore1 = 'deck'
            '''''''''''''''''''''''''''''''''''''''''''''''''EXPLORING THE DECK'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            if str(explore1.lower()) == 'deck':
                explorecount = explorecount + 1
                deckexplored = True
                if str(sidegain.lower()) == 'no':
                    slowtype("\nThe deck seems interesting. I'll go there.\n")
                    time.sleep(1.5)
                    slowtype("I went to peer over the side of the boat and breathed in the ocean air. The salt in the air stung my nose a little, but was refreshing nonetheless.\n")
                    slowtype("The walkways are lined with chairs where people are relaxing. I guess there's no mast since the boat is powered by electricity.",.5)
                    slowtype("A little disappointing\n")
                    slowtype("There are some stairs that lead up to a cabana bar where people are enjoying refreshing beverages. There are bananas, apples, and other assorted fruits resting on the table.\n",.5)
                    slowtype("Seems like there are some people at the bar. Maybe I should try to meet some new people... Or I could just check out the next area.\n")
                elif str(sidegain.lower()) == 'yes':
                    sys.stdout.write("{}: ".format(name))
                    slowtype("Let's go check out the deck.\n")
                    sys.stdout.write("Speed Wagon: ")
                    slowtype("Sure thing!\n")
                    time.sleep(1.5)
                    sys.stdout.write("Speed Wagon: ")
                    slowtype("Here we are.")
                    slowtype(" As you can see there are chairs on the deck that people can enjoy themselves in along the walkways.")
                    slowtype(" Also, if you drink, there is a bar up these stairs where you can get drinks and fruits like apples, bananas, or almost anything else. ")
                    slowtype("Just not kiwi I think. ")
                    slowtype("If you follow me up the stairs")
                    slowtype1("...")
                    slowtype(" There is also a pair of binoculars attached to the ground over there where you can see the ocean.")
                    slowtype(" A bit of the deck gets in the view, but it's still a great view.",.5)
                    slowtype(" There are some people at the bar I can introduce you to if you'd like. Or we can just go to another area.\n")
                stayleave = input("Stay     Leave\n   -> ")
                while str(stayleave.lower()) not in ["stay","leave"]:
                    stayleave = input("So... Am I staying or leaving\nStay     Leave\n   -> ")
                if str(stayleave.lower()) == 'stay' and str(sidegain.lower()) == 'no':
                    slowtype("\nI guess I'm staying.",.5)
                    slowtype(" There are a lot of people at the bar, but three of them caught my eye.")
                    slowtype("A man with purple hair that's tied up into what looks like a broom's straws is sitting and rubbing his hands together as if he's praying.")
                    slowtype(" Weird guy.",.5)
                    slowtype(" He has a rather slim build and is wearing a dress shirt and khaki shorts.\n",.5)
                    slowtype("He just rolled a die. He put his hands on his head and reluctantly ordered a drink. I guess he decided what to buy based on his dice roll. I bet his friends call him dice guy.\n")
                    slowtype("There's a woman with long blonde hair and sunglasses, resting her elbows on the table. She is wearing a nice red dress and is staring off the side of the cabana at the ocean.\n")
                    slowtype("She has a vibe of superiority, almost like she is royalty... A princess or something.\n",.5)
                    slowtype("There is a rather large gentleman wearing a white suit, with a white tie, and white dress pants.\n")
                    slowtype("He seems like the CEO of a company or something. ",.5)
                    slowtype("Now... Who to sit next to?")
                if str(stayleave.lower()) == 'stay' and str(sidegain.lower()) == 'yes':
                    sys.stdout.write("{}: ".format(name))
                    slowtype("I think I'd like to meet some people.\n")
                    sys.stdout.write("Speed Wagon: ")
                    slowtype("Sure, let me introduce you to them. ")
                    slowtype("First is that man over there with the purple hair that's tied into a broom or something.")
                    slowtype(" That's R. Renji, he loves to do everything by chance. ")
                    slowtype("That woman over there with long blonde hair and sunglasses is Trish. ")
                    slowtype("I think her dad is the boss of some gang so try not to get on her bad side. ")
                    slowtype("Over there is my dad, Robert E.O. Speedwagon,")
                    slowtype(" CEO of the Speedwagon foundation. ",.5)
                    slowtype("I think that's everyone that I know at the bar. ")
                    slowtype("So who do you want to sit next to?")
                     
                while str(stayleave.lower()) == 'stay':
                    if str(sidegain.lower()) == 'no':
                        sit = input("\n\nWho do you want to sit next to?\nDice Guy     Royalty     CEO\n   -> ")
                        while str(sit.lower()) not in ['ceo','royalty','dice guy']:
                            slowtype("That person doesn't seem too interesting. Who should I sit next to?\n")
                            sit = input("Dice Guy    Royalty     CEO\n   -> ")
                    elif str(sidegain.lower()) == 'yes':
                        sit = input("\n\nWho do you want to sit next to?\nR. Renji     Trish     Robert Wagon\n   -> ")
                        while str(sit.lower()) not in ['r. renji', 'trish','robert wagon']:
                            slowtype("That doesn doesn't seem too interesting. Who should I sit next to?\n")
                            sit = input("R. Renji     Trish     Robert Wagon\n   -> ")
                    if str(sit.lower()) == 'dice guy' or 'r. renji':
                        if str(sidegain.lower()) == 'no':
                                slowtype("\nGuess I'll sit next to that dice guy.\n",.5)
                                slowtype("As you take your seat, the man turns and you make eye contact. ")
                                slowtype("Without hesitation, he introduces himself.\n")
                                sys.stdout.write("???: ")
                                slowtype("Hey bud, good looks. I'm R. Renji.\n")
                        elif str(sidegain.lower()) == 'yes':
                            sys.stdout.write("{}: ".format(name))
                            slowtype("Let's sit next to R. Renji.\n")
                            sys.stdout.write("Speed Wagon: ")
                            slowtype("R. Renji's a really cool guy, I'm sure you'll get along fine with him.\n")
                            slowtype("As you take your seat, R. Renji turns and you make eye contact. ")
                            slowtype("Without hesitation, he introduces himself.\n")
                            sys.stdout.write("R. Renji: ")
                            slowtype("Hey Speed Wagon. Who's this?\n")
                            sys.stdout.write("Speed Wagon: ")
                            slowtype("This is {}.\n".format(name))
                            sys.stdout.write("R. Renji:")
                            slowtype("Good looks {}, nice to meet you.\n".format(name))
                        while str(askrenji.lower()) != "leave":
                            print("What would you like to know about R. Renji?\n")
                            askrenji=input("What is your selling point?                     What do you do for a living?\n\nWhat is with your hair?                    Leave.\n   -> ")
                            while str(askrenji.lower()) not in ["what is your selling point?","what is your selling point","what do you do for a living?","what do you do for a living","what is with your hair?","what is with your hair","leave"]:
                                slowtype("Gonna have to say he wouldn't know how to answer that.\n\n")
                                askrenji=input("What is your selling point?                     What do you do for a living?\n\nWhat is with your hair?                    Leave.\n   -> ")
                            if str(askrenji.lower()) in ["what is your selling point?","what is your selling point"]:
                                sys.stdout.write("{}: ".format(name))
                                slowtype("So what's your selling point?\n")
                                sys.stdout.write("R. Renji: ")
                                slowtype("I like to do everything by chance.")
                                slowtype(" It's like the saying goes. ")
                                slowtype("'God I hate RNG'",.5)
                                slowtype("Why does it feel like I just dissed myself...\n")
                            elif str(askrenji.lower()) in ["what do you do for a living?","what do you do for a living"]:
                                sys.stdout.write("{}: ".format(name))
                                slowtype("So what do you do for a living?\n")
                                sys.stdout.write("R. Renji: ")
                                slowtype("I go from casino to casino trying my luck at different games.")
                                slowtype(" Surprisingly, it's going really well right now.\n")
                            elif str(askrenji.lower()) in ["what is with your hair?","what is with your hair?"]:
                                sys.stdout.write("{}: ".format(name))
                                slowtype("What's with your hair? It's in a weird fan broom thing.\n")
                                sys.stdout.write("R. Renji: ")
                                slowtype("Oh this?")
                                slowtype(" Yeah I have a dartboard and throw a dart, blindfolded, at the dartboard every morning.")
                                slowtype(" Depending on what I hit, I'll do a specific hairstyle.\n")
                            elif str(askrenji.lower()) in ["leave",'leave.']:
                                sys.stdout.write("R. Renji: ")
                                slowtype("Alright, see ya later {}.\n".format(name))
                    elif str(sit.lower()()) == 'royalty' or 'trish':
                        if str(sidegain.lower()()) == 'no':
                            slowtype("\nGuess I'll sit next to the princess girl.\n",.5)
                            slowtype("She's wearing a hat that says TRISH on it. So I guess her name is Trish? ")
                            slowtype("When you sit down, it doesn't seem like she noticed you.\n")
                        elif str(sidegain.lower()()) == 'yes':
                            sys.stdout.write("{}: ".format(name))
                            slowtype("Let's sit next to Trish.\n")
                            sys.stdout.write("Speed Wagon: ")
                            slowtype("Trish can be a bit spoiled at times, but I'm sure you'll get along fine.\n",.5)
                            slowtype("You walk to the bar and take your seat. Trish doesn't register that you or Speed Wagon sat next to her.")
                        slowtype1("...")
                        slowtype("The silence is killing you and you decide to start the conversation yourself.\n\n")
                        while str(asktrish.lower()()) != "leave":
                            print("What would you like to know about Trish?\n")
                            asktrish=input("What is your selling point?                     What do you do for a living?\n\nWhat is your favorite band?                    Leave.\n   -> ")
                            while str(asktrish.lower()()) not in ["what is your selling point?","what is your selling point","what do you do for a living","what do you do for a living?","what is your favorite band?","what is your favorite band","leave"]:
                                slowtype("She probably wouldn't know how to answer that.")
                                asktrish=input("What is your selling point?                     What do you do for a living?\n\nWhat is your favorite band?                    Leave.\n   -> ")
                            if str(asktrish.lower()()) in ["what is your selling point?", "what is your selling point"]:
                                sys.stdout.write("{}: ".format(name))
                                slowtype("So what's your selling point?\n")
                                sys.stdout.write("Trish: ")
                                slowtype("I have a collection of soft things. I don't know why, but I really like soft things.\n")
                            elif str(asktrish.lower()) in ["what do you do for a living?", "what do you do for a living"]:
                                sys.stdout.write("{}: ".format(name))
                                slowtype("So what do you do for a living?\n")
                                sys.stdout.write("Trish: ")
                                slowtype("I don't actually do anything. My dad is the boss of a gang called Passione, so he provides me with everything I need.\n")
                            elif str(asktrish.lower()) in ["what is your favorite band?","what is your favorite band"]:
                                sys.stdout.write("{}: ".format(name))
                                slowtype("Do you have a favorite band?\n")
                                sys.stdout.write("Trish: ")
                                slowtype("My favorite band is Spice Girls. They're great.")
                                slowtype(" Oh, and my favorite song is Wannabe\n")
                            elif str(asktrish.lower()) == "leave":
                                sys.stdout.write("Trish: ")
                                slowtype("See you later.\n")
                    elif str(sit.lower()()) == 'ceo' or 'robert wagon':
                        if str(sidegain.lower()()) == 'no':
                            slowtype("\hGuess I'll sit next to the CEO guy.\n",.5)
                            sys.stdout.write("???: ")
                            slowtype("Hello, take a seat.")
                            slowtype(" I'm Robert E.O. Wagon, founder of the Speed Wagon Foundation. ")
                            slowtype("Would you like to chat?\n")
                        elif str(sidegain.lower()()) == 'yes':
                            sys.stdout.write("{}: ".format(name))
                            slowtype("Let's sit next to your dad.\n",.5)
                            slowtype("As you walk up to Robert Wagon, he signals for you to take a seat next to him.\n")
                            sys.stdout.write("Robert Wagon: ")
                            slowtype("I see you've met Speed Wagon already, so I assume there's no need to introduce myself. Please, ask me anything\n")
                        while str(askrobert.lower()) != 'leave':
                            print("What would you like to know about Robert Wagon?\n")
                            askrobert=input("What is your selling point?                     What do you do for a living?\n\nWhy did you start the Speed Wagon Foundation?                    Leave.\n   -> ")
                            while str(askrobert.lower()) not in ["what is your selling point", "what is your selling point?","what do you do for a living","what do you do for a living?","why did you start the speed wagon foundation?","why did you start the speed wagon foundation", "leave","leave."]:
                                slowtype("I don't think that he would know how to answer that. I should ask him another question.\n")
                                askrobert=input("What is your selling point?                     What do you do for a living?\n\nWhy did you start the Speed Wagon Foundation?                    Leave.\n   -> ")
                            if str(askrobert.lower()) in ["what is your selling point","what is your selling point?"]:
                                sys.stdout.write("{}: ".format(name))
                                slowtype("What's your selling point?\n")
                                sys.stdout.write("Robert Wagon: ")
                                slowtype("I guess it would be this really cool hat I have. ")
                                slowtype("It's got blades that come out of the rim of it. ")
                                slowtype("Neat stuff.\n")
                            elif str(askrobert.lower()) in ["what do you do for a living?","what do you do for a living"]:
                                sys.stdout.write("{}: ".format(name))
                                slowtype("What do you do for a living?\n")
                                sys.stdout.write("Robert Wagon: ")
                                slowtype("I'm the CEO of the Speed Wagon Foundation, it's named after my only child, Speed Wagon\n")
                            elif str(askrobert.lower()) in ["why did you start the speed wagon foundation?","why did you start the speed wagon foundation"]:
                                sys.stdout.write("{}: ")
                                slowtype("Why did you start the Speed Wagon Foundation?\n")
                                sys.stdout.write("Robert Wagon: ")
                                slowtype("A long time ago I went on a journey with a friend. ")
                                slowtype("He died along the journey, and I regret that I was unable to do more for him. ")
                                slowtype("I hoped that someday I would be able to provide whatever the future generations of his family need on any of their bizarre adventures. ")
                                slowtype("The only keepsake I have of him is this handkerchief.\n")
                                slowtype("It's a handkerchief with the initials J.J.\n")
                            elif str(askrobert.lower()) in ["leave","leave."]:
                                sys.stdout.write("Robert Wagon: ")
                                slowtype("It was nice talking with you.\n")
                    stayleave = input("Well I finished my conversation. Should I stay or leave?\n   -> ")
                    while str(stayleave.lower()) not in ['stay','leave']:
                        slowtype("Uh... I don't think that response helps my decision.\n\n")
                        stayleave = input("Should I stay or leave?\n   -> ")
                    if str(stayleave.lower()) == 'leave':
                        slowtype("Ok, guess I'll go somewhere else.\n")
                    elif str(stayleave.lower()) == 'stay':
                        slowtype("I think I'm gonna keep talking to people.\n")
    
                    explore1 = input("\n\nWhere would you like to explore next?\nWater Park     Cabins\n   -> ")
                                                                 #EXPLORING THE WATER PARK
            elif str(explore1.lower()) == 'water park':
                waterparkexplored = True
                explorecount = explorecount + 1
                if str(sidegain.lower()) == 'yes':
                    sys.stdout.write("{}: ".format(name))
                    slowtype("Let's go see the water park now.\n")
                    sys.stdout.write("Speed Wagon: ")
                    slowtype("The water park? ")
                    slowtype("Sounds good!\n")
                elif str(sidegain.lower()) == 'no':
                    slowtype("\nThe water park seems interesting. ")
                    slowtype("I'll go check it out.\n")
                slowtype("When you arrive at the indoor water park, you see multiple people enjoying themselves in a variety of pools. ")
                slowtype("There's a lazy river, a wave pool, and a water slide that leads to the normal pool. The lazy river is really close to the normal pool, and the wave pool is in an area of its own.\n")
                if str(sidegain.lower()) == 'yes':
                    sys.stdout.write("Speed Wagon: ")
                    slowtype("As you can see, there are a lot of different pools you can go to. ")
                    slowtype("There're some concession stands over there too. ",.5)
                    slowtype("So is there anything you want to check out? Or should we just leave.\n")
                elif str(sidegain.lower()) == 'no':
                    slowtype("Looks like there're some concession stands that people are at too. ")
                    slowtype("Maybe I should look around. Or I could just leave.\n")
                while str(pooloptions.lower()) != 'leave':
                    pooloptions = input("\nWhere do you want to go?\nThe Concession Stands     The Pool     Leave\n   -> ")
                    while str(pooloptions.lower()) not in ['the concession stands','the pool','leave']:
                        slowtype("Uh. Where am I going?\n")
                        pooloptions = input("\nWhere do you want to go?\nThe Concession Stands     The Pool     Leave\n   -> ")
                    if str(pooloptions.lower()) == 'the concession stands':
                        if str(sidegain.lower()) == 'yes':
                            sys.stdout.write("{}: ".format(name))
                            slowtype("I'm kind of hungry. Let's go to the concession stands.\n")
                        elif str(sidegain.lower()) == 'no':
                            slowtype("I'm kind of hungry.")
                            slowtype(" Guess I'll go get some food.")
                        slowtype("There are 4 concessions stands lined up in their own area-away from the poolside.")
                        slowtype(" There's a hefty line at each stand. ")
                        slowtype("Doesn't look like you'll be able to get something to eat anytime soon.\n",.5)
                        if str(sidegain.lower()) == 'yes':
                            sys.stdout.write("Speed Wagon: ")
                            slowtype("Hmm... ")
                            slowtype("The lines seem pretty long. Maybe you should talk to some people instead. ")
                            slowtype("Want me to introduce you to some of the people I recognize?\n\n")
                        elif str(sidegain.lower()) == 'no':
                            slowtype("Since the lines seem pretty long, maybe I should talk to some people.\n\n")
                        pooltalk = input("Talk to some people?\Yes    No\n   -> ")
                        while str(pooltalk.lower()) not in ['yes','no']:
                            slowtype("I don't think that answer would help me with my decision.\n\n")
                            pooltalk = input("Talk to some people?\nYes    No\n   -> ")
                        if str(pooltalk.lower()) == 'yes':
                            if str(sidegain.lower()) == 'yes':
                                sys.stdout.write("{}: ".format(name))
                                slowtype("Yeah, can you introduce me to them?\n")
                                sys.stdout.write("Speed Wagon: ")
                                slowtype("With pleasure.")
                                slowtype(" But I only recognize the two over there sitting at that table.")
                                slowtype("The tall and muscular guy wearing sunglasses is Serranity, and the tall, lanky, red headed guy is Eldniw. ")
                                slowtype("Let's go over and say hi.\n")
                                slowtype("As you approach their table, you overhear a bit of their conversation.\n")
                                sys.stdout.write("Eldniw: ")
                            elif str(sidegain.lower()) == 'no':
                                slowtype("There's a tall and muscular guy wearing sunglasses and a tall, lanky, red headed guy. ")
                                slowtype("Guess I'll go see if I can join those two.\n",.5)
                                slowtype("As you approach their table, you overhear a bit of their conversation.\n")
                                sys.stdout.write("???: ")
                            slowtype("Look, Serranity. ")
                            slowtype("I'm telling you that water is the best substance in the world. ")
                            slowtype("Who could ever get enough of that AQUAtic taste?\n")
                            sys.stdout.write("Serranity: ")
                            slowtype("Eldniw... Let me tell you something. ")
                            slowtype("I'm a slick Ford, I like a sick Ford.\n",.5)
                            slowtype1("..." )
                            slowtype("On second thought, you decide not to get involved with either of those people as they seem very weird.\n\n")
                        elif str(pooltalk.lower()) == 'no':
                            if str(sidegain.lower()) == 'yes':
                                sys.stdout.write("{}: ".format(name))
                                slowtype("I think I'll pass on that.\n")
                            elif str(sidegain.lower()) == 'no':
                                slowtype("Maybe some other time.\n")
                    elif str(pooloptions.lower()) == 'the pool':
                        if str(sidegain.lower()) == 'yes':
                            sys.stdout.write("{}: ".format(name))
                            slowtype("The pool seems like a good way to cool off. Let's go there.\n")
                            sys.stdout.write("Speed Wagon: ")
                            slowtype("The pool does sound good right about now.\n",.5)
                        elif str(sidegain.lower()) == 'no':
                            slowtype("I think I'll get in the pool for a while.\n",.5)
                        slowtype("You get your bathing suit on and get in the pool.")
                        slowtype(" The sun shines through the glass encasing the water park. The water splashing around the pool area creates vibrant colors that soothe the eyes. ",.5)
                        slowtype("You get out of the pool after thoroughly enjoying yourself.\n\n")                    
                    elif str(pooloptions.lower()) == 'leave':
                        if str(sidegain.lower()) == 'yes':
                            sys.stdout.write("{}: ".format(name))
                            slowtype("I think I'm ready to leave\n")
                            sys.stdout.write("Speed Wagon: ")
                            slowtype("Okay then, let's go.\n")
                        elif str(sidegain.lower()) == 'no':
                            slowtype("\nI should head out now.\n")
                                                                                #EXPLORING THE CABINS
            elif str(explore1.lower()) == 'cabins':
                cabinsexplored = True
                explorecount = explorecount + 1
                if str(sidegain.lower()) == 'yes':
                    sys.stdout.write("Speed Wagon: ")
                    slowtype("Here are the cabins. ")
                    slowtype("Obviously, this is where you'll sleep. ")
                    slowtype("There isn't really much to the cabins, but I think it's important to tell you the layout so that you don't get lost. ")
                    slowtype("The cabin layout is one big square with two exits to the deck, the east-side exit and the west-side exit. ")
                    slowtype("There are 3 rows of cabins, one on the west side, one in the middle, and the last is on the east side. ")
                    slowtype("So that's the layout, I guess you can go unpack now. I'll wait at the east side exit for you while you unpack.\n",.5)
                elif str(sidegain.lower()) == 'no':
                    slowtype("There isn't really much to the cabins from what I can see. ")
                    slowtype("Looks like the layout is one big square with 3 rows of cabins. An east side row, a west side row, and a middle row.")
                    slowtype(" There are two exits to the deck, one on the east side and one on the west side. ")
                    slowtype("That's it so I guess I can go unpack now.\n",.5)
                slowtype("You walk to the west-side row where your cabin is located and enter your room. After unpacking your things, you leave the room and see a crowd of people walking to the exit. ")
                slowtype("You tug on someone's shirt to ask if he knows what's going on. ")
                slowtype("He's a tall blonde man with a braided tail and three curls above his forehead.\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("Hey, where're all those people going?\n")
                sys.stdout.write("???: ")
                slowtype("There's a Prince concert on the deck for their new album Gold Experience.")
                slowtype("It's starting soon if you want to check it out.\n")
                slowtype("You hear someone call out to the man you stopped.\n")
                sys.stdout.write("???: ")
                slowtype("Hey, Giorno hurry up.\n")
                sys.stdout.write("Giorno Giovanna: ")
                slowtype("My friend is calling for me so I'm gonna go now. ")
                slowtype("Coming Bruno! ")
                slowtype("Oh. I'm Giorno Giovanna by the way.\n")
                slowtype("Giorno walks ahead to catch up with his friend near the exit. ",.5)
                slowtype("Doesn't seem like there's anything else in the cabins, so you decide to leave.\n")
        if str(sidegain.lower()) == 'yes':
            slowtype("After meeting back up with Speed Wagon, the two of you decide to go your separate ways. ")
        slowtype("It's been a long day of exploration, and it's already really late, so you decide to go back to your cabin to sleep.",1.5)
        save = 'start of killing game'
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''START OF KILLING GAME'''''''''''''''''''''''''''''''''''''''''''''''
    if str(save.lower()) == 'start of killing game':
        slowtype1("PART 1\n",.5)
        slowtype("ACT II: THE START OF THE KILLING LIFE\n")
        slowtype("Enter 'Start of killing life' as your save state if you want to start from here.\n\n",1.5)
        slowtype("You wake up to the sound of a loud boom and screams. ")
        slowtype("People are outside saying there's something going on at the deck. ")
        slowtype("You leave your room to go check on the commotion.\n",.5)
        slowtype("Upon seeing what was on the deck, you realized just how unprepared you were to see any of it. ")
        slowtype("Fire consumes the entirety of the deck, and there is a huge hole in the center of the fire.")
        slowtype(" People are screaming and you hear some crewman saying that there was a bomb set off on board. ")
        slowtype("You look around and see the bodies of multiple dead passengers who were unlucky enough to be on the deck at the time of the bomb going off. ")
        slowtype("You think to yourself:")
        slowtype(" The only reason I didn't get caught up in this explosion is because I was out exploring the boat so late. ")
        slowtype("Thoughts of what would've happened if you had been on the deck at the time of the explosion fill your mind. ")
        slowtype("Who would commit such an atrocity? ",.5)
        slowtype("Almost as if on cue, a figure appears above the fire, seemingly floating.\n",.5)
        sys.stdout.write("???: ")
        slowtype("Ladies and gentlemen, have you enjoyed the show so far? ")
        slowtype("Because there is much more to come.\n",.5)
        slowtype("... Show? ")
        slowtype("What kind of sociopathic creep calls this heinous act of villainy a show?\n",.5)
        sys.stdout.write("???: ")
        slowtype("I would like to reveal the next act as soon as possible, but some introductions are in order for the few of you remaining. ")
        slowtype("Right now, the deck is the only safe place on board so the people you see around you are the only people alive.\n",.5)
        slowtype("That's impossible! There were over 300 people on board the ship! ")
        slowtype("Now this lunatic is gonna tell me there're only 13 people alive!\n",.5)
        sys.stdout.write("???: ")
        slowtype("I'm sure you're all very startled right now, but please direct your attention towards me for a moment. ")
        slowtype("My name is Kira Yoshikage, and I would like all of you to participate in a game. ")
        slowtype("For the rest of your time on the Deep Sea Escape, you will participate in a killing game!\n",.5)
        slowtype("I can't comprehend anything that this guy is saying.\n")
        slowtype("A killing game? Is he serious?\n",.5)
        sys.stdout.write("Kira Yoshikage: ")
        slowtype("If you want to get off this ship, it is very easy. ")
        slowtype("All you have to do is ")
        slowtype1("...")
        slowtype("kill someone.\n",.5)
        fasttype("HUH!? ")
        slowtype("Kill someone? He's gotta be joking right? ",.5)
        slowtype1("Right? ")
        slowtype("But from what he's done so far, he must be serious.",.5)
        sys.stdout.write("Kira Yoshikage: ")
        slowtype("That's not all there is to the game though. ")
        slowtype("If you want to escape, not only must you kill someone, but you must get away with the murder! ")
        slowtype("After you've all thoroughly investigated the case, we will have a trial where you will determine the culprit!")
        slowtype(" If you guess right, then the culprit will be punished, and the rest of you will continue the game. ")
        slowtype("But if you guess wrong the culprit gets away. But that's not all that happens. ")
        slowtype("If you guess wrong... ")
        slowtype1("you all die.\n",.5)
        slowtype(" But you don't have to worry about that right now! ")
        slowtype(" Now let's go over the rules. Because what fun's a game without rules!\n\n")
        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''RULES'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        print("Rule 1: You will not harm Kira Yoshikage.")
        print("Rule 2: Certain areas are restricted past 8 P.M.")
        print("Rule 3: There will be no breaking and entering another person's cabin.")
        print("Rule 4: These rules can not be broken or removed.")
        print("Rule 5: Certain places will be off-limits at certain times. Please keep this in mind.")
        print("Make sure to remember these rules, as they are very important and will not be repeated again.\n")
        readytoproceed = input("Have you read the rules and are ready to move on?\n   -> ")
        if str(readytoproceed.lower()) not in ["yes",'no']:
            sys.stdout.write("Kira Yoshikage: ")
            slowtype("I don't care if you're ready or not I'm taking that as a yes!\n")
            readytoproceed = 'yes'
        while readytoproceed != 'yes':
            sys.stdout.write("Kira Yoshikage: ")
            slowtype("That's fine, take your time.\n")
            readytoproceed = input("Have you read the rules and are ready to move on?\n   -> ")
        sys.stdout.write("\nKira Yoshikage: ")
        slowtype("I sincerely hope that you will enjoy your time on board. All commodities will be provided for you, so you don't have to procure your own food and water.\n",.5)
        slowtype("This is crazy... There's no way that I'll ever kill anyone, and I'm sure the rest of the passengers feel the same way. ")
        slowtype("This Kira guy is crazy to think that we'd stoop so low as to murder for our own freedom. Especially if we're provided for while we're on the boat.\n",.5)
        sys.stdout.write("Kira Yoshikage: ")
        slowtype("Until we meet again.\n",.5)
        slowtype("Just as Kira finished his sentence, a pink gas begins to spread across the deck and you lose consciousness.\n\n",1.5)
        '''''''''''''''''''''''''''''''''''''''''''''''''''''''CHECK IF IT WAS A DREAM?'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        slowtype("When you next awake, you're back in your cabin.\n",)
        slowtype("I knew it. It must have just been a dream. ",.5)
        slowtype("But I should still make sure that it was a dream.\n")
        scaredorwhat = input("Do you want to reassure yourself that it was a dream?\nYes     No\n   -> ")
        if str(scaredorwhat.lower()) not in ['yes','no']:
            slowtype("\nWhat did I just say? ")
            slowtype("Whatever, I'll just go reassure myself it was a dream.\n")
            scaredorwhat = 'yes'
        elif str(scaredorwhat.lower()) == 'no':
            slowtype("No... ")
            slowtype("That's not necessary. ")
            slowtype("I know that it was a dream. ")
            slowtype("What a horrible nightmare though. I'll just go back to sleep.\n",1)
            slowtype("Before you realized it, you had fallen asleep and are now being woken to the sound of knocking on your door.\n")
            sys.stdout.write("???: ")
            slowtype("According to the manual I received from Kira, there should be someone who lives here. Is anyone here? ")
            slowtype("If so, come to the bar, the survivors are all meeting there.\n")
            slowtype1("... ")
            slowtype("Survivors.")
            slowtype(" So it wasn't a dream. ",)
            slowtype("Despair fills your soul as the cruel reality sinks in. ",.5)
            slowtype("When you manage to pull yourself together, you make your way to the bar.\n",1.5)
        elif str(scaredorwhat.lower()) == 'yes':
            slowtype("Okay, I should go check out the deck.\n")
            slowtype("You make your way to the deck, and make note that it is eerily quiet. ")
            slowtype("When you get to the deck, everything is the way it should be. Except for one thing. ")
            sys.stdout.write("{}: ".format(name))
            slowtype("Where is everyone?\n")
            slowtype("You accidentally said that out loud, and now you hear footsteps coming from behind you.\n")
            sys.stdout.write("???: ")
            slowtype("Don't you remember yesterday?")
            slowtype(" Or maybe you just thought it was a dream? ")
            slowtype("Whatever the case is, all the passengers are dead. ")
            slowtype("Save the 13 people lucky enough to survive, me and you included.\n")
            slowtype("You turn around to see a man in a sailor outfit.\n")
            sys.stdout.write("???: ")
            slowtype("I'll introduce myself in a sec, the survivors are all meeting at the bar. Let's go.\n")
            slowtype("The man seems suspicious, but you trust that no one is going to murder anyone and follow him.\n")
        slowtype("When you get to the bar, the 13 survivors are all there. ")
        slowtype("There aren't enough chairs for everyone to sit in, so some people had to stand.\n")
        sys.stdout.write("Speed Wagon: ")
        slowtype("{}! I'm glad that you survived. ".format(name))
        slowtype("Now that the last survivor is here, let's begin the meeting.")
        slowtype(" First let's start by going over what's happened so far. ")
        slowtype("We're the only survivors of a bombing on the ship, some creep named Kira Yoshikage is keeping us hostage here, and the only way out is to... ")
        slowtype("Nevermind that part. ")
        slowtype("Some of you may have noticed that there was a manual left on your desk in your cabin. ")
        slowtype("For those of you who didn't see it for whatever reason, it's called 'The Survivors Guide to Survival'. ")
        slowtype("Not the greatest of names, but it's whatever I suppose.")
        slowtype(" In the book lists the names of all the survivors, some things about us, and the layout of the ship, which includes the location of each of our cabins. ")
        slowtype("I think we should take some time to read over the manual, and if you've already read over it, give it to someone who didn't get it yet so that they can read it now.\n")
        slowtype("Everyone complies with what Speed Wagon is saying. ")
        if genderside == 'girl':
            slowtype("You'd think it's strange that everyone is just going along with what she says, ")
        elif genderside == 'guy':
            slowtype("You'd think it's strange that everyone is just going along with what he says, ")
        slowtype("but it's probably because everyone is still shocked about what happened and just want to follow a leader figure. ")
        slowtype("Speed Wagon walks over to me and hands me a manual.\n")
        sys.stdout.write("Speed Wagon: ")
        slowtype("Here. ")
        slowtype("You can consider this extra ammends for what happened earlier I suppose.\n")
        slowtype("Speed Wagon gives you a smile and walks back to the bar. ")
        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''SURVIVORS MANUAL'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        slowtype("You start to read over the manual.\n")
        print("\nThe Survivors Guide to Survival\nBy: Kira Yoshikage\n")
        print("This is where the real fun begins! You know the rules of the game, so here I'll provide you with everything else that you need to know in order to play.")
        print("Survivor List")
        print("Survivor 1: Speed Wagon - (Alive)\nThe child of Robert Wagon. Will inherit the Speed Wagon Foundation upon Robert Wagon's retirement.")
        print("Survivor 2: Robert Wagon - (Alive)\nThe father of Speed Wagon. Current CEO of the Speed Wagon Foundation.")
        print("Survivor 3: Serranity - (Alive)\nA student at the University of Ford. Is a quick Ford and likes a sick Ford.")
        print("Survivor 4: Eldniw - (Alive)\nA student at the University of Ford. Really likes water, and in particular the word aqua.")
        print("Survivor 5: R. Renji - (Alive)\nGoes from casino to casino gambling to make a living. Does everything by random.")
        print("Survivor 6: Trish: - (Alive)\nThe daughter of a mafia boss. Can be a rich spoiled girl at times.")
        print("Survivor 7: Josuke Higashikata - (Alive)\nSon of a sailor, and was determined to be a sailor at a young age. Likes bubbles.")
        print("Survivor 8: Giorno Giovanna - (Alive)\nThe bastard son of Bio Drando and in the future, wants to be a Gang Star.")
        print("Survivor 9: Bruno Bucciarati - (Alive)\nA Capo in the gang known as Passione. Really likes zippers.")
        print("Survivor 10: {} - (Alive)\nWorks a boring 9-5 office job. No interesting hobbies or quirks.".format(name))
        print("Survivor 11: Izaya Orihara - (Alive)\nA well known information broker who likes to be an observer. Loves humans.")
        print("Survivor 12 and 13: |           | - (Alive)\nA brother and sister pair who never lose at any game. Their real names are Sora and Shiro.")
        print("The areas currently available to you are: The Kitchen, The Deck, The Water Park, The Cabins, and The Mess Hall. All other places are off limits.")
        print("Please keep in mind that certain areas will be restricted past 8 P.M. If you enter these areas you will be killed on the spot.")
        print("These areas include, but are not limited to, The Lazy River, The Kitchen, The Mess Hall, The ~!2)#, and The ---")
        print("Speed Wagon, Robert Wagon, Serranity, Eldniw, Izaya Orihara and Josuke Higashikata live in the west-side cabins.")
        print("Bruno Bucciarati, Giorno Giovanna, Trish, and {} live in the middle cabins.".format(name))
        print("R. Renji and |           | live in the east-side cabins.")
        readguide = input("\nEnter yes when you have read the guide, and are ready to move on.\n   -> ")
        while readguide != 'yes':
            readguide = input("Enter yes when you have read the guide, and are ready to move on.\n   -> ")
        time.sleep(1)
        sys.stdout.write("Speed Wagon: ")
        slowtype("\nSince all of our names are in this book, I doubt there's any need for introductions. I recommend that we all check out the areas that were previously only open at certain times.")
        slowtype("I'm sure you all also noticed that some of the restricted areas are blurred and scribbled out. I'm not sure what that's about but I'm sure we'll find out sooner or later.")
        slowtype(" Also, Kira changed some things on the boat so if you notice something out of the ordinary it was probably him.\n")
        sys.stdout.write("Sora: ")
        slowtype("We're not going to explore so we'll be in our rooms if anyone needs us.\n")
        slowtype("Sora and Shiro walk back to their cabin, and the rest of us remained at the bar.\n")
        sys.stdout.write("Bruno Bucciarati: ")
        slowtype("Speed Wagon, while it's great that you've taken the lead. I'm hesitant to do everything that you say.")
        sys.stdout.write("Speed Wagon: ")
        slowtype("That's fine, it's just a recommendation anyway.\n")
        sys.stdout.write("Giorno Giovanna: ")
        slowtype("I don't think Bruno is disagreeing with anything you've said, but I think he just wants us to collectively be more careful.\n")
        sys.stdout.write("Josuke Higashikata: ")
        slowtype("Then how about we all move in groups, that way if anyone is killed we can narrow the suspects down, and create witnesses.\n")
        sys.stdout.write("Speed Wagon: ")
        slowtype("That's a pretty good idea.")
        slowtype(" How should we decide the groups?\n")
        sys.stdout.write("R. Renji: ")
        slowtype("I've got just thing for this. ")
        slowtype("Let's pull sticks from a cup with numbers on it to decide groups.")
        slowtype("There are 4 numbers so we'll be among four groups, I assume that's fine?\n")
        slowtype("No one objects to this idea, so we all go ahead and draw sticks.\n",.5)
        slowtype("Everyone drew a stick and moved into their groups. ")
        slowtype("Looks like the groups are Speed Wagon, Robert Wagon, and R. Renji, Trish, Bruno, and Giorno, Eldniw, Serranity, and Josuke, and Izaya and I are the last group.\n")
        sys.stdout.write("Josuke Higashikata: ")
        slowtype("Wait, those two are the only ones in a group, that could create some problems.\n")
        sys.stdout.write("Izaya Orihara: ")
        slowtype("Don't worry about me, I live as a permanent spectator. I won't murder or be murdered, after all, a spectator shouldn't participate in the game.\n")
        slowtype("Izaya smiles after saying this.")
        slowtype(" There's a weird vibe to him, but it doesn't seem like he's lying.\n")
        sys.stdout.write("Speed Wagon: ")
        slowtype("Well, considering the information that was in the guide, I think we can trust you on that. ".format(name))
        slowtype("{} do you have any problems with this?\n")
        sys.stdout.write("{}: ".format(name))
        slowtype("I'll trust Izaya for now. But let's try to coordinate when our groups are going to places.\n")
        sys.stdout.write("Bruno Bucciarati: ")
        slowtype("That's a good idea. ")
        slowtype("Our groups should be close enough that we can respond quickly in case something happens.")
        sys.stdout.write("Speed Wagon: ")
        slowtype("Okay then. Now that that's settled, we'll be leaving first.\n")
        slowtype("Speed Wagon, Robert Wagon, and R. Renji all leave the bar. ")
        slowtype("The other groups quickly follow suit until it's just me and Izaya left on the deck.\n")
        '''''''''''''''''''''''''''''''''''''''''''''''''''EXPLORING WITH IZAYA'''''''''''''''''''''''''''''''''''''''''
        sys.stdout.write("Izaya Orihara: ")
        slowtype("We should go too, {}.".format(name))
        slowtype("Izaya walks down the stairs, onto the deck, and heads in the direction of the kitchen.\n\n",1.5)
        slowtype("The kitchen is a big room with multiple separate counters for preparing food. ")
        slowtype("Izaya and I checked the fridge and the pantry, and it doesn't seem like we'll have to worry about food. ")
        slowtype("There are different tools in the kitchen for preparing and eating food")
        slowtype("There's a grinder, a whisk, tongs, etc. ")
        slowtype("But the thing that worries me the most is the knives.")
        slowtype("Looks like there are 4 of them, each lined up in ascending order of length. ")
        slowtype("Just as Izaya and I agreed that there wasn't much else to the kitchen, Serranity, Eldniw, and Josuke walked in.\n")
        sys.stdout.write("Josuke Higashikata: ")
        slowtype("Did you two just finish looking at the kitchen?\n")
        sys.stdout.write("{}: ".format(name))
        slowtype("Yeah. So far there was nothing out of the ordinary. ")
        slowtype("If you find anything when you look, make sure to let us know.")
        sys.stdout.write("Eldniw: ")
        slowtype("Don't worry, we got this. I'm really collected responsible so you can count on me.\n")
        sys.stdout.write("Serranity: ")
        slowtype("Like that time you got into an argument with some random guy on the street?\n")
        sys.stdout.write("Eldniw: ")
        slowtype("Okay, listen. ")
        slowtype("That was because he bumped into me and started talking about how water isn't that great of a substance. ")
        slowtype("I mean, I tried to keep calm and explained to him that he was wrong, and water is actually the greatest substance known to man. ")
        slowtype('Then he started saying things like "salt water constitutes more than 70% of the Earth and is useless" and that water is "easily polluted" and I lost it. ')
        slowtype("I punched him right in his water-hating face. ")
        slowtype("God I love water.\n")
        slowtype("While Eldniw was giving his spiel, Izaya had already left the kitchen and made his way to the mess hall. ")
        slowtype("When I was able to catch up to Izaya, he had already explored the mess hall.\n")
        sys.stdout.write("Izaya Orihara: ")
        slowtype("It's just a normal lunch room, looks like this is where we come for breakfast and dinner. ")
        slowtype("There was a giant sign that's in that room that says that murder is prohibited in that room, so I wouldn't worry too much about the mess hall.\n")
        slowtype("Izaya opened the door to the mess hall and revealed to me exactly what he had described. ")
        slowtype("When I turned back around, Izaya was walking away.\n")
        sys.stdout.write("Izaya Orihara: ")
        slowtype("I'm going back to my room now. I'm sure the others are doing the same.\n")
        slowtype("Izaya is right, I should probably go back to my room. ")
        slowtype("On my way back to my room, I ran into R. Renji.\n")
        sys.stdout.write("R. Renji: ")
        slowtype("Pretty random meeting you here. It's already 7:30, you gonna hit the sack soon?\n")
        sys.stdout.write("{}: ".format(name))
        slowtype("Yeah, I'm going to my room right now.\n")
        sys.stdout.write("R. Renji: ")
        slowtype("I'm gonna do the same. I'm beat. ")
        slowtype("I'll see ya tomorrow, {}.\n".format(name))
        slowtype("... Tomorrow huh. ")
        slowtype("It would be nice if I woke up and this were all a dream.\n")
        slowtype("You decide that these kinds of things are pointless to think about, and that you should go back to your room to rest, as you would need as much as possible.",.5)
        slowtype("Just as you entered your room, however, you noticed something. ")
        slowtype("There was a sword, sitting on your dresser. ")
        slowtype("I stared at the sword for a bit, wondering if it was actually real, but decided to just put it away. ")
        slowtype("Kira must be trying to bait us by putting weapons in our rooms. ")
        slowtype("I should assume everyone else got a weapon too. ")
        slowtype("Would anyone of us really commit a murder? ")
        slowtype("The Wagon family seem like nice people so I don't think they would, but I don't know a lot about the others. ")
        slowtype("Trish and Bruno are both associated with the mafia, and if Giorno is a friend of Bruno, then he must be too. ")
        slowtype("I can't imagine any of us really dying. This whole situation still feels like a dream. ")
        slowtype("Maybe it would've been better if I had just stayed at work and given someone else the trip... ")
        slowtype("It was a long day, so I pushed these thoughts to the side for now. I grabbed my Survivors Guide, put it in my back pocket, and went to sleep for the night.\n",1.5)
        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''SECOND DAY'''''''''''''''''''''''''''''''''''''''''''''
        slowtype("\nI woke up the next morning to the sound of the ship's horn, and Kira appeared on the T.V. that was in my room.\n")
        sys.stdout.write("Kira Yoshikage: ")
        slowtype("Good morning everyone. I hope you slept well. ")
        slowtype("Because things are going to get a lot better from here on. ")
        slowtype("I am very excited for what you will all do today, and eagerly await your actions.\n")
        slowtype("The T.V. switched off and someone started banging on my door.\n")
        sys.stdout.write("Speed Wagon: ")
        slowtype("{}? Are you there!? It's terrible, you've gotta come quick!\n".format(name))
        slowtype("A sinking feeling rushed throughout my body. All the things I thought about last night came rushing back to me, and I assumed the worst.\n")
        sys.stdout.write("Hurry up and get ready! You've gotta follow me, you need to see something!\n")
        slowtype("I opened the door and follow Speed Wagon. ")
        slowtype("As I was running, I thought of what Kira said on the T.V. ")
        slowtype("Does he know what happened? If so, how is Kira watching us. There are barely any security cameras anywhere. ")
        slowtype("Before I could elaborate any further on that thought, we arrived at the water park and Speed Wagon dashed towards the lazy river.\n")
        slowtype("I couldn't believe my eyes. ")
        slowtype("What I saw was the dead body of Giorno tied to a raft and floating along the lazy river. ")
        slowtype("I looked around and saw that some others had just arrived. ")
        slowtype("When they saw Giorno's body, they were just as shocked as I was. ")
        slowtype("We stood in silence, staring at Giorno's body.\n")
        slowtype("It's hard to believe that just yesterday he was so full of life.\n",.5)
        sys.stdout.write("R. Renji: ")
        slowtype1("He's... ")
        slowtype("Dead.\n")
        slowtype("How? ")
        slowtype("How did it come to this? ")
        slowtype("This can't be real.\n")
        slowtype("When the fifth person arrived at the scene of the crime, we heard another honk of the ship's horn.\n")
        sys.stdout.write("Kira Yoshikage: ")
        slowtype("Erm... Attention. Attention. ")
        slowtype("A body has been discovered. Please conduct a thorough investigation, and report to the deck in 12 hours for a trial. ")
        slowtype("That is all. *that was fun I hope I get to do it again*\n")
        slowtype("Trial? ")
        slowtype("That must be where we decide who the culprit is. ")
        slowtype("Even though I didn't know Giorno that well, he was such an understanding person. From our group meeting, I could tell he understood his friends well. ")
        slowtype("And now he's dead. ")
        slowtype("I will bring the truth to light.\n")
        save = 'investigation'
        '''''''''''''''''''''''''''''''''''''''''''''''''''''''''INVESTIGATION'''''''''''''''''''''''''''''''''''''''''''''''''''''
    if save == 'investigation':
        slowtype("\nInvestigation Period - Start\n")
        print("During the investigation period, you will review certain locations, and look for any discrepancies from when you last saw them.")
        print("Additionally, others will be conducting their own investigation, and when you may have a chance to ask some of them questions.")
        print("The key to a successful trial is a complete understanding of the case, so make sure you don't miss anything.")
        print("Enter 'investigation' as your save state if you want to start from here.")
        slowtype("I guess I should start by interrogating the people that're here and investigating the water park first.\n\n")
        while 'R. Renji' in waterparkinterrogate or 'Bruno Bucciarati' in waterparkinterrogate or 'Josuke Higashikata' in waterparkinterrogate or 'Speed Wagon' in waterparkinterrogate:
            investigatewaterpark = input("Who would you like to interrogate?\n{}\n   -> ".format(waterparkinterrogate))
            while str(investigatewaterpark.lower()) not in ['bruno bucciarati', 'josuke higashikata','speed wagon','r. renji']:
                if 'brun' in str(investigatewaterpark.lower()):
                    slowprint("I already interrogated Bruno.\n")
                elif 'josu' in str(investigatewaterpark.lower()):
                    slowprint("I already interrogated Josuke.\n")
                elif 'r. r' in str(investigatewaterpark.lower()):
                    slowprint("I already interrogated R. Renji.\n")
                elif 'speed ' in str(investigatewaterpark.lower()):
                    slowprint("I already interrogated Speed Wagon.\n")
                slowtype("\nYou hear a voice telling you to type: R. Renji, Speed Wagon, Bruno Bucciarati, or Josuke Higashikata, whichever you have not interrogated.\n")
                investigatewaterpark = input("Who would you like to interrogate?\n{}\n   -> ".format(waterparkinterrogate))
            if str(investigatewaterpark.lower()) == 'r. renji':
                sys.stdout.write("\n{}: ".format(name))
                slowtype("Hey, Renji did you see anything suspicious last night?\n")
                sys.stdout.write("R. Renji: ")
                slowtype("Can't say that I did. ")
                slowtype("I flipped a coin and it landed heads so I went to bed.\n")
                print("\nYou learned R. Renji's Alibi\n")
                waterparkinterrogate.remove("R. Renji")
            elif str(investigatewaterpark.lower()) == 'speed wagon':
                sys.stdout.write("\n{}: ".format(name))
                slowtype("Speed Wagon, you were the one who came to get me, but how did you find out that Giorno died?\n")
                sys.stdout.write("Speed Wagon: ")
                slowtype("Well you see, I decided that it would be a good idea to patrol the area in the morning, afternoon, and near night time in case something suspicious is going on. ")
                slowtype("When I was patrolling the water park, that's when I found Giorno.\n")
                print("\nYou learned Speed Wagon's Testament\n")
                waterparkinterrogate.remove("Speed Wagon")
            elif str(investigatewaterpark.lower()) == 'bruno bucciarati':
                sys.stdout.write("\n{}: ".format(name))
                slowtype("Sorry to bother you right now, but I've got to ask, Bruno. ")
                slowtype("When was the last time you saw Giorno? ")
                slowtype("You two are close, so I imagine that you or Trish must've been the last person to see him.\n")
                sys.stdout.write("Bruno Bucciarati: ")
                slowtype("Don't worry about it, this happens a lot in my line of work. ")
                slowtype("I saw him just before I went to bed. After we finished investigating the kitchen, Giorno, Trish, and I were on the deck from about 7:30 to 8:00 P.M.")
                slowtype("After that, we left the deck and went right to our cabins around 8 P.M. ")
                slowtype("I know that for sure, I saw Giorno walk into his room.\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("I see. ")
                slowtype("So Giorno must've been killed some time past 8 P.M. ")
                slowtype("Was he acting strange at all when you were talking to him\n")
                sys.stdout.write("Bruno Bucciarati: ")
                slowtype("No, I can't say that he was. ")
                slowtype("But on that topic, I did hear some footsteps outside Giorno's cabin last night. In fact, I heard footsteps three times. ")
                slowtype("I don't know what time this was at, but it couldn't have been that long after we had all gone to our cabins.\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("Thanks for telling me that. ")
                slowtype("I must not have heard the footsteps because my cabin is on the other end of the middle cabins from yours.\n")
                print("\nYou learned Bruno Bucciarati's Alibi")
                print("You learned Three Sets of Footsteps")
                print("You learned Time of Murder\n")
                waterparkinterrogate.remove("Bruno Bucciarati")
            elif str(investigatewaterpark.lower()) == 'josuke higashikata':
                sys.stdout.write("\n{}: ".format(name))
                slowtype("Hey, Josuke did you notice anything anything suspicious last night?\n")
                sys.stdout.write("Josuke Higashikata: ")
                slowtype("Sorry, I didn't. ")
                slowtype("After I saw you in the kitchen, Serranity, Eldniw, and I went our separate ways. ")
                slowtype("I can't tell you what they were doing, but I went right to my cabin. ")
                slowtype("Dealing with those two is a hassle... ")
                slowtype("Especially Serranity. ")
                slowtype("The hell is a Ford?\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("Seems like you had a rough time.\n")
                print("\nYou learned Josuke Higashikata's Alibi\n")
                waterparkinterrogate.remove("Josuke Higashikata")
        slowtype("Seems like that was everyone. ")
        slowtype("I should investigate the water park itself now.\n\n")
        while 'Lazy River' in waterparkinvestigated or 'Normal Pool' in waterparkinvestigated or 'Water Slide' in waterparkinvestigated: 
            investigatewaterpark = input("Where do you want to investigate?\n{}\n   -> ".format(waterparkinvestigated))
            if str(investigatewaterpark.lower()) not in waterparkinvestigated:
                if 'laz' in str(investigatewaterpark.lower()):
                    slowprint("I already investigated the Lazy River\n")
                    investigatewaterpark = input("Where do you want to investigate?\n{}\n   -> ".format(waterparkinvestigated))
                elif 'normal pool' in str(investigatewaterpark.lower()):
                    slowprint("I already investigated the Normal Pool\n")
                    investigatewaterpark = input("Where do you want to investigate?\n{}\n   -> ".format(waterparkinvestigated))
                elif 'water sl' in str(investigatewaterpark.lower()):
                    slowprint("I already investigated the Water Slide\n")
                    investigatewaterpark = input("Where do you want to investigate?\n{}\n   -> ".format(waterparkinvestigated))
                else:
                    slowtype("\nYou hear a voice saying in your head. Try Normal Pool, Water Slide, or Lazy River.\n")
                    investigatewaterpark = input("Where do you want to investigate?\n{}\n   -> ".format(waterparkinvestigated))
            if str(investigatewaterpark.lower()) == 'lazy river':
                slowtype("This is the place that Giorno's body is. ")
                slowtype("He's floating around in circles with the current of the lazy river. ")
                slowtype("For some reason, Giorno is tied down to a raft with some rope. ")
                slowtype("Upon closer inspection, you notice that the back of Giorno's head a small bump with some blood. ")
                slowtype("He must've been hit in the back of the head with some kind of blunt object. ")
                slowtype("The weapon must be somewhere else, since I don't see anything like that near the lazy river or in the lazy river.\n")
                print("\nYou learned Giorno's Cause of Death\n")
                waterparkinvestigated.remove("Lazy River")
                print("You learned Location of Giorno's Body\n")
            elif str(investigatewaterpark.lower()) == 'normal pool':
                slowtype("I don't think there will be anything at the normal pool, but I should check it out anyway. ")
                slowtype("There doesn't seem to be anything out of the ordinary here.\n")
                slowtype("But, just as you are about to go somewhere else, you notice something.\n")
                slowtype("There're weird lines along the water slide. ")
                slowtype("I had completely forgotten about the water slide until now. I should go take a look.\n")
                waterparkinvestigated.remove("Normal Pool")
                waterslideavailable = 'yes'
                print("The water slide is now available for investigation.")
            elif str(investigatewaterpark.lower()) == 'water slide' and waterslideavailable == 'no':
                slowtype("I don't see why I would need to go to the water slide right now. ")
                slowtype("Maybe I should look somewhere else.\n")
            elif str(investigatewaterpark.lower()) == 'water slide' and waterslideavailable == 'yes':
                slowtype("When you get to the top of the water slide, you that there are small strands of something at the top of the water slide.\n")
                slowtype("They're very dry and are a brownish color. ")
                slowtype("Could this be someone's hair?\n")
                slowtype("You also make note of the streaks going down the waterslide.\n")
                slowtype("There are multiple scratch marks on the water slide that have deteriorated the paint. ")
                slowtype("This couldn't have been here before, I mean this is a luxury cruise liner.")
                slowtype("Does this mean something?\n")
                print("\nYou learned Mysterious Strands\n")
                print("You learned Multiple Scratch Marks\n")
                waterparkinvestigated.remove("Water Slide")
        slowtype("That should be all the points of interest. ")
        slowtype("Bruno and the rest of the guys are over at the wave pool, so if they notice anything I'm sure they'll bring it up during the trial.\n")
        slowtype("It would probably be a good idea to go to Giorno's room.\n",1.5)
        slowtype("When you get to the cabins, you see some people already investigating Giorno's room. ")
        slowtype("You enter the room to begin your own investigation.\n")
        while 'Trish' in giornoroominterrogate or 'Eldniw' in giornoroominterrogate or 'Serranity' in giornoroominterrogate:
            giornoroominvestigate = input("Who would you like to interrogate?\n{}\n   -> ".format(giornoroominterrogate))
            while str(giornoroominvestigate.lower()) not in ['trish','serranity','eldniw']:
                if 'tri' in str(giornoroominvestigate.lower()):
                    slowtype("I already talked to Trish")
                elif 'ser' in str(giornoroominvestigate.lower()):
                    slowtype("I already talked to Serranity")
                elif 'eld' in str(giornoroominvestigate.lower()):
                    slowtype("I already talked to Eldniw")
                else:
                    slowtype("\nYou hear a voice in your head telling you to type: Trish, Serranity, or Eldniw, whichever you have not talked to yet.\n")
                giornoroominvestigate = input("Who would you like to interrogate?\n{}\n   -> ".format(giornoroominterrogate))
            if str(giornoroominvestigate.lower()) == 'trish':
                sys.stdout.write("{}: ".format(name))
                slowtype("Hey, Trish. How're you doing?\n")
                sys.stdout.write("Trish: ")
                slowtype("...\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("I know you're upset, but right now, Giorno would want us to discover his murderer. In order to do that, I need to ask you some questions. Can you help me?\n")
                sys.stdout.write("Trish: ")
                slowtype("... Okay.\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("Thanks. ")
                slowtype("I heard from Bruno that you were on the deck with him and Giorno yesterday and that you went to your cabin after you all left. ")
                slowtype("Did you go anywhere after or notice anything suspicious?\n")
                sys.stdout.write("Trish: ")
                slowtype("I didn't go anywhere after that, no.")
                slowtype("But I did hear footsteps coming from near Giorno's room. I heard it three times.\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("You heard them too, huh?\n")
                sys.stdout.write("Trish: ")
                slowtype("I'm guessing Bruno heard them too?\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("Yeah, he did. ")
                slowtype("Is there anything else I should know?\n")
                sys.stdout.write("Trish: ")
                slowtype("Oh. Bruno probably didn't tell you this since he said to keep it a secret, but I'll tell you anyway. ")
                slowtype("Bruno and Giorno both gave me the weapons that they had in their room. ")
                slowtype("They told me that they'd be fine and that they were more worried about my safety than their own. ")
                slowtype("And now look what happened...")
                print("\nYou learned Trish's Testament - Footsteps\n")
                print("You learned Giorno and Bruno's Weapons\n")
                giornoroominterrogate.remove('Trish')
                giornoroominterrogatel.remove('trish')
            elif str(giornoroominvestigate.lower()) == 'Serranity':
                sys.stdout.write("{}: ".format(name))
                slowprint("Hey, Serranity. Have you noticed anything suspicious lately?\n")
                sys.stdout.write("Serranity: ")
                slowprint("The morning sun will rise\nAs we lose another Ford\nI can hear our brothers' cries\nBecause today we lost a Ford\n")
                sys.stdout.write("{}: ".format(name))
                slowprint("... I'll keep that in mind, thanks.\n")
                giornoroominterrogate.remove("Serranity")
                giornoroominterrogatel.remove("serranity")
            elif str(giornoroominvestigate.lower()) == 'Eldniw':
                sys.stdout.write("{}: ".format(name))
                slowprint("Hey, Eldniw. Have you noticed anything suspicious lately?\n")
                sys.stdout.write("Eldniw: ")
                slowprint("Dude, please don't talk so loudly. ")
                slowprint("I was up all last night drinking apple juice. ")
                slowprint("Oh, and by the way. Apple juice contains water so I'm not committing adultery\n")
                slowprint("It doesn't seem like Eldniw will be much help.\n")
                giornoroominterrogate.remove("Eldniw")
                giornoroominterrogatel.remove(eldniw)
        slowprint("Just as you were about to leave the room, you overhear Serranity and Eldniw talking.\n")
        sys.stdout.write("Serranity: ")
        slowprint("Yo, Fords I just found this paper with writing!\n")
        sys.stdout.write("Eldniw: ")
        slowprint("Mmmm paper. Yes. Can I eat that?\n")
        sys.stdout.write("{}: ".format(name))
        fasttype("WAIT! ")
        slowtype("Don't eat that!\n")
        slowtype("You were able to get the piece of paper just before Eldniw ate it. ")
        slowtype("You begin to read the letter.\n")
        print("Giorno,\n    I have something important to talk to you about. Please meet me on the Deck at 8:30 P.M")
        print("\nYou learned Letter to Giorno\n")
        slowtype("This must have been written by the culprit. ")
        slowtype("I'll hold on to this for safe keeping, it must be important. ")
        slowtype("I mean, if we can figure out who went to the deck at 8:30, besides Giorno, we can narrow down our suspects!\n")
        slowtype("As you finished reading the letter, you heard the ship's horn again.\n",.5)
        sys.stdout.write("Kira Yoshikage: ")
        slowtype("Attention, the trial will commence shortly, please come to the deck immediately. Failure to comply will result in execution.\n.",.5)
        slowtype("I guess we don't have a choice. ")
        slowtype("We have to participate in the trial.\n\n",1.5)
        ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''INVESTIGATION PERIOD OVER'''''''''''''''''''''''''''''''''''
        slowtype("Everyone gathered at the deck very soon after you arrived. ")
        slowtype("Once everyone was there, Kira made his appearance.\n")
        sys.stdout.write("Kira Yoshikage: ")
        slowtype("Thank you all for coming. We commence the trial momentarily.\n")
        slowtype("Everyone looked around with confused faces until someone had the courage to ask the question we were all wondering.\n")
        sys.stdout.write("Robert Wagon: ")
        slowtype("Mr. Yoshikage. Are we conducting the trial on this barren deck?\n")
        slowtype("Kira laughed at this comment.\n")
        sys.stdout.write("Kira Yoshikage: ")
        slowtype("Oh, silly Robert. Of course we're not going to hold the trial here you imbecile.\n")
        slowtype("As Kira finished his sentence, machinery opened a circular hole in the deck. ")
        slowtype("From the hole, came an elevator. However, to me, it seemed more like a cell than an elevator.\n")
        sys.stdout.write("Kira Yoshikage: ")
        slowtype("Please, don't be shy. ")
        slowtype("Enter.\n",.5)
        slowtype("We hesitated to enter the elevator. We were scared of what was to come. ")
        slowtype("Bruno and Trish were the first ones to enter the elevator.\n")
        sys.stdout.write("Trish: ")
        slowtype("Are you all coming? Or are we just gonna let ourselves be executed and let the murderer get away?\n")
        slowtype("Trish's words incited courage in everyone, allowing us to step onto the elevator.",2)
        slowtype("The elevator took us deeper than I think any human has ever been before. ")
        slowtype("It felt like an eternity had passed while we were on that elevator, but I'm sure only a few seconds had actually gone by. ")
        slowtype("When we reached the bottom, what was revealed to us was as an enormous dome. ")
        slowtype("There's a ring of podiums with each of our names at one of them, and a judge's seat where the same figure I saw above the flames was sitting.\n")
        sys.stdout.write("Kira Yoshikage: ")
        slowtype("Ladies and gentlemen. ")
        slowtype("Please take to your respective podium. ")
        slowtype("We will momentarily begin the trial.\n")
        slowtype("We were hesitant, once more, to take that first step forward. ")
        slowtype("However Trish and Bruno's confident stride reminded us that we weren't dead yet, and that we can still unmask the culprit and bring justice to Giorno. ")
        slowtype("The killer is among us, but who is it?\n\n")
        save = 'trial'
    ''''''''''''''''''''''''''''''''''''''''''''''''''''TRIAL START'''''''''''''''''''''''''''''''''''''''''''''
    if str(save.lower()) == 'trial':
        print("Get closer to the truth of the mystery using evidence in the list provided")
        print("Make sure your answers contain the entire name of the proof.")
        print("As the trial goes on, use the evidence that you collected in order to refute people's statements, and point out the contradictions in their words.")
        print("If you successfully point out a contradiction, you move on. If not, you will lose one heart. You have three hearts. Each time you lose HP, a count will be displayed.")
        print("When answering a question, you can type 'Review Evidence' to see the list of evidence again.")
        print("Enter 'trial' as your save state if you want to start from here.\n")
        readytocontinue = input("Are you clear on the rules and ready to continue?\n   -> ")
        while readytocontinue != 'yes':
            if str(readytocontinue.lower()) not in ['yes','no']:
                print("Type yes to continue, or no to keep reading.")
                readytocontinue = input("Are you clear on the rules and ready to continue?\n   -> ")
            elif str(readytocontinue.lower()) == 'no':
                print("Take your time reading")
                readytocontinue = input("Are you clear on the rules and ready to continue?\n   -> ")
        while str(attemptagain.lower()) == 'yes':
            while hp != 0:
                slowtype1("\nTrial - Start\n\n")
                print(evidence)
                slowtype("\nRobert Wagon: Well, we're supposed to start the trial... but how do we do that? ")
                slowtype("The only experience I've ever had was sitting next to a lawyer as a representative.\n",.5)
                slowtype("It doesn't seem like anyone knows what to do.\n")
                slowtype("Sora: ")
                slowtype("Sigh. Let's start by going over what we know then.\n")
                sys.stdout.write("Shiro: ")
                slowtype("The victim is Giorno Giovanna, and the place of murder is the water park.\n")
                sys.stdout.write("Sora: ")
                slowtype("Giorno was killed by a blunt object to the back of the head. ")
                slowtype("The body was tied to a raft and left in the lazy river. ")
                slowtype("That's the gist of what we know 100% for now.\n")
                slowtype("Wait, are these guys actually useful?!\n")
                sys.stdout.write("Eldniw: ")
                slowtype("Not trying to say I don't understand why the body was left in the pool, because after all water is the GOAT, ")
                slowtype("but why was the body left on a raft, better yet, why was he tied to it?\n")
                sys.stdout.write("R. Renji: ")
                slowtype("Is that really an important detail?\n")
                sys.stdout.write("Speed Wagon: ")
                slowtype("Sure it's a small detail, but why would the culprit go through the trouble of tying Giorno to a raft?\n\n")
                whyisgiornotied = input("Why was Giorno tied to the raft?\n   -> ")
                printevidence(whyisgiornotied)
                while str(whyisgiornotied.lower()) not in ["rule 5","location of giorno's body"]:
                    if str(whyisgiornotied.lower()) != 'review evidence':
                        sys.stdout.write("R. Renji: ")
                        slowtype("I don't see why that would make the culprit tie Giorno to the raft.\n")
                        slowtype("Shit... I blew it!\n")
                        hp = hp - 1
                        print("You have {} HP left".format(hp))
                        if hp == 0:
                            break
                    if str(whyisgiornotied.lower()) not in ['rule 5',"location of giorno's body"]:
                        whyisgiornotied = input("Why was Giorno tied to the raft in the lazy river?\n   -> ")
                    printevidence(whyisgiornotied)
                if hp == 0:
                    break
                if str(whyisgiornotied.lower()) == 'rule 5':
                    sys.stdout.write("{}: ".format(name))
                    slowtype("Giorno was tied to the raft because of Rule 5.\n")
                elif str(whyisgiornotied.lower()) == "location of giorno's body":
                    sys.stdout.write("{}: ".format(name))
                    slowtype("The reason Giorno was tied to the raft can be explained with the location of his body.\n")
                sys.stdout.write("Robert Wagon: ")
                slowtype("It must be due to my age that I don't understand, could you elaborate?\n\n")
                whyisgiornotied2 = input("What other crucial piece of evidence is necessary in order to fully understand the reason for the culprit tying Giorno's body to the raft?\n   -> ")
                printevidence(whyisgiornotied2)
                while str(whyisgiornotied2.lower()) != "time of murder":
                    sys.stdout.write("Robert Wagon: ")
                    if str(whyisgiornotied2.lower()) != 'review evidence':
                        slowtype("I'm sorry, I still don't quite understand.\n")
                        slowtype("Shit... I blew it!\n")
                        hp = hp - 1
                        print("You have {} HP left".format(hp))
                        if hp == 0:
                            break
                    if str(whyisgiornotied2.lower()) != 'time of murder':
                        whyisgiornotied2 = input("What other crucial piece of evidence is necessary in order to fully understand the reason for the culprit tying Giorno's body to the raft?\n   -> ")
                    printevidence(whyisgiornotied2)
                if hp == 0:
                    break
                sys.stdout.write("{}: ".format(name))
                slowtype("There's one more thing that's important to keep in mind. ")
                slowtype("The time of murder is equally important here. ")
                slowtype("Bruno can attest that the last time that he saw Giorno was at 8 P.M, which means that Giorno died some time after 8 P.M. According to Rule 5, the lazy river is one of the places that is closed, threatening death if you enter past 8 P.M. ")
                slowtype("The only reason I can think that the culprit tied Giorno to the raft is because he needed a way to circumvent this rule.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("Okay, I can understand that. ")
                slowtype("But how exactly did the culprit use the raft to circumvent this?\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("Well, I haven't thought that far ahead yet...\n")
                sys.stdout.write("Izaya Orihara: ")
                slowtype("It seems that you got a little bit ahead of yourself, {}. ".format(name))
                slowtype("But I see where that goes next.\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("Really? ")
                slowtype("How did he circumvent that rule?\n")
                sys.stdout.write("Izaya Orihara: ")
                slowtype("Well I wouldn't be much of an information broker if I just gave out information willy nilly. ")
                slowtype("If you want to know, it's going to cost you.\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("What use is money on this ship? Why can't you just tell us?\n")
                sys.stdout.write("Izaya Orihara: ")
                slowtype("I'm a spectator, {}. I only get involved if you involve me forcefully. I don't want your money, I want information.\n".format(name))
                slowtype("If you want me to lead you down the right path, then tell me something I don't know.\n\n".format(name))
                tellizaya = input("What thing could Izaya not know about the case?\n   -> ")
                printevidence(tellizaya)
                while str(tellizaya.lower()) != "letter to giorno":
                    if str(tellizaya.lower()) != 'review evidence':
                        if str(tellizaya.lower()) in evidencel:
                            sys.stdout.write("Izaya Orihara: ")
                            slowtype("Sigh. I already knew that. How disappointing.\n")
                        elif str(tellizaya.lower) not in evidencel:
                            sys.stdout.write("Izaya Orihara: ")
                            slowtype("I don't see how that's related to the case.\n")
                        slowtype("Shit... I blew it!\n")
                        hp = hp - 1
                        print("You have {} HP left".format(hp))
                        if hp == 0:
                            break
                    if str(tellizaya.lower()) != 'letter to giorno':
                        tellizaya = input("What thing could Izaya not know about the case?\n   -> ")
                    printevidence(tellizaya)
                if hp == 0:
                    break
                sys.stdout.write("{}: ".format(name))
                slowtype("There's no way that you could've known about the letter that the culprit wrote to Giorno.\n")
                sys.stdout.write("Izaya Orihara: ")
                slowtype("Go on.\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("The reason you couldn't have known is because only four people know about this: Trish, Serranity, Eldniw, and Me. ")
                slowtype("And that's because Eldniw almost ate the letter, so I held on to it for safe keeping.\n")
                sys.stdout.write("Eldniw: ")
                slowtype("Oh yeah, that is a thing that I did, yeah.\n")
                sys.stdout.write("Serranity: ")
                slowtype("This Ford wack.\n",.5)
                sys.stdout.write("Izaya Orihara: ")
                slowtype("Right. So what does the letter say?\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("It reads as follows\n\n")
                slowtype("Giorno,\n    I have something important to talk to you about. Please meet me on the Deck at 8:30 P.M\n\n")
                sys.stdout.write("R. Renji: ")
                slowtype("Hold on, that contradicts the location of the murder! There's no way in hell that letter is real!\n")
                sys.stdout.write("Speed Wagon: ")
                slowtype("Now that you mention it...\n")
                sys.stdout.write("Sora: ")
                slowtype("But that doesn't mean that it can't be real.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("If it doesn't mean that it isn't real, then why is Giorno's body in the lazy river? ")
                slowtype("If you can't explain that, then there's no way that letter is real!\n")
                sys.stdout.write("Izaya Orihara: ")
                slowtype("That can be easily answered, R. Renji.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("I-it can?\n")
                sys.stdout.write("Izaya Orihara: ")
                slowtype("Yeah, but I'm not going to answer your question. {} will.\n".format(name))
                sys.stdout.write("{}: ".format(name))
                slowtype("I will?\n")
                slowtype("The room turns to you in anticipation.\n\n")
                lettercontradict = input("How do you explain the discrepency between the location of Giorno's murder, and the letter that the culprit wrote?\n   -> ")
                printevidence(lettercontradict)
                while str(lettercontradict.lower()) != "three sets of footsteps":
                    if str(lettercontradict.lower()) != 'review evidence':
                        if str(lettercontradict.lower()) in evidencel:
                            sys.stdout.write("Izaya Orihara: ")
                            slowtype("Are you always this disappointing?\n")
                        elif str(lettercontradct.lower()) not in evidencel:
                            sys.stdout.write("Izaya Orihara: ")
                            slowtype("I don't see how that's related to the case")
                        slowtype("Shit... I blew it!\n")
                        hp = hp - 1
                        print("You have {} HP left".format(hp))
                        if hp == 0:
                            break
                    if str(lettercontradict.lower()) != 'three sets of footsteps':    
                        lettercontradict = input("How do you explain the discrepency between the location of Giorno's murder, and the letter that the culprit wrote?\n   -> ")
                    printevidence(lettercontradict)
                if hp == 0:
                    break
                sys.stdout.write("{}: ".format(name))
                slowtype("It can be explained by the three sets of footsteps that Bruno and Trish heard outside their door.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("That seems pretty convenient, that Bruno and Trish just happened to hear those footsteps.\n")
                sys.stdout.write("Trish: ")
                slowtype("You trying to say something?\n")
                sys.stdout.write("Bruno Bucciarati: ")
                slowtype("What merit would we have in making up such a thing?\n")
                sys.stdout.write("R. Renji: ")
                slowtype("For instance, maybe you two are working together, and killed Giorno!\n")
                sys.stdout.write("Trish: ")
                slowtype("That's ridiculous!\n")
                sys.stdout.write("Bruno Bucciarati: ")
                slowtype("Even someone such as forgiving as I can't overlook what you just said, R. Renji. ")
                slowtype("Accusing a man of the mafia, a capo no less, of killing one of his own is blasphemous.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("All the more reason for you two to do this! ")
                slowtype("I bet you two killed Giorno so both of you could escape! ")
                slowtype("You probably figured he would forgive you, since your a part of the same gang. ")
                slowtype("But you gotta get up pretty early in the morning to trick ol' R. Renji!\n",.5)
                sys.stdout.write("Kira Yoshikage: ")
                slowtype("Wait, did I not tell you guys? ")
                slowtype("Even if two people plan a murder, only the person who delivers the killing blow will be able to leave.\n",.5)
                sys.stdout.write("R. Renji: ")
                slowtype1("... ")
                slowtype("Say that sooner man.\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("So this letter is legit, we confirmed that, because both Trish and Bruno heard footsteps. ")
                slowtype("As you can see, the letter states that Giorno would go to the deck around 8:30 P.M, which aligns with what Bruno said about last seeing Giorno. ")
                slowtype("It also explains the three sets of footsteps. ")
                slowtype("First, the culprit walked towards Giorno's room to drop off the letter, and left for the deck, second, Giorno walked to the deck, and third, both Giorno and the culprit walked to the water park.\n")
                sys.stdout.write("Eldniw: ")
                slowtype("Oh HELL YEAH. This culprit's got taste! If you're gonna commit a murder, at least do it near water!\n")
                slowtype("The room turns to Eldniw\n",.5)
                sys.stdout.write("Eldniw: ")
                slowtype("Wait, I know that makes me look suspicious, but it wasn't me!")
                slowtype("Wait, I know that this makes me look suspicious, but I swear it wasn't me!\n")
                sys.stdout.write("Speed Wagon: ")
                slowtype("That's still up for debate, Eldniw. We don't have anything conclusive yet.\n")
                sys.stdout.write("Shiro: ")
                slowtype("Speed Wagon is right, the only thing it confirms is that the murder took place a little after 8:30 and that the method to circumvent Rule 5 is somewhere in the water park.\n")
                sys.stdout.write("Robert Wagon: ")
                slowtype("But how exactly would one go about doing such a thing? ")
                slowtype("I didn't find anything in the water park that could help the culprit do that.\n")
                sys.stdout.write("Speed Wagon: ")
                slowtype("I've gotta go with my dad on this one. There was nothing out of the ordinary at the pool. The wave pool was the same, the lazy river was the same except for Giorno, the normal pool was the same, and the water slide were all the same.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("So in other words, we can't figure out anymorer unless we figure out how the culprit got Giorno in the river.\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("Wait a second, you're wrong about that, Speed Wagon.\n\n")
                howisgiornointheriver = input("What piece of evidence can explain a discrepency in what was said in this discussion, and show how the culprit got Giorno into the lazy river?\n   -> ")
                printevidence(howisgiornointheriver)
                while str(howisgiornointheriver.lower()) not in ['mysterious strands','multiple scratch marks']:
                    if str(howisgiornointheriver.lower()) != 'review evidence':
                        sys.stdout.write("Speed Wagon: ")
                        slowtype("So, how does that disprove my statement?\n")
                        slowtype("Shit... I blew it!\n")
                        hp = hp - 1
                        print("You have {} HP left".format(hp))
                        if hp == 0:
                            break
                    if str(howisgiornointheriver.lower()) not in ['mysterious strands','multiple scratch marks']:    
                        howisgiornointheriver = input("What piece of evidence can explain a discrepency in what was said in this discussion, and show how the culprit got Giorno into the lazy river?\n   -> ")
                    printevidence(howisgiornointheriver)
                if hp == 0:
                    break
                sys.stdout.write("{}: ".format(name))
                slowtype("Actually, there were multiple scratch marks and weird strands on the water slide. ")
                slowtype("It's possible that those could be related to the rope.\n")
                sys.stdout.write("Bruno Bucciarati: ")
                slowtype("I didn't notice that, that's a good catch, {}. ".format(name))
                slowtype("I would imagine that since this is a luxury cruise liner, that the staff wouldn't allow something like that to remain on the water slide for long.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("I guess that's true. ")
                slowtype("But how did Giorno get from the water slide to the lazy river?\n\n")
                slidetoriver = input("What piece of evidence would explain how Giorno went from the water slide in the normal pool to the lazy river?\n   -> ")
                printevidence(slidetoriver)
                while str(slidetoriver.lower()) != "layout of water park":
                    if str(slidetoriver.lower()) != 'review evidence':
                        sys.stdout.write("R. Renji: ")
                        slowtype("... I don't follow.\n")
                        slowtype("Shit... I blew it!\n")
                        hp = hp - 1
                        print("You have {} HP left".format(hp))
                        if hp == 0:
                            break
                    if str(slidetoriver.lower()) != 'layout of water park':    
                        slidetoriver = input("What piece of evidence would explain how Giorno went from the water slide in the normal pool to the lazy river?\n   -> ")
                    printevidence(slidetoriver)
                if hp == 0:
                    break
                sys.stdout.write("{}: ".format(name))
                slowtype("If you look at the layout of the water park, the normal pool and lazy river are really close to each other. ")
                slowtype("It's possible that the culprit slid giorno down the waterslide, and used the momentum from the water slide to launch him towards the lazy river! ")
                slowtype("That would also explain why Giorno was tied down to a raft! It's so that Giorno had some sort vehicle that lets him skid across the water towards the lazy river, and so that he doesn't fall off!\n")
                sys.stdout.write("Trish: ")
                slowtype("It's all starting to make sense now!\n")
                sys.stdout.write("R. Renji: ")
                slowtype("That's great and all, and I hate to be the bearer of bad news, but we still haven't made much progress towards finding the culprit.\n")
                sys.stdout.write("Robert Wagon: ")
                slowtype("R. Renji is right,  even if we know how the culprit committed the crime, how do we figure out who committed the crime?\n")
                sys.stdout.write("Sora: ")
                slowtype("Let's start by going over who has a reliable alibi. An alibi that can be confirmed by someone else. ")
                slowtype("Since only the one who delivered the killing blow will escape, there shouldn't be any reason to lie about someone else's alibi being true. ")
                slowtype("Shiro and I were in our room, we didn't leave except for meals and for the trial.\n")
                sys.stdout.write("Bruno Bucciarati: ")
                slowtype("Trish and I were in our rooms the whole time after we parted from Giorno. I didn't hear footsteps coming from Trish's room, only from Giorno's, so she can't be the culprit.\n")
                sys.stdout.write("Trish: ")
                slowtype("Yeah, it's the same for Bruno, I didn't hear any footsteps from his room either.\n")
                sys.stdout.write("Josuke Higashikata: ")
                slowtype("As much as I wish it weren't the case, I'm certain that Eldniw and Serranity didn't go anywhere. Oh and also Izaya. ")
                slowtype("After we finished exploring, Eldniw and Serranity hung around in my room and kept bothering me. After that I went for a walk where I met Izaya at one of the cross sections. ")
                slowtype("We had a conversation and we saw each other walk in to our cabins.\n")
                sys.stdout.write("Izaya Orihara: ")
                slowtype("That's true, I went into my room after that.\n")
                sys.stdout.write("Serranity: ")
                slowtype("Yup, that's a Ford. I can confirm that is a Ford.\n")
                sys.stdout.write("Speed Wagon: ")
                slowtype("I'm guessing that's his way of saying that it's as Josuke says? ",.5)
                slowtype("Anyway, my dad and I said goodnight to each other before going to bed and we saw each other go into the our room. I didn't hear him leave. ")
                sys.stdout.write("Robert Wagon: ")
                slowtype("This is true, we turned in around 6:30 I believe.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("{} and I ran into each other just before going to bed, so we're clean too... ".format(name))
                slowtype("but that means that everybody has a reliable alibi. We're stuck again.\n",.5)
                slowtype("Silence filled the room. Were we really stuck?\n",.5)
                sys.stdout.write("Sora: ")
                slowtype("Hold on. Someone's alibi isn't as strong as the others. ")
                slowtype("{} and R. Renji, you two say you saw each other before bed, but neither of you saw each other go to your room. ".format(name))
                slowtype("Not only that, but you two don't even live in the same row of cabins!\n")
                sys.stdout.write("Bruno Bucciarati: ")
                slowtype("So how do we determine which of them is more suspicious?\n")
                sys.stdout.write("Shiro: ")
                slowtype("That's easy. ")
                slowtype("Sora and I didn't hear R. Renji come back to his room.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("*Geh*\n")
                sys.stdout.write("Trish: ")
                slowtype("Is that true?")
                sys.stdout.write("Sora: ")
                slowtype("Yeah, it is. ")
                slowtype("Shiro and I have alibis that account for each other, so that means there's a high chance that neither of us is the culprit. ")
                slowtype("If that's the case, then our testimonies are equally reliable as our alibi.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("Well what about {}!? ")
                if gendermain == 'male':
                    slowtype("He's equally as suspicious as I am since no one can account for him either!\n")
                elif gendermain == 'female':
                    slowtype("She's equally as suspicious as I am since no one can account for her either!\n")
                sys.stdout.write("Sora: ")
                slowtype("That's not true R. Renji. ")
                slowtype("There's one thing that you're overlooking. ",.5)
                slowtype("{} lives in the middle row with Trish and Bruno, whereas you live in the east row where the only other people are Shiro and I! ")
                sys.stdout.write("R. Renji: ")
                slowtype("T-That doesn't mean that {} couldn't have been at the deck! ")
                if gendermain == 'male':
                    slowtype("I last saw {} at 7:30 P.M, when he was just going to bed! ")
                    slowtype("That means that if he didn't go to his room, then he could've been at the deck! ")
                elif gendermain == 'female':
                    slowtype("I last saw {} at 7:30 P.M, when she was just going to bed! ")
                    slowtype("That means that if she didn't go to his room, then she could've been at the deck! ")
                sys.stdout.write("{}: ".format(name))
                slowtype("That's not quite right R. Renji. ")
                slowtype("There's a reason why we couldn't have been at the deck, and a very good one.\n\n")
                whycantbedeck = input("What evidence makes it impossible for you to have been at the deck past 7:30?\n   -> ")
                printevidence(whycantbedeck)
                while str(whycantbedeck.lower()) != "bruno bucciarati's alibi":
                    if str(whycantbedeck.lower()) != 'review evidence':
                        sys.stdout.write("R. Renji: ")
                        slowtype("See! You don't have a good reason after all!\n")
                        slowtype("Shit... I blew it!\n")
                        hp = hp - 1
                        print("You have {} HP left".format(hp))
                        if hp == 0:
                            break
                    if str(whycantbedeck.lower()) != "bruno bucciarati's alibi":
                        input("What evidence makes it impossible for you to have been at the deck past 7:30?\n   -> ")
                    printevidence(whycantbedeck)
                if hp == 0:
                    break
                sys.stdout.write("{}: ".format(name))
                slowtype("R. Renji, the reason that I couldn't have been on the deck is because of Bruno's alibi! ")
                slowtype("Bruno was on the deck with Giorno and Trish from 7:30 - 8 P.M, meaning that I could not have been anywhere but the water park or the cabins! ")
                slowtype("But, there would have been more than three sets of footsteps if I were to be at the water park, meaning that I was in my cabin.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("That doesn't mean that it couldn't be either of you, the culprit's footsteps could've easily have been one of theirs.\n")
                sys.stdout.write("Sora: ")
                slowtype("That's wrong. ")
                slowtype("If it was either of them, then Bruno or Trish would have told us one more thing. ")
                slowtype("They would have told us that they heard a door open! ")
                slowtype("That leaves only you R. Renji.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("Then how about this!? ")
                slowtype("Someone so closely involved with the mafia surely would have brought a weapon! ")
                slowtype("We all had one, and since Giorno is a part of the mafia, there's no way that I'd ever be able to kill him. ")
                slowtype("Also, if the culprit and Giorno met on the deck, there's no chance for a sneak attack since they both walked to the water park together. ")
                slowtype("How about that huh?!\n")
                sys.stdout.write("Speed Wagon: ")
                slowtype("We did all have weapons, didn't we?\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("That's not quite right.\n")
                sys.stdout.write("Speed Wagon: ")
                slowtype("It's not? Did we not all receive weapons?\n")
                weaponswhere = input("What piece of evidence would prove that not everyone had their weapons?\n   -> ")
                printevidence(weaponswhere)
                while str(weaponswhere.lower()) != "giorno and bruno's weapons":
                    if str(weaponswhere.lower()) != 'review evidence':
                        sys.stdout.write("R. Renji: ")
                        slowtype("See?! You can't explain that after all!\n")
                        slowtype("Shit... I blew it.\n")
                        hp = hp - 1
                        print("You have {} HP left".format(hp))
                        if hp == 0:
                            break
                    if str(weaponswhere.lower()) != "giorno and bruno's weapons":
                        input("What piece of evidence would prove that not everyone had their weapons?\n   -> ")
                    printevidence(weaponswhere)
                if hp == 0:
                    break
                sys.stdout.write("{}: ".format(name))
                slowtype("It's not that part that's wrong, Speed Wagon. ")
                slowtype("It's just that not everyone had weapons at the time of Giorno's death, one of those people being Giorno.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("Where'd that claim come from?\n")
                sys.stdout.write("Trish: ")
                slowtype("From me.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("Huh?\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("That's right. ")
                slowtype("Both Bruno and Giorno gave their weapons to Trish. So it would've been impossible for Giorno to have a weapon when he was attacked.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("Why would they do such a thing? That's ridiculous!\n")
                sys.stdout.write("Bruno Bucciarati: ")
                slowtype("Not at all. ")
                slowtype("I am a capo of the gang Passione, and under me was Giorno. ")
                slowtype("Part of the reason why Giorno and I are even here is because we were tasked with protecting Trish. ")
                slowtype("That mission doesn't change even in this situation.\n")
                sys.stdout.write("R. Renji: ")
                slowtype("...\n")
                slowtype("R. Renji hung his head in defeat and shame, and fell to his knees.\n")
                sys.stdout.write("Kira Yoshikage: ")
                slowtype("Sooo. ")
                slowtype("I'm guessing you're all ready to vote? ")
                slowtype("Then please vote for who you think the killer is!")
                slowtype1("TRIAL CLEAR!",1.5)
                attemptagain = 'complete'
            if hp == 0:
                time.sleep(.5)
                sys.stdout.write("Kira Yoshikage: ")
                slowtype("The votes are in, and you voted for... ")
                slowtype("{}! ".format(name))
                slowtype("Unfortunately, you voted wrong. ")
                slowtype("You will now all be executed, and the culprit will be allowed to leave.\n")
                sys.stdout.write("{}: ".format(name))
                slowtype("Damn it... Why did no one trust me!\n")
                slowtype1("GAME OVER\n")
                attemptagain = input("Would you like to try the trial again?\n   -> ")
                while str(attemptagain.lower()) not in ["yes",'no']:
                    attemptagain = input("Would you like to try the trial again?")
                if str(attemptagain.lower()) == 'yes':
                    hp = 3
        if attemptagain == 'complete':
            sys.stdout.write("Kira Yoshikage: ")
            slowtype("The votes are in, and you voted for... ")
            slowtype("R. Renji! ",.5)
            slowtype("Congratulations! You guessed correctly! ")
            slowtype("Now, as promised R. Renji will be punished for disturbing our peace!\n")
            slowtype("R. Renji was forced into the air by some other wordly magic, none of us could explain how he does it, but this must be how Kira levitates himself. ")
            slowtype("Kira flung R. Renji into another room, we heard screaming, and then silence. ")
            slowtype("This must be a dream.",1.5)
            slowtype1("END OF PART I",.5)
        elif attemptagain == 'no':
            slowtype("I see...\n")
            slowtype("Is this death?\n")
            slowtype("It's cold.\n")
            slowtype("It's dark.\n")
            slowtype("But at least it's finally over.\n")
    play = input("Would you like to load a save point?\n   -> ")
    while str(play.lower()) not in ['yes','no']:
        print("Try yes or no")
        play = input("Would you like to load a save point?\n   -> ")
    if str(play.lower()) == 'yes':
        playthrough = 1
        print("")
    elif str(play.lower()) == 'no':
        print("Thanks for playing")
                