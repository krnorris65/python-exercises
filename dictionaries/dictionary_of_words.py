# """
# Create a dictionary with key value pairs to
# represent words (key) and its definition (value)
# """
word_definitions = dict()

# """
# Add several more words and their definitions
#    Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
# """

word_definitions["Sad"] = "The feeling Ada has when she has to be in the crate all day"
word_definitions["Mad"] = "The feeling Ada has when she has to take a bath"
word_definitions["Happy"] = "The feeling Ada has when she gets to go to the dog park"

# """
# Use square bracket lookup to get the definition of two
# words and output them to the console with `print()`
# """
print(word_definitions["Sad"])

# """
# Loop over the dictionary to get the following output:
#     The definition of [WORD] is [DEFINITION]
#     The definition of [WORD] is [DEFINITION]
#     The definition of [WORD] is [DEFINITION]
# """
for(key, value) in word_definitions.items():
    print(f"{key}: {value}")
