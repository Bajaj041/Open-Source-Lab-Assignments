from collections import Counter

def char_frequency(filename):
    with open(filename, 'r', errors='ignore') as file:
        content = file.read()
    freq = Counter(content)
    return freq

if __name__ == "__main__":
    filename = input("Enter filename: ")
    freq = char_frequency(filename)
    
    for char, count in freq.most_common():
        # Print printable characters, else their ASCII code
        if char.isprintable() and char != '\n':
            print(f"'{char}': {count}")
        elif char == '\n':
            print(f"\\n: {count}")
        else:
            print(f"ASCII {ord(char)}: {count}")
