with open('example.txt', 'w') as file:
    file.write("Hello, world!\n")
    
    lines = ["This is line 1.\n", "This is line 2.\n", "This is line 3.\n"]
    file.writelines(lines)

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print("Full content:\n", content)

with open('example.txt', 'r') as file:
    first_line = file.readline()
    print("First line:", first_line)

    second_line = file.readline()
    print("Second line:", second_line)
