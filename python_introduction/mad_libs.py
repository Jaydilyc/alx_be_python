print("🎉 Welcome to Mad Libs! Let's build a silly story.\n")

# Collect user input
adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
adj3 = input("Enter one more adjective: ")
adj4 = input("Enter a final adjective: ")

animal = input("Enter an animal: ")

# Conditional twist
if animal.lower() == "lion":
    animal_description = "majestic"
else:
    animal_description = "mysterious"

# Build the story
story = f"""
On a beautiful {adj1} day, I went to the zoo.
I saw a funny {adj2} monkey swinging from the trees.
Then, I spotted a {animal_description} {animal} lounging in the sun.
Nearby was a {adj3} elephant spraying water everywhere.
What a wild and {adj4} experience!
"""

# Display the story
print("\n📖 Your Mad Libs Story:")
print(story)