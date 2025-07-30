def print_lines_in_reverse(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in reversed(lines):
        print(line, end='')

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    print_lines_in_reverse(filename)
