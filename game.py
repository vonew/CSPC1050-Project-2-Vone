from player import Player
from map import Map
from artifact import Artifact

class Game: # where the game will be executed 
    def __init__(self):
        self.player = None
        self.map = Map() # calling the map class  
        self.locations = "forest" # forest as starting location
        self.game_over = False 
    
    def start(self):
        print("Welcome to The Quest for the Powerful Artifacts!")
        print("You will embark on a journey to different biomes to solve riddles in order to discover powerful artifacts.")
        print("Let's see if you can collect all of the artifacts, good luck!")
        self.player = Player(input("Enter your name: ")) # player enters name 

    def play(self):
        while not self.game_over: # while game is not over
            self.show_location() # displaying location
            self.input_choice() # choices for interacting with game
        self.print_outputlog
    def show_location(self):
        location_info = self.map.get_location(self.locations)
        print("\n" + location_info["description"]) # printing location description
        print("What would you like to do?")
        print("1. Solve the riddle")
        print("2. Move to a different location.")
        print("3. Check inventory")

    def input_choice(self):
        choice = input("Enter your choice by typing in the numbers 1,2, or 3 based on the list of choices below: ")
        if choice == "1":
            self.solve_riddle()
        elif choice == "2":
            self.move_location()
        elif choice == "3":
            self.player.show_inventory()
        else:
            print("Invalid choice. Try again.")

    def solve_riddle(self):
        location_info = self.map.get_location(self.locations)
        print("Here's the riddle: ")
        print(location_info["riddle"])
        answer = input("Enter your answer: ").lower()

        if answer == location_info["answer"].lower():
            artifact_type = location_info["artifact"]
            artifact = Artifact(artifact_type)
            print("Correct! You found the", artifact)
            self.player.add_to_inventory(location_info["artifact"])
            del self.map.locations[self.locations]
            with open('outputlog.txt', 'a') as log:
                log.write(f"Found: {artifact_type}\n")
            if not self.map.locations:
                self.game_over = True
                print("Congratulations! You have collected all of the powerful artifacts and won the game!")
            else:
                self.move_location()
        else:
            self.wrong_answer()

    def print_outputlog(self):
        print(" End of Game Log:")
        try:
            with open('outputlog.text', 'r') as log:
                print(log.read())
        except FileNotFoundError:
            print("outputlog.txt cannot be found.")

    def wrong_answer(self):
        location_info = self.map.get_location(self.locations)
        print("Incorrect! Would you like a hint?")
        hint_choice = input("Enter 'yes' for a hint or any key to try again: ")

        if hint_choice == 'yes':
            print("Hint:", location_info["hint"])
        else:
            print("Here's the riddle again:")
            print(location_info["riddle"])

    def move_location(self): # moving location if player does not want to solve riddle
        print("Available locations left:")
        for location in self.map.locations:
            print("-", location.capitalize()) # capitalizes 1st letter of each location name only

        new_location = input("Enter the location you want to move to next: ").strip().lower() # entering next location 
        
        if new_location in ['forest', 'river', 'cave', 'mountain']: # if new_location in ['forest', 'river', 'cave', 'mountain']
            self.locations = new_location
        else:
            print("Invalid location, try again.")



    

