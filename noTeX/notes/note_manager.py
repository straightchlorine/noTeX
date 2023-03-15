#!/usr/bin/python

import os
from datetime import datetime
from noTeX.dir.logger import NoTeXLogger

from noTeX.exceptions.exc import NoSubjectPathException
from noTeX.notes.subjects import NoTeXSubjects
from noTeX.utility.utils import NoTeXUtility

class NoTeXNoteId:
    """
    Class provides identification string for each created note,
    in order to quickly find and navigate to given note.

    Attributes
    ----------
    __note_main_root : os.PathLike
    __note_subject : str
    __note_type : str
    __note_template : str
    __id : str

    Methods
    -------
    get_id():
        Returns the id of the note.

    TODO
    ____
    1. id string initial idea: <main_root>:<subject>:<type>:<internal_id>
    2. export each id to config and import it from config as well
    """
    # path to the root of the note directory, a the very top of the hierarchy
    __note_main_root : os.PathLike
    #name of the subject, which note concerns
    __note_subject : str
    # type of the note (lecture/tutorial/code)
    __note_type : str
    # chosen template of the note
    __note_template : str
    # final identification string representing the note
    __id : str

    def __init__(self,
            note_main_root,
            note_subject,
            note_type,
            note_template):

        self.__note_main_root = note_main_root
        self.__note_subject = note_subject
        self.__note_type = note_type
        self.__note_template = note_template
        self.__make_id()

    def __make_id(self):
        """Function generates the id, called in the constructor.

        For now, it simply assigns (number_of_directories_in_path) + 1.
        """
        self.__id = str(NoTeXUtility.get_dir_size(
                        os.path.join(self.__note_main_root,
                                    self.__note_subject,
                                    self.__note_type)))

    def get_id(self):
        """
        Getter, provides the id for outside use.

        Returns
        -------
        id
            final identification string
        """
        return self.__id


class NoTeXNoteManager:
    """
    Class responsible for creating notes.

    Methods
    -------
    create_note():
        Returns the id of the note.

    TODO: proper management
    1. needs to create the note (base functionality for now)
    2. needs to create the id of the note (for future navigation)
    """

    @staticmethod
    def __make_note_path(note_subject, note_type, note_template):
        """
        Function builds and creates directory for new note.

        Path consists of:
            <path_to_subject_directory>/
                <[id]-[creation_date]-[chosen_template]>
        Where id is (for now) number of directories in the path + 1.

        Parameters
        ----------
        note_subject : str
            subject of the note
        note_type : str
            type of the note
        note_template : str
            template selected for the note
        """
        # subject path
        s_path = NoTeXSubjects.getpath(note_subject)
        if s_path is None:
            raise NoSubjectPathException('Subject path missing.')

        # base for the note path (starting with subject path)
        path = os.path.join(s_path, note_type)
        if os.path.exists(path):
            os.mkdir(path)

        # creating id object
        note_id = NoTeXNoteId(NoTeXLogger.get_opt('root'),
                              note_subject,
                              note_type,
                              note_template)

        # creating name for the directory
        internal_id = note_id.get_id()
        dir_name = str(internal_id) + '-'                        \
                + datetime.today().strftime('%a-%d-%b-%Y') + '-' \
                + note_template
        path = os.path.join(path, dir_name)

        os.mkdir(path)

    @staticmethod
    def create_note(note_subject, note_type, note_template):
        pass
