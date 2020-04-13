def kids(chore_func):
    def kids_chore():
        original_output = chore_func()
        return f"{original_output} by the kids"
    return kids_chore

def mom(chore_func):
    def moms_chore():
        original_output = chore_func()
        return f"{original_output} by Mom"
    return moms_chore
    
def dad(chore_func):
    def dads_chore():
        original_output = chore_func()
        return f"{original_output} by Dad"
    return dads_chore

def laundry():
    return "The dirty laundry was cleaned"

@kids
def garbage():
    return "The garbage was taken out"

@dad
def dust():
    return "The house was dusted"

@mom
def groom():
    return "The dog was brushed"

print(laundry())
print(garbage())
print(dust())
print(groom())