def file_stats(filename):
    chars = 0
    words = 0
    lines = 0
    with open(filename, 'r') as file:
        for line in file:
            lines += 1
            chars += len(line)
            words += len(line.split())
    return chars, words, lines

filename = 'example.txt'
characters, word_count, line_count = file_stats(filename)
print(f"Characters: {characters}")
print(f"Words: {word_count}")
print(f"Lines: {line_count}")