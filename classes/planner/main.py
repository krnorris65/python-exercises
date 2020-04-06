from building import Building
from city import City

main = Building("123 Main St", 3)
sky = Building("23 Sky Drive", 5)
jones = Building("2839 Jones Rd", 1)
dogwood = Building("2039 Dogwood Lane", 2)
porter = Building("2938 Porter Rd", 3)

megalopolis = City("Megalopolis")

megalopolis.add_building(main)
megalopolis.add_building(sky)
megalopolis.add_building(jones)
megalopolis.add_building(dogwood)
megalopolis.add_building(porter)

for building in megalopolis.buildings:
    print(building.address)