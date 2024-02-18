#Don Jones 1.18.2024

#user input/output code for python, two variables

#welcome message
print("Good day, can I get your name to properly greet you?")

#function to get the user's name
#add space so that it looks better when running
userName = input("What is your first name? ")

#print out the input
print("I hope you have a great day", userName)

#commas in print statements add a space
print("Is it a good day today?", " What is the weather like?")

#ask for the weather
weatherIs = input("How is the weather today? ")

#relay 
print(f"Ah, so it is {weatherIs}. I hope you have a nice {weatherIs} day!")

#ask how day has been
rateDay = input("Please let me know, from 1-5 (5 being GREAT!), how your day has been so far: ")
rateInt = 0

#check to see if it was a number
#do NOT camel case isnumeric. all lowercase
if rateDay.isnumeric():
    rateInt = int(rateDay)
    #the f needs to be at the beginning of any line that will have a variable printed
    print("Thank you for letting me know!")
#else needs a colon beside it, just like the function
else:
    #if the entry is not a number
    print("That's not the numerical version of a number")
    
#relay all info
print(f"So it's been a {rateInt}/5, {weatherIs} day for {userName}.")