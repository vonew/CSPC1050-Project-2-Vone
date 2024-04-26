from player import Player
from map import Map
from artifact import Artifact

class Game: # where the game will be executed 
    def __init__(self): 
        self.player = None # initializing player
        self.map = Map() # calling the map class  
        self.locations = "forest" # setting forest as starting location
        self.game_over = False # indicating whether game is over
    
    def start(self): # starting the game with 3 descriptions
        print("Welcome to The Quest for the Powerful Artifacts!")
        print("You will embark on a journey to different biomes to solve riddles in order to discover powerful artifacts.")
        print("Let's see if you can collect all of the artifacts, good luck!")
        self.player = Player(input("Enter your name: ")) # player enters name 

    def play(self):
        while not self.game_over: # while game is not over
            self.show_location() # displaying current location
            self.input_choice() # choices for interacting with game so the player can choose
    
    def show_location(self): 
        location_info = self.map.get_location(self.locations) # calling location from map file
        print("\n" + location_info["description"]) # printing location description from map file in dictionary 
        print("What would you like to do?") # asking player about their next action
        print("1. Solve the riddle") # choice 1
        print("2. Move to a different location.") # choice 2
        print("3. Check inventory") # choice 2 

    def input_choice(self): # function where player inputs coice 
        choice = input("Enter your choice by typing in the numbers 1,2, or 3 based on the list of choices below: ").strip()
        if choice == "1": 
            self.solve_riddle() # solving the riddle
        elif choice == "2":
            self.move_location() # moving to a different location 
        elif choice == "3":
            self.player.show_inventory() # checking/showing inventory 
        else:
            print("Invalid choice. Try again.") # if player types something other than 1,2, or 3

    def solve_riddle(self): # function for solving riddle
        location_info = self.map.get_location(self.locations) 
        print("Here's the riddle: ") 
        print(location_info["riddle"]) # printing riddle from location dictionary 
        answer = input("Enter your answer: ").lower().strip() # where player types their answer

        if answer == location_info["answer"].lower(): # checking if the answer is correct
            artifact_type = location_info["artifact"] # getting the specific artifact
            artifact = Artifact(artifact_type) # assigns specific artifact to Artifact class
            print("Correct! You found the", artifact) # printing what you found 
            self.player.add_to_inventory(location_info["artifact"]) # adding artifact found by player to inventory 
            del self.map.locations[self.locations] # deleting the location from the map
            with open('outputlog.txt', 'a') as log: # opening and appending artifact to outputlog text
                log.write(f"Found: {artifact_type}\n") # writing Found: --> for each artifact type
            if not self.map.locations: # if all locations were found
                self.game_over = True # game is over  
                print("Congratulations! You have collected all of the powerful artifacts and won the game!") # description for when game is over
                with open('outputlog.txt', 'r') as log: # reading txt 
                    contents = log.read() 
                print(contents) # printing artifacts found after game is completed
            else:
                self.move_location() #moving to another location
        else:
            self.wrong_answer() # if answer is incorrect, offer and hint or enter anything to try again 

    def wrong_answer(self): # function for incorrect answer 
        location_info = self.map.get_location(self.locations) 
        print("Incorrect! Would you like a hint?") # asking for hint
        hint_choice = input("Enter 'yes' for a hint or any key to try again: ") # asking if they want a hint or to try again

        if hint_choice == 'yes': # if they type yes for a hint
            print("Hint:", location_info["hint"]) # print hint from location dictionary
        else:
            print("Here's the riddle again:") 
            print(location_info["riddle"]) # providing riddle again 

    def move_location(self): # moving location if player does not want to solve riddle
        print("Available locations left:")
        for location in self.map.locations: # for each location from location dictionary in the map file
            print("-", location.capitalize()) # capitalizes 1st letter of each location name only

        new_location = input("Enter the location you want to move to next: ").strip().lower() # entering next location 
        
        if new_location in ['forest', 'river', 'cave', 'mountain']: # if next location is in this list
            self.locations = new_location # allow player to enter that location
        else:
            print("Invalid location, try again.") # if new_location was not in the list provided 



    

