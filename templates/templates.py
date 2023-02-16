import os

class NoTeXTemplates:
    __dir = os.path.join(os.path.expanduser('~'), 'latex-template')
    __templates = []

    def __init__(self):
        with os.scandir(self.__dir) as it:
            for entry in it:
                if entry.is_dir() and not entry.name == '.git':
                    self.__templates.append(entry)

    def getentries(self):
        return self.__templates

    def getpaths(self):
        paths = []
        for entry in self.__templates:
            paths.append(entry.path)
        return paths

    def getnames(self):
        names = []
        for entry in self.__templates:
            names.append(entry.names)
        return names

if __name__ == "__main__":
    templates = NoTeXTemplates()
    print(templates.getpaths())
