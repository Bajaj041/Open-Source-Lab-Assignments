import textwrap

def wrap_file(filename, width):
    with open(filename, 'r') as file:
        for line in file:
            wrapped_lines = textwrap.wrap(line.rstrip('\n'), width=width)
            for wrapped_line in wrapped_lines:
                print(wrapped_line)

wrap_file("example.txt", 10);