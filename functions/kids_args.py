def run(*kids):
    for kid in kids:
        print(f"{kid} ran like a fool!")

def swing(*kids):
    for kid in kids:
        print(f"{kid} swung on the swings!")

def slide(*kids):
    for kid in kids:
        print(f"{kid} slide down the slide")

def hide_and_seek(*kids):
    for kid in kids:
        print(f"{kid} loves playing hide and seek")

run("Pam", "Sam", "Andrea", "Will")
swing("Marybeth", "Jenna", "Kevin", "Courtney")
slide("Mike", "Jack", "Jennifer", "Earl")
hide_and_seek("Henry", "Heather", "Hayley", "Hugh")