#making a write/read file

#function that reads file 
def readFile(fileNameToRead):
    #open file to read
    with open(fileNameToRead, 'r') as file:
        #read content
        data = file.read()
        #return contents to the code
        return data
    
#function tht writes file 
def writeFile(fileNameToWrite, fileData):
    #open file to write
    with open(fileNameToWrite, 'a') as file: 
        #write content
        file.write(fileData)

#main part, user chooses to add or read

#create loop so user can choose to add or read as long as they want       
while True:
    #the name of the file
    theFile = 'Journal.txt'
    #create file
    writeFile(theFile, '')
    #print options for the user
    print('1: Create a journal entry')
    print('2: Read your journal entries')
    print('3: Exit')
    #choose
    choice = input('Enter your choice(1/2/3): ')

    #check entry and respond correctly
    if choice == '1':
        journalEntry = input('Enter your journal entry: ')
        #places a break in the entries
        writeFile(theFile, journalEntry + '\n\n')
        print('Entry added!')

    elif choice == '2':
        print(readFile(theFile))

    elif choice == '3':
        print('Thank you for using this journal, have a great day!')
        #break the loop
        break
    #catches invalid inputs
    else: 
        print('Please enter (1/2/3): ')