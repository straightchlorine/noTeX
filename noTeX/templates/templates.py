import os
from pathlib import Path

from noTeX.dir.logger import NoTeXLogger

"""
    1. template manager of some sort
    2. documentation after finishing
    3. maybe assign parameters to each template in logger
        class so you can have predefined settings for each
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

    def get_template_entries(self):
        return self.__templates

    def get_template_paths(self):
        paths = []
        for entry in self.__templates:
            paths.append(entry.path)
        return paths

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
