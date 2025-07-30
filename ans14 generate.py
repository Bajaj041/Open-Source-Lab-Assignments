def parse_csv(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            data.append(row)
    return data
