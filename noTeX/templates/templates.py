import os
from pathlib import Path

from noTeX.dir.logger import NoTeXLogger
"""
    Class responsible for managing latex templates.

    TODO: add code template (artificial one)
"""
class NoTeXTemplates:
    # Potential template paths
    __dir = [str(NoTeXLogger.get_opt('templates'))]
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
    def get_template_entries(self):
        return self.__templates

    """
        Provide paths to each of the loaded templates

        :return: paths of all loaded templates
        :rtype: list (string)
    """
    def get_template_paths(self):
        paths = []
        for entry in self.__templates:
            paths.append(entry.path)
        return paths

    """
        Provide names of loaded templates.

        :return: names of all loaded templates
        :rtype: list (string)
    """
    def get_template_names(self):
        names = []
        for entry in self.__templates:
            names.append(entry.name)
        return names

    @staticmethod
    def get_template_path(template) -> os.PathLike:
        for entry in NoTeXTemplates.__templates:
            if entry.name == template:
                return entry.path
        return Path('.')

    def get_template_entry(self, template):
        for entry in self.__templates:
            if entry.name == template:
                return entry
