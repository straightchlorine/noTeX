import os

class NoTeXTemplates:
    __dir = []
    __templates = []

    def __init__(self, dirs = None):
        if dirs is not None:
            for entry in dirs:
                if '~' in entry:
                    entry = entry.replace('~', os.path.expanduser('~'))
                if os.path.lexists(entry):
                    self.__dir.append(entry)

        for dir in self.__dir:
            with os.scandir(dir) as it:
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
    templates = NoTeXTemplates([ '~/latex-template' ])
    print(templates.getpaths())
