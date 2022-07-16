from json import JSONEncoder


class Codificador(JSONEncoder):

    def default(self, o):
        return o.__dict__
