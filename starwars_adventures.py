scenes = {
    "start": {
        "description":  "You are on a mission to deliver plans to the Rebel base. You land on Tatooine and must find a guide.",
        "choices": ["Look for Obi-Wan", "Head to the cantina"], 
        "results": "obiwan", "cantina"] 
    },
    "obiwan": { 
        "description": "You find Obi-Wan Kenobi. He agrees to help you.",
        "choices": ["Travel to the Rebel base", "Return to your ship"], 
        "results": ["win", "lose"]
    },
"cantina": {
    "description": "In the cantina, you encounter some unsavory types.", 
    "choices": ["Talk to the band", "Sit quietly in a corner"], 
    "results": ["band", "corner"]
},
"band": {
    "description": "The band knows someone who can help. You meet Han Solo.", "choices": ["Hire Han" "Decline his offer"].
    "results": ["win", "Lose"] 
	},
"corner": {
 "description": "You are noticed and questioned by Stormtroopers.",
 "choices": ["Fight" "Flee"],
 "results": ["lose", "Lose"] 
},
"win" :
“description”: "You successfully make it to the Rebel base. The galaxy is in your debt!", 
“choices”: [],
“results”: []
},
"lose": {
 "description": "You failed your mission. The galaxy is doomed!", 
"Choices":[]
 "Results": [] },