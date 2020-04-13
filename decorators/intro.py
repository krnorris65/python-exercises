def reversal(sentence_func):
    def reversed_sentence(*args, **kwargs):
        original_sentence = sentence_func(*args, **kwargs)
        return f"Reversed: {''.join(reversed(original_sentence))}"
    return reversed_sentence


@reversal
def letterPress():
    return "Adaptogen tote bag drinking vinegar, letterpress pabst locavore migas hella"


def taxidermy():
    return "Taxidermy health goth locavore, pickled post-ironic pork belly kale chips tofu PBR&B bicycle rights"


@reversal
def mustache():
    return "Umami hexagon stumptown enamel pin, mustache echo park readymade celiac"


def lumberSexual():
    return "Jean shorts lumbersexual stumptown tumeric everyday carry readymade"


print(letterPress())
print(taxidermy())
print(mustache())
print(lumberSexual())
