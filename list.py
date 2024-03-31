#five functions

def main():
    #basics of program
    print("Welcome to the program! ")

    #an empty list to hold items
    shoppingCart = []

    #add item
    def addItem(cart, item):
    #loop until the user chooses to stop
        print("Enter 'no' to stop adding items, and 'yes' to continue: ")
        #the loop
    #add item to list
        cart.append(item)
        print(f"{item} was added!")
        #return 'cart'
        return cart
        

    #remove item
    def removeItem(cart, item):
        #checks if there even is anything to remove
        if item in cart: 
            cart.remove(item)
            print(item, "was removed from the cart")
            return cart
        else:
            print("That isn't there to remove, silly! ")

    #view items
    def viewCart(cart):
        if cart:
            for num in cart:
                print(f"You have", num)
        else:
            print("There isn't anything yet. ")

    #remove all items
    def clearCart(cart):
        #empty the array
        cart.clear()
        print("The cart is empty. ")

    #state items and break
    def checkout(cart):
        #recap contents
        viewCart(cart)
        #remove all
        clearCart(cart)
        print("Thank you! Have a great day! ")

   
   
    while True:
        print("1. Add ")
        print("2. Remove ")
        print("3. View ")
        print("4. Clear ")
        print("5. Finish ")

        #get input
        userInput = input("What would you like to do?: ")

        #break loop
        if userInput.lower() == "quit":
            print("Have a great day! ")
            break
        
        elif userInput == "1":
            while True:
                #ask for what item the user wants
                itemToAdd = str(input("What would you like to add?: "))
                shoppingCart = addItem(shoppingCart, itemToAdd)
                #ask if they want to add more
                addMore = input("Do you want to add more?: ")
                #if they do, continue the loop
                if addMore.lower() == "yes":
                    continue
                #if they don't, break the loop
                elif addMore.lower() == "no":
                    break
                elif addMore.lower() != "yes" or "no":
                    print("Please use 'yes' or 'no' to answer")
                    addMore = input("Do you want to add more?: ")
                    #if they do, continue the loop
                    if addMore.lower() == "yes":
                        continue
                    #if they don't, break the loop
                    elif addMore.lower() == "no":
                        break
            
        elif userInput == "2":
            #ask what the user wants to remove
            itemToRemove = input("What do you want to remove?: ")
            shoppingCart = removeItem(shoppingCart, itemToRemove)

        elif userInput == "3":
            #let the user look inside the 'cart'
            viewCart(shoppingCart)

        elif userInput == "4":
            #let user remove all
            clearCart(shoppingCart)

        elif userInput == "5":
            #clear and exit after confirming the cart contents
            checkout(shoppingCart)
            break

        #catchall
        else:
            print("Please use one of the indicated responses to make a choice, or type 'quit' to exit. ")
    

if __name__ == "__main__":
    main()