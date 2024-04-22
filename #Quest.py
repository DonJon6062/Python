# import tkinter
import tkinter as tk

#add message boxes
from tkinter import messagebox

# create the main window
root = tk.Tk()
# give the main window a title
root.title("Torfam: The Title My Friend Gave This Game Upon Asking For Them To Give Me One, Who Knows What It Means? ")

# Create a frame to hold a scrollable text area for displaying the jokes
wordsFrame = tk.Frame(root)
# Add the frame using the grid layout
wordsFrame.grid(row=0, column=0, pady = 50, sticky="nsew")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
wordsFrame.grid_rowconfigure(0, weight=1)
wordsFrame.grid_columnconfigure(0, weight=1)

#add textbox
textBoxText = tk.Text (wordsFrame, wrap = "word")
textBoxText.grid(row=0, column=0, sticky="nsew")

#add scrollbar
scrollbar = tk.Scrollbar(wordsFrame, orient= "vertical", command=textBoxText.yview) #create scrollbar
scrollbar.grid(row = 0, column = 1, sticky="ns") #place scrollbar
textBoxText.config(yscrollcommand=scrollbar.set) #configure scrollbar

def introductionText():
    #print intro
    startingText = "It is a nice day, judging by the feeling of the sun on your skin. You open your eyes, or you would. You don't have a head! \n 1. Stumble out of bed looking for one. \n 2. Keep laying down. How would you even find one without eyes?"
    textBoxText.insert(tk.INSERT, startingText)

def buttonChoiceOne():
        #choice one
        choiceButton1 = tk.Button(root, text= "1", command = buttonSelectionOne)
        choiceButton1.grid(row=1, column=0)
        #choice two
        choiceButton2 = tk.Button(root, text= "2", command = buttonSelectionTwo)
        choiceButton2.grid(row=1, column=1)

def buttonSelectionOne():
    #consequences
        choiceTextOne = " \n You stumble around, trip, and eventually feel what may be a doorway! \n 1. Are you even decent? Look for clothes, or something to protect yourself with. Anything other than just /going out unprepared/. \n 2. You don't have a head! How you look is important when you can /see/! Go out to find a head, quickly! "
        textBoxText.insert(tk.INSERT, choiceTextOne)
        choiceUn()

def buttonSelectionTwo():
        choiceTextTwo =" \n What will you do then, rot? You can't do anything with that mindset! I suppose if you wish to give up, I can't stop you. You coward. Go to bed. Stay headless, and spineless. "
        textBoxText.insert(tk.INSERT, choiceTextTwo)


def choiceUn(): 
        #disable previous buttons
        choiceButton1 = tk.Button(root, text= "1", state = "disabled")
        choiceButton1.grid(row=1, column=0)

        choiceButton2 = tk.Button(root, text= "2", state = "disabled")
        choiceButton2.grid(row=1, column=1)
       
        #choice; prepare
        choiceUnText = " \n What now? Is there time to prepare, or will you /head/ out? (1 or 2): "
        textBoxText.insert(tk.INSERT, choiceUnText)

        choiceUnTextButton1 = tk.Button(root, text = "1", command = buttonUnSelectionOne)
        choiceUnTextButton1.grid(row=1, column=0)

        choiceUnTextButton2 = tk.Button(root, text = "2", command = buttonUnSelectionTwo)
        choiceUnTextButton2.grid(row=1, column=1)

def buttonUnSelectionOne():
      buttonSelectionOneText = " \n Fumbling about more, you ram your foot into something hard. It is a box. \n The items inside are heavy. You can only really carry one and remember where it is. \n 'Cause all you have is touch to lead you \n You can't even smell it. \n Or taste it. \n It's all up to memory. \n 1. The hollow metal thing seems useful. \n 2. The thick wooden thing is probably good. \n 3. The heavy cloth with something inside, please! "
      textBoxText.insert(tk.INSERT, buttonSelectionOneText)
      choiceUnPtOne()
      
def buttonUnSelectionTwo():
      buttonSelectionTwoText = " \n There's no time for prep! You need to find your head, quickly!"
      textBoxText.insert(tk.INSERT, buttonSelectionTwoText) 
      choiceUnPtTwo()

def choiceUnPtOne():
        #disable previous buttons
        choiceUnTextButton1 = tk.Button(root, text = "1", state = "disabled")
        choiceUnTextButton1.grid(row=1, column=0)

        choiceUnTextButton2 = tk.Button(root, text = "2", state = "disabled")
        choiceUnTextButton2.grid(row=1, column=1)
        
        #choice; prepare
        choiceUnPtOneTextButtonOne = tk.Button(root, text = "1", command = buttonUnPtOneSelectionOne)
        choiceUnPtOneTextButtonOne.grid(row=1, column=0)

        choiceUnPtOneTextButtonTwo = tk.Button(root, text = "2", command = buttonUnPtOneSelectionTwo)
        choiceUnPtOneTextButtonTwo.grid(row=1, column=1)

        choiceUnPtOneTextButtonThree = tk.Button(root, text = "3", command = buttonUnPtOneSelectionThree)
        choiceUnPtOneTextButtonThree.grid(row=1, column=2)

#choice-ception
#choice within a choice; broom, pot and sack of potatoes
def buttonUnPtOneSelectionOne():
    #pot get!
    buttonUnSelectionOneText = " \n You grab it and put it on your neck, as once more, no head. It's not very big, but it has a top, so maybe attackers will aim for what they think has a head. Or they won't. But now is not the time for pessimism. Pessimism is for when you have a mind to feel negative. And thus, you retrace your steps to the exit, and begin the search for your head. "
    textBoxText.insert(tk.INSERT, buttonUnSelectionOneText)
    choiceUnPtTwo()

def buttonUnPtOneSelectionTwo():
    #broom get!
    buttonUnSelectionTwoText = " \n Giving it a few swings, you're fairly certain that if someone approaches you can scare them off. Swinging like a madman and all. 'Cause you can't see them and can only flail, hoping to hit /something/. Only if they wack you first of course. You can't hear them. And thus, you retrace your steps to the exit, and begin the search for your head. "
    textBoxText.insert(tk.INSERT, buttonUnSelectionTwoText)
    choiceUnPtTwo()

def buttonUnPtOneSelectionThree():
    #sack of potatoes get!
    buttonUnSelectionThreeText = " \n The hefty item has what feels like multiple smaller items making up the weight. The oblong items are grainy. Did you have a bag of stones? You can't remember much, with your hippocampus detatched. You hope they're stones. Or. Something. Something useful. Please let this be useful. And thus, you retrace your steps to the exit, and begin the search for your head. "
    textBoxText.insert(tk.INSERT, buttonUnSelectionThreeText)
    choiceUnPtTwo()

def choiceUnPtTwo():
      #disable previous buttons
        choiceUnPtOneTextButtonOne = tk.Button(root, text = "1", state = "disabled")
        choiceUnPtOneTextButtonOne.grid(row=1, column=0)

        choiceUnPtOneTextButtonTwo = tk.Button(root, text = "2", state = "disabled")
        choiceUnPtOneTextButtonTwo.grid(row=1, column=1)

        choiceUnPtOneTextButtonThree = tk.Button(root, text = "3", state = "disabled")
        choiceUnPtOneTextButtonThree.grid(row=1, column=2)

        #move somewhere
        choiceUnPtTwoText = " \n Without a brain, you can't remember where.. anything is. Welp, the only way is forward.\n Where /is/ forward?"
        textBoxText.insert(tk.INSERT, choiceUnPtTwoText)

        choiceUnPtTwoTextButtonOne = tk.Button(root, text = "Northwest", command = buttonUnPtTwoSelectionOne)
        choiceUnPtTwoTextButtonOne.grid(row=1, column=0)

        choiceUnPtTwoTextButtonTwo = tk.Button(root, text = "North", command = buttonUnPtTwoSelectionTwo)
        choiceUnPtTwoTextButtonTwo.grid(row=1, column=1) 

        choiceUnPtTwoTextButtonThree = tk.Button(root, text = "Northeast", command = buttonUnPtTwoSelectionThree) 
        choiceUnPtTwoTextButtonThree.grid(row=1, column=2)

def buttonUnPtTwoSelectionOne():
    buttonUnPtTwoSelectionOneText = " \n Soon enough, dried leaves crunch around you, and the occasional patch of grass tickles your ankle. You trip over a root, and ram into a tree trunk. \n HARD.\n Something falls on your head! You can see! The bees whose hive is on your neck don't seem as happy.."
    textBoxText.insert(tk.INSERT, buttonUnPtTwoSelectionOneText)

def buttonUnPtTwoSelectionTwo():
    buttonUnPtTwoSelectionTwoText = " \n After a bit of walking, you feel vines around your feet, and moist soil. Using your hand to trail up one of the vines, you feel a hard surface. A pumpkin! Placing it on your lead leads you to realize; no eyeholes, but you can hear, at least."
    textBoxText.insert(tk.INSERT, buttonUnPtTwoSelectionTwoText)

def buttonUnPtTwoSelectionThree():
    buttonUnPtTwoSelectionThreeText = " \n The unmistakable feeling of mud sticks to the soles of your feet. Suddenly, you step right in something cold and.. mettalic? Aside from adjusting your vision for the many, many holes in the bucket, this is a great head! Whoever had that probably didn't need it anywhoo. This'll do, for now!"
    textBoxText.insert(tk.INSERT, buttonUnPtTwoSelectionThreeText)


introductionText()
buttonChoiceOne()

# start the main window
root.mainloop()