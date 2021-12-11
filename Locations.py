def location_data():
    location_data = {
        "Shire": {
            "Location":"The Shire",
            "Description": "The Shire is where Frodo, Sam, Bilbo, and the other Hobbits live. They love food, Ale, and the smoking of pipe-weed. The local is hilly with lots of trees and homes made out of holes in the ground.",
            "Items_required": [],
            "Items": [],
            "Directions": {
                "Right": "Bree"
            },
            "Win":False,
            "Villian":False,
            "Lose_Description":False
        },
        "Bree": {
            "Location":"Bree",
            "Description": "The land of the big folk. Bree is infamous for its pubs, and the wide array of people that visit. Here Frodo and Sam are waiting for further instruction from Gandalf indicating what they need to do next.",
            "Items_required": [],
            "Items": [
                "Gandalf",
                "One Ring"
            ],
            "Directions": {
                "Right": "Rivendell",
                "Down": "Brandywine Bridge",
                "Left": "Shire"
            },
            "Win":False,
            "Villian":False,
            "Lose_Description":False
        },
        "Rivendell": {
            "Location":"Rivendell",
            "Description": "The land of the beloved Elves. Here is where the great warrior Elrond lives with his family. Though the Elves have resided in Middle Earth for generations, they have been slowly leaving Middle Earth in search for a new land",
            "Items_required": [],
            "Items": [
                "Fellowship"
            ],
            "Directions": {
                "Right": "Moria",
                "Down": "Isengard",
                "Left": "Bree"
            },
            "Win":False,
            "Villian":False,
            "Lose_Description": False
        },
        "Moria": {
            "Location":"Moria",
            "Description": "Moria, it is here where the Dwarves delved too greedily and too deep. They have awoken the demon from the deep, The Balrog. \n\ndeeper and deeper you go into the mine, taking a Left turn, then a Right, then a Left, then another Left and finally you take one fateful Right turn which takes you to a point on the path where there are three possible directions. However, Gandalf doesn't know which way to go....,",
            "Items_required": [
                "Gandalf",
                "Fellowship"
            ],
            "Items": [],
            "Directions": {
                "Right": "Path on the Right",
                "Down": "Rivendell",
                "Left": "Path on the Left"
            },
            "Win":False,
            "Villian":False,
            "Lose_Description":False
        },
        "Path on the Left": {
            "Location":"Lorien",
            "Description": "Welcome to Lorien, the wooded areas where Lady Galadriel lives along with her Elven Kin. She has been watching over you as you progress on your journey, though she is wondering where Gandalf is.",
            "Items_required": [],
            "Items": [],
            "Directions": {
                "Up": "Moria",
                "Down": "Rohan"
            },
            "Win":False,
            "Villian":False,
            "Lose_Description":False
        },
        "Isengard": {
            "Location":"Isengard",
            "Description": "As you sneak by Isengard, you notice the White Wizard keeping a close lookout on top of the mysterious tower in the middle. It's best to keep a distance",
            "Items_required": [],
            "Items": [],
            "Directions": {
                "Up": "Rivendell",
                "Right": "Rohan"
            },
            "Win":False,
            "Villian":False,
            "Lose_Description": False
        },
        "Rohan": {
            "Location":"Rohan",
            "Description": "Welcome to Rohan. The land of the Horsemen. This is where Theoden, King of the Mark, lives with his family Eomer and Eowyn. As you pass through, they muster the Rohirrim to support you in your journey",
            "Items_required": [
                "Fellowship"
            ],
            "Items": [
                "Rohirrim"
            ],
            "Directions": {
                "Up": "Lorien",
                "Right": "Gondor",
                "Left": "Isengard"
            },
            "Win":False,
            "Villian":False,
            "Lose_Description": False
        },
        "Gondor": {
            "Location":"Gondor",
            "Description": "The kingdom of men. Aragorn, son of Arathorn, and King of Gondor greets you as you progress on your quest. He is supportive and wishes for your success. He decides to join you as you head towards the Mount Doom in Mordor.",
            "Items_required": [],
            "Items": [
                "Aragorn"
            ],
            "Directions": {
                "Right": "Path to Mordor",
                "Left": "Rohan"
            },
            "Win":False,
            "Villian":False,
            "Lose_Description":False
        },
        "Path to Mordor": {
            "Location":"Path to Mordor",
            "Description": "'Halt!' calls out Aragorn. 'A Nazgul approaches' What does the team decide to do?",
            "Items_required": [],
            "Items": [],
            "Directions": {
                "Up": "Do Nothing",
                "Right": "Hide",
                "Down": "Path of the Dead",
                "Left": "Gondor"
            },
            "Win":False,
            "Villian":False,
            "Lose_Description":False
        },
        "Hide": {
            "Location":"Hide",
            "Description": "Shh! You mustn't make a sound... \nWhile you are hiding, you notice a skulking creature heading closer to you. Is he a servant of darkness? Alas, it's Smeagol. He is wishing to assist in the journey, However, you have your suspicions.",
            "Items_required": [],
            "Items": [
                "Smeagol"
            ],
            "Directions": {
                "Right": "Continue to Mordor",
                "Left": "Gondor"
            },
            "Win":False,
            "Villian":False,
            "Lose_Description":False
        },
        "Continue to Mordor": {
            "Location":"Mordor",
            "Description": "The Black Gate of Mordor! The groUp has gotten so close, but the Black Gate of Mordor seems all but impenetrable. Beside you, Smeagol offers an alternative choice... To take the Grimold road, and Up the secret stairs...",
            "Items_required": [
                "Rohirrim",
                "Aragorn",
                "Smeagol"
            ],
            "Items": [],
            "Directions": {
                "Up": "Mount Doom",
                "Down": "Smeagol's alternative"
            },
            "Win":False,
            "Villian":False,
            "Lose_Description": False
        },
        "Mount Doom": {
            "Location":"Mount Doom",
            "Description": "You have arrived and the time has come for you to cast the ring into the fire. What do you do?",
            "Items_required": [
                "One Ring"
            ],
            "Items": [],
            "Directions": {
                "Up": "Cast the Ring into the Fire",
                "Down": "The ring is Mine!"
            },
            "Win":False,
            "Villian":False,
            "Lose_Description": False
        },
        "Cast the Ring into the Fire": {
            "Location":"Cast the Ring into the Fire",
            "Description": "Congratulations you are the winner! You will now sail off into the west with Gandalf the White, Elrond, Bilbo, and a whole host of other elves that you do not know",
            "Items_required": [],
            "Items": [],
            "Directions": {
                "Up": "You Win"
            },
            "Win":True,
            "Villian":False,
            "Lose_Description":False
        },
        "Brandywine Bridge": {
            "Location":"Brandywine Bridge",
            "Description": "You have arrived at the Brandywine bridge. As you decide what to do next, you notice a hooded figure approaching. .",
            "Items_required": [],
            "Items": [],
            "Directions": {
                "Up": "Game Over"
            },
            "Win":False,
            "Villian":True,
            "Lose_Description": "But it's too late, the hooded figure captured you and took you bound to the Dark Lord Sarun all hope has faded as the dark powers continue to take over"
        },
        "Path on the Right": {
            "Location":"Moria",
            "Description": "Run! It's the Balrog",
            "Items_required": [],
            "Items": [],
            "Directions": {
                "Up": "Game Over"
            },
            "Win":False,
            "Villian":True,
            "Lose_Description": "The Balrog has defeated you by slaughtering the entire fellowship and taking the One Ring for itself"
        },
        "Do Nothing": {
            "Location":"Do Nothing",
            "Description": "You have decided to do nothing",
            "Items_required": [],
            "Items": [],
            "Directions": {
                "Up": "Game Over"
            },
            "Win":False,
            "Villian":True,
            "Lose_Description": "The Nazgul has captured you and took you bound to the Dark Lord Sarun all hope has faded as the dark powers continue to take over"
        },
        "Path of the Dead": {
            "Location":"Path of the Dead",
            "Description": "You Lose!",
            "Items_required": [],
            "Items": [],
            "Directions": {
                "Up": "Game Over"
            },
            "Win":False,
            "Villian":True,
            "Lose_Description": "This is the story of Frodo and the One Ring of Power, Not the story of how Aragorn ascended to the throne of Gondor."
        },
        "Smeagol's alternative": {
            "Location":"Smeagol's alternative suggestion",
            "Description": "You Lose",
            "Items_required": [],
            "Items": [],
            "Directions": {
                "Up": "Game Over"
            },
            "Win":False,
            "Villian":True,
            "Lose_Description": "Because you listened to Smeagol, you ended Up taking signifacantly more time in your quest to destroy the ring. As a result, Sarun destroyed Gondor, Saruman Destroyed Rohan, and Smeagol lured you into Shelobs Lair where you are poked, spun into a web, and all life is sucked out of you."
        },
        "The Ring is Mine": {
            "Location":"The Ring is mine",
            "Description": "You Lose",
            "Items_required": [],
            "Items": [],
            "Directions": {
                "Up": "Game Over"
            },
            "Win":False,
            "Villian":True,
            "Lose_Description": "Because you took the ring, you ended Up living a very short life. In your idiocy of putting the ring on your finger, Sarun - who was literally in the same reagion as you - quickly found you, killed you, took the ring, and destroyed Middle Earth. All hope has faded and all Hobbits are no more."
        }
    }

    return location_data