planet_list = ["Mercury", "Mars"]

# Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")

# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
last_planets = ["Uranus", "Neptune"]
planet_list.extend(last_planets)

# Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

# Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")

# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets. Mercury, Venus, Earth and Mars
rocky_planets = planet_list[slice(0, 4)]

# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
del planet_list[8]

print(f'Planet List: {planet_list}')
print(f'Rocky Planets: {rocky_planets}')


# CHALLENGE
# Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on.
spacecraft = [
    ("Cassini", "Saturn"),
    ("Viking", "Mars"),
    ("Mariner 1", "Venus"),
    ("Mariner 1", "Mars"), 
    ("Mariner 2", "Saturn"),
    ("Voyager 1", "Jupiter"),
    ("Voyager 1", "Saturn")
]


# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.
for planet in planet_list:
    satellites = []
    for tup in spacecraft:
        if planet == tup[1]:
            satellites.append(tup[0])

    if len(satellites) != 0:
        sats = ", ".join(satellites)
        print(f'{planet}: {sats}')

