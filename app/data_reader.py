def read_journeys(file):
    i = 0
    with open(file, 'r') as f:
        for line in f:
            values = line.split()

            if i == 0:
                journeys = [None] * int(values[0])
            else:
                journeys[i - 1] = values

            i = i + 1

    return journeys

print(read_journeys('../data/trayectos.txt'))

