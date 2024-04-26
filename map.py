class Map: # calling the Map class
    def __init__(self): # Going through each location
        # A dictionary for each biome with their description and riddles, etc.
        self.locations = {
            "forest": {
                "description": "You are dark and mysterious dense forest.",
                "riddle": "What has keys but can't open locks?", 
                "answer": "A piano", 
                "artifact": "Ancient pot filled with gold",
                "hint": "It's a musical instrument."}, 
            "cave": {
                "description": "You have entered a cave where mummies lay.", 
                "riddle": "What has 4 legs but can't run?", 
                "answer": "A chair", "artifact": "Crystal",
                "hint": "You need it to sit down."}, 
            "mountain": {
                "description": "You stand at the top of a steep mountain in the deep forest.",
                "riddle": "If you have me, you will want to share me. If you share me, you will no longer have me. What am I?",
                "answer": "A secret", "artifact": "Mystic Rock",
                "hint": "Think of something somebody told you that you could not tell."},
            "river": {"description": "You approach a flowing river with dirty, murky water.", 
                "riddle": "What always ends everything?",
                "answer": "A G", "artifact": "Holy Water",
                "hint": "It's a letter, don't think to hard."}}
    
    def get_location(self, location): # getting location
        if location:
            return self.locations[location] # retrieving location 