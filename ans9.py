def print_each_line_reversed(filename):
    with open(filename, 'r') as file:
        for line in file:
            # Remove trailing newline, reverse the line, then print
            print(line.rstrip('\n')[::-1])

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    print_each_line_reversed(filename)
