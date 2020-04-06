# Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("Otter", "Zebra", "Lion", "Tiger", "Panda", "Koala", "Bear", "Llama", "Bat", "Bird")

# Find one of your animals using the tuple.index(value) syntax on the tuple.
zoo.index("Panda")

# Determine if an animal is in your tuple by using value in tuple syntax.
animal_to_find = "Bear"
if animal_to_find in zoo:
    print(animal_to_find)

# You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
(animal1, animal2, animal3, animal4, animal5,animal6, animal7, animal8, animal9, animal10) = zoo

# print(animal1)
# print(animal2)
# print(animal3)
# print(animal4)
# print(animal5)
# print(animal6)
# print(animal7)
# print(animal8)
# print(animal9)
# print(animal10)

# Convert your tuple into a list.
zooAsList = list(zoo)

# Use extend() to add three more animals to your zoo.
moreAnimals = ["Kangaroo", "Monkey", "Hippo"]
zooAsList.extend(moreAnimals)

# Convert the list back into a tuple.
zoo = tuple(zooAsList)
