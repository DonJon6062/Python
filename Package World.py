import json 

#function tht writes file 
def writeJSON(data, fileName = "JSONfile.json"):
    #make file
    with open(fileName, "w") as f:
        #write content
        json.dump(data, f, indent=4)

#make JSON file
data = ["Your File: "]
writeJSON(data)

#create loop so user can choose to add or read as long as they want       
while True:
        #inform user about what's going to happen
        print("I'm going to create a JSON file for you! You can look at it, too!")
        #print options for the user
        print('1: Look at the file')
        print('2: Quit')

        #choose
        choice = input('Enter your choice(1/2): ')

        #for the second choice
        if choice == '1':
            with open("JSONfile.json", "r") as f:
                data = json.load(f)

            print(data)

        #end loop
        elif choice == '2':
            print("Thanks for trying this out! ")
            break

            #catches invalid inputs
        else: 
            print('Please enter (1/2/3): ')