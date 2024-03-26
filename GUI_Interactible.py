# import sqlite library for database things
import sqlite3

# import tkinter
import tkinter as tk

#add message boxes
from tkinter import messagebox

# create jokes table
def create_table(conn):
    # this SQL statement will create a jokes table if a jokes table does not exist
    # the table has 2 columns with the datatype of TEXT
    conn.execute("CREATE TABLE IF NOT EXISTS jokes (setup TEXT, punchline TEXT)")
    # Commit the change to actually create the table
    conn.commit()
    #print("Joke table created")

# function to add a joke to the table
def add_joke(conn, joke_setup, joke_punchline):
    # this SQL statement will add a joke to the jokes table
    conn.execute("INSERT INTO jokes (setup, punchline) VALUES (?, ?) ", (joke_setup, joke_punchline))
     # Commit the change to actually create the table
    conn.commit()
    print("Joke was added")

# function to display all of the jokes in the jokes table
def display_all_jokes(conn):
    # this SQL statement will return all of the jokes
    cursor = conn.execute("SELECT setup, punchline FROM jokes")

    # variable to hold all of the jokes
    all_the_jokes = ""

    # loop through all of the records returned from the select statement - they are sitting in the cursor variable
    for row in cursor:
        all_the_jokes += f"Joke Setup: {row[0]}"
        all_the_jokes += f"Joke Punchline: {row[1]}"
        
    return all_the_jokes

# TODO: make this function do something
def add_joke_clicked():
    
    print(f"all the jokes: {display_all_jokes(conn)}")


# Create a connection to the database; if the database does not exist, it will be created
conn = sqlite3.connect("jokes.db")

# Make sure the table exists
create_table(conn)

# add a joke for testing
add_joke(conn, "Just because you don't know the meaning of the word Armageddon... ", "...it's not the end of the world")

# display the jokes
display_all_jokes(conn)

# create the main window
root = tk.Tk()
# give the main window a title
root.title("Jokes App")

# Create a label to show the Joke Setup text and introduce the textbox 
setup_label = tk.Label(root, text="Joke Setup:")
# Let's add the label to our window using the grid layout
setup_label.grid(row=0, column=0) # first row and first column

# Create the textbox to gather the joke setup from the user
setup_textbox = tk.Entry(root, width=50)
# Add the textbox to our window using the grid layout
setup_textbox.grid(row=0, column=1) # first row and second column


# Create a label to show the Joke Punchline text and introduce the textbox 
punchline_label = tk.Label(root, text="Joke Punchline:")
# Add the label in the second row, and first column
punchline_label.grid(row=1, column=0)

# Create the textbox to gather the joke punchline from the user
punchline_textbox = tk.Entry(root, width=50)
# Add the textbox to our window using the grid layout
punchline_textbox.grid(row=1, column=1)

# Create a button to add the new joke to the database
add_joke_button = tk.Button(root, text="Add Joke", command=add_joke_clicked)
# Add the button to our window using the grid layout
add_joke_button.grid(row=2, column=0)

# Create a frame to hold a scrollable text area for displaying the jokes
jokes_frame = tk.Frame(root)
# Add the frame using the grid layout
jokes_frame.grid(row=3, column=0, columnspan=2, sticky="nsew")

# Create the text area to hold the jokes
jokes_text = tk.Text(jokes_frame, wrap="word") # so the words wrap if needed
# Add the frame using the grid layout
jokes_text.grid(row=0, column=0, sticky="nsew")



# start the main window
root.mainloop()