import string

def mutate(word):
    letters = string.ascii_lowercase
    mutations = set()
    
    for i in range(len(word) + 1):
        for c in letters:
            mutations.add(word[:i] + c + word[i:])
    
    for i in range(len(word)):
        mutations.add(word[:i] + word[i+1:])
    
    for i in range(len(word)):
        for c in letters:
            if word[i] != c:
                mutations.add(word[:i] + c + word[i+1:])
    
    for i in range(len(word) - 1):
        if word[i] != word[i+1]:
            swapped = (word[:i] + word[i+1] + word[i] + word[i+2:])
            mutations.add(swapped)
        mutations.discard(word)
    
    return mutations