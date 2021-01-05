# poetrygen


## Description
This repo is the week1 assignment of the Reading and Writing Electronic Text course at ITP.

The assignment is to create my own poetry generator using straightforward string manipulation techniques (e.g. concatenation, splitting, joining, indexing, etc.) in Python.

Here's the [implementations of early and well-known poetry generators](https://github.com/aparrish/rwet/blob/master/some-poetry-generators.ipynb) which we can use as a reference.

I was inspired by the "Love Letter Generator" by by Christopher Strachey and decided to take a similar approach to form a sentence.

Here's my full Python code:

```
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
```
And here's an example output:
```
The boy desires small horses
The ugly sky dreams shiny cats
The misty girl loves rainbows
The hollow sun hates stars
```

As you can see, it basically generates four sentences that are built in the following format:

```
The + (optional adjective) + subject + verb + (optional adjective) + object
```

I tried to avoid repeating of words by incrementing the index to access the shuffled List element.

It was a great learning experience to familiarize myself with Python string manipulations.

## Setup
1. Installation of python3 is required. Follow [this guide](https://realpython.com/installing-python/) to install it.
2. Run the following commands in the Terminal.
```
git clone https://github.com/cuinjune/poetrygen.git
cd poetrygen
python3 poetrygen.py
```

## Author
* [Zack Lee](https://www.cuinjune.com/about): MPS Candidate at [NYU ITP](https://itp.nyu.edu).


