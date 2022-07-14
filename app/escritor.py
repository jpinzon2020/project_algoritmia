from pathlib import Path


class Escritor:
    directorio = Path(__file__).parent

    def create_program_report(self, contenido):
        archivo = '../data/programacion1.txt'
        ruta_archivo = (self.directorio / archivo).resolve()

        vertices = len(contenido)

        with open(f'{ruta_archivo}', 'w') as f:
            f.write(f'{vertices}\n')

            i = 0
            for vertice in contenido:
                f.write(f'{i}\n')
                f.write(f'{len(vertice)}\n')

                for arista in vertice:
                    f.write(f'{arista[0]} {arista[1]}\n')

                i = i + 1

        f.close()

        return archivo
