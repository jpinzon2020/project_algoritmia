from pathlib import Path


class Writer:
    directory = Path(__file__).parent

    def create_program_report(self, content):
        file = '../data/programacion1.txt'
        filepath = (self.directory / file).resolve()

        vertices = len(content)

        with open(f'{filepath}', 'w') as f:
            f.write(f'{vertices}\n')

            i = 0
            for vertice in content:
                f.write(f'{i}\n')
                f.write(f'{len(vertice)}\n')

                for edge in vertice:
                    f.write(f'{edge[0]} {edge[1]}\n')

                i = i + 1

        f.close()

        return file
