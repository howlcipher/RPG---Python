import character
import csv

class menu:
    def __init__(self):

        print("Welcome to RPG\n-----")
        #need a function for each menu item and loop back to menu if "quit" is not selected
        menu_items(self)
        user_choice = input("Please make a selection: ")
        #change to while loop - loop till quit option is true
        if user_choice == "1":
            nc = character_create(self)
            print(nc)
        elif user_choice == "2":
            try:
              #open csv file and create using csv
              "Displaying Character"
              print(nc)
            except:
              print("No character found, please create or load")
              menu()
        elif user_choice == "3":
            save_character(self)
        elif user_choice == "4":
            load_character(self)
        elif user_choice == "5":
            print("Thanks For Playing!  Goodbye!")

        else:
            print("Please make a numerical selection 1 - 5")
            menu()

def character_create(self):
            print("Creating Character")
            #if true creates a character
            nc = character.Character()
            ds=(character.display_character(nc))
            #displays character
            print(ds)
            #saves character
            save_character(nc)
            #return to menu
            menu()

#display menu items
def menu_items(self):
    print("1. Create Character")
    print("2. Display Character")
    print("3. Save Character")
    print("4. Load Character")
    print("5. Quit\n-----")


#consider using JSON instead of csv
#save a character
def save_character(self):
  print("saving...")
  #use self.name, self.job...etc
   #save to csv
  fields = ["name", "job", "strength", "dexterity", "constitution", "wisdom", "intellegence"]
  rows = [[self.name, self.job, str(self.Strength), str(self.Dexterity), str(self.Constitution), str(self.Wisdom), str(self.Intelligence)]]

  #save file name
  filename = "character.csv"

  # writing to csv file 
  with open(filename, 'w') as csvfile: 
      # creating a csv writer object 
      csvwriter = csv.writer(csvfile) 
        
      # writing the fields 
      csvwriter.writerow(fields) 
        
      # writing the data rows 
      csvwriter.writerows(rows)


#load a character
def load_character(self):
  print("loading...")