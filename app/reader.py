from pathlib import Path


class Reader:
    directory = Path(__file__).parent

    def read_journeys(self, file):
        i = 0
        filepath = (self.directory / file).resolve()
        with open(f'{filepath}', 'r') as f:
            for line in f:
                values = line.split()

                if i == 0:
                    journeys = [None] * int(values[0])
                else:
                    journeys[i - 1] = values

                i = i + 1

        return journeys



