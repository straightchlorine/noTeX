import os

"""
    Class responsible for managing latex templates.
"""
class NoTeXTemplates:
    # Potential template paths
    __dir = []
    # DirEntry objects containing the templates
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

    """
        Provide raw DirEntry objects corresponding to each of the templates.

        :return: DirEntry objects of all loaded templates
        :rtype: list (DirEntry)
    """
    def getentries(self):
        return self.__templates

    """
        Provide paths to each of the loaded templates

        :return: paths of all loaded templates
        :rtype: list (string)
    """
    def getpaths(self):
        paths = []
        for entry in self.__templates:
            paths.append(entry.path)
        return paths

    """
        Provide names of loaded templates.

        :return: names of all loaded templates
        :rtype: list (string)
    """
    def getnames(self):
        names = []
        for entry in self.__templates:
            names.append(entry.names)
        return names

if __name__ == "__main__":
    templates = NoTeXTemplates([ '~/latex-template' ])
    print(templates.getpaths())
