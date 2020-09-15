import random

# Lists
subject = ["boy", "girl", "dog", "cat", "star", "horse", "sky", "rainbow", "sun", "moon"]
verb = ["love", "hate", "want", "fear", "desire", "draw", "dream", "feel", "fight", "leave"]
adjective = ["beautiful", "ugly", "big", "small", "shiny", "colorful", "misty", "hollow", "scary", "little"]

# Shuffle Lists
random.shuffle(subject)
random.shuffle(verb)
random.shuffle(adjective)

# An index to access the List element
index = 0

# An output text string
output = ""

# Generate four sentences
for i in range(4):
    # Start a sentence with The
    output += "The"

    # Add an optional adjective for the subject
    if random.choice([True, False]):
        output += " " + adjective[index % len(adjective)]
    
    # Add a subject
    output += " " + subject[index % len(subject)]

    # Add a verb
    output += " " + verb[index % len(verb)] + "s"

    # Increment the index
    index += 1
    
    # Add an optional adjective for the object
    if random.choice([True, False]):
        output += " " + adjective[index % len(adjective)]

    # Add an object
    output += " " + subject[index % len(subject)] + "s\n"
    
    # Increment the index
    index += 1
    
# Print the output    
print(output)