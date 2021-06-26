import wikipedia

def give_details(monument):
    s = wikipedia.summary(monument, sentences = 4)
    return s
