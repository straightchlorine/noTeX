"""
    Note class - base class of every single created note.
"""

from noTeX.notes.subjects import NoTeXSubjects
from noTeX.templates.templates import NoTeXTemplates
from noTeX.utility.utils import NoTeXUtility

from os import DirEntry
import os
from datetime import datetime


class NoTeXNote:
    # Identifies the note - for now it is simply the number of
    # notes currently in the directory.
    __id = None
    # Where the note belongs (if there are multiple trees)
    __path = None
    # Creation date (also in the name of the folder)
    __date = None

    # Type of the note (for example lecture or tutorial)
    __type : str
    # Chosen template
    __template : str
    # Chosen template
    __template_path : str
    # What is the note about (for example physics or mathematics)
    __subject : str
    # What is the note about (for example physics or mathematics)
    __subject_path : str

    def __init__(self, subject, note_type, template):
        temp_subjects = NoTeXSubjects()
        temp_templates = NoTeXTemplates()

        print(subject, note_type, template)

        self.__subject = subject
        self.__subject_path = str(temp_subjects.get_subject_path(subject))
        self.__type = note_type
        self.__template = template
        self.__template_path = str(temp_templates.get_template_path(template))

        self.create_path()

    def create_path(self):
        print(self.__subject_path)
        print(self.__template_path)
        base_path = os.path.join(self.__subject_path, self.__type)

        if not os.path.exists(base_path):
            os.mkdir(base_path)

        os.chdir(base_path)
        id = NoTeXUtility.get_dir_size(base_path)
        self.__id = id
        date = datetime.today().strftime('%a-%d-%b-%Y')

        new_dir = str(id) + '-' + date + '-' + self.__template
        new_path = os.path.join(base_path, new_dir)
        os.mkdir(new_path)
        os.chdir(new_path)

        os.system('cp ' + self.__template_path + '/*.tex .')
        os.rename('template.tex', str(date + '.tex'))
