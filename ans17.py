from collections import defaultdict

def find_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagram_dict[key].append(word)
    
    return [group for group in anagram_dict.values() if len(group) > 1]

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
anagrams = find_anagrams(words)
print(anagrams)
