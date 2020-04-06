# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.

def run(name):
    print(f"{name} ran like a fool!")

def swing(name):
    print(f"{name} swung on the swings!")

def slide(name):
    print(f"{name} slide down the slide")

def hide_and_seek(name):
    print(f"{name} loves playing hide and seek")

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

for kid in running_kids:
    run(kid)

for kid in swinging_kids:
    swing(kid)

for kid in sliding_kids:
    slide(kid)

for kid in hiding_kids:
    hide_and_seek(kid)