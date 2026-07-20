#import the random module
import random

#subject
subjects = [
    "shahrukh khan",
    "virat kholi",
    "A mumbai cat",
    "A group of monkey",
    "david Raj",
    "prime minsister modi",
]

#action
action =[
    "dances with",
    "cancels",
    "eating",
    "orders",
    "celebration",
    "launches",
]

#palce or things
places_or_thing =[
    "AT red fort",
    "inside parliment",
    "in cricket ground",
    "at ganga ghat",
    "in mumbai local train",
    "a plate of samosa",
    "during IPL match",
]

emojis = ["😂", "🔥", "🎉", "🐒", "🐱", "🏏"]
#while loop
while True:
    subject = random.choice(subjects)
    actions = random.choice(action)
    places_or_things = random.choice(places_or_thing)

    headline = f"BREAKING NEW : {subject} {actions} {places_or_things} {random.choice(emojis)}"
    print("\n" + headline)
    


    user_input = input("\n Do you want another headline ? (yes/no):").strip().lower()
    if user_input == "no":
        break

#print goodbye message
print("\n Thanks for using the fake Headline generator .Have a fun day " )