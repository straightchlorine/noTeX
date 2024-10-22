#!/usr/bin/python

import os
from datetime import datetime

from noTeX.dir.logger import NoTeXLogger
from noTeX.exceptions.exc import NoSubjectPathException
from noTeX.notes.subjects import NoTeXSubjects
from noTeX.templates.templates import NoTeXTemplates
from noTeX.utility.utils import NoTeXUtility

class NoTeXNoteData:
    """
    Class provides identification string for each created note,
    along with all needed information for easier access.

    In the future the id is meant to allow for quick navigation
    in the root directory.

    Methods
    -------
    get_id():
        Returns the id of the note.

    TODO
    ____
    1. id string initial idea: <main_root>:<subject>:<type>:<internal_id>
    2. export each id to config and import it from config as well
    2. create method to nicely make it into json
    """
    # path to the root of the note directory, a the very top of the hierarchy
    __note_main_root : os.PathLike
    #name of the subject, which note concerns
    __note_subject : str
    # type of the note (lecture/tutorial/code)
    __note_type : str
    # chosen template of the note
    __note_template : str
    # path to the chosen template of the note
    __note_template_path : os.PathLike
    # path of the note generated by NoTeXNoteManager
    __note_path : os.PathLike
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
        self.__note_template_path = NoTeXTemplates.get_template_path(
                                                    self.__note_template)
        self.__make_id()

    def __make_id(self):
        """Function generates the id, called in the constructor.

        For now, it simply assigns (number_of_directories_in_path) + 1.
        """
        self.__id = str(NoTeXUtility.get_dir_size(
                        os.path.join(self.__note_main_root,
                                    self.__note_subject,
                                    self.__note_type)))


    def set_path(self, path):
        """
        Setter, assigns given path to the __note_path class atribute.

        Parameters
        ----------
        path : os.PathLike
            path object
        """
        self.__note_path = path

    def get_id(self):
        """
        Getter, provides the id for outside use.

        Returns
        -------
        id
            final identification string
        """
        return self.__id

    def get_path(self):
        """
        Getter, provides the path of the note for outside use.

        Returns
        -------
        path : os.PathLike
            path of the note, that object coresponds to
        """
        return self.__note_path

    def get_subject(self):
        """
        Getter, provides the subject name for outside use.

        Returns
        -------
        subject
            subject of the note
        """
        return self.__note_subject


    def get_type(self):
        """
        Getter, provides selected type for outside use.

        Returns
        -------
        __note_type
            type of the note
        """
        return self.__note_type

    def get_template(self):
        """
        Getter, provides the template name for outside use.

        Returns
        -------
        __note_template
            template of the note
        """
        return self.__note_template


class NoTeXNoteManager:
    """
    Class responsible for creating notes.

    Methods
    -------
    create_note():
        Returns the id of the note.

    TODO: proper management
    2. needs to create the id of the note (for future navigation)
    3. maybe get template copying here also
    """

    @staticmethod
    def __make_note_path(note_data):
        """
        Function builds and creates directory for new note.

        Path consists of:
            <path_to_subject_directory>/
                <[id]-[creation_date]-[chosen_template]>
        Where id is (for now) number of directories in the path + 1.

        Parameters
        ----------
        note_data : NoTeXNoteData
            object responsible for storing and processing data
            needed in order to create note

        Raises
        ------
        NoSubjectPathException
            in case subject path was not created

        Returns
        -------
        os.PathLike
            generated path
        """
        # subject path
        s_path = NoTeXSubjects.getpath(note_data.get_subject())
        if s_path is None:
            raise NoSubjectPathException('Subject path missing.')

        # base for the note path (starting with subject path)
        path = os.path.join(s_path, note_data.get_type())
        if os.path.exists(path):
            os.mkdir(path)

        # creating name for the directory
        internal_id = note_data.get_id()
        dir_name = str(internal_id) + '-'                        \
                + datetime.today().strftime('%a-%d-%b-%Y') + '-' \
                + note_data.get_template()
        path = os.path.join(path, dir_name)

        os.mkdir(path)

        return path

    @staticmethod
    def create_note(note_subject, note_type, note_template):
        # creating note data object
        note_data = NoTeXNoteData(
                        NoTeXLogger.get_opt('root'),
                        note_subject,
                        note_type,
                        note_template)
        note_data.set_path(NoTeXNoteManager.__make_note_path(note_data))

        # here note will be put together
        # * make the path
        # * get the Note object done - give it everythin it needs
        # * give some sort of notification that it succeded
