#!/usr/bin/python

import os
from datetime import datetime

from noTeX.exceptions.exc import NoSubjectPathException
from noTeX.notes.subjects import NoTeXSubjects
from noTeX.utility.utils import NoTeXUtility

"""NoTeXNoteId.

Class provides the identification string for each note.
One ID object accompanies each note object, providing
easy access to each of the parameters.

For now it is simply (number_of_directories_in_path) + 1.

TODO:
1. id string initial idea: <main_root>:<subject>:<type>:<internal_id>
2. export each id to config and import it from config as well
"""
class NoTeXNoteId:
    note_main_root = ''
    note_subject = ''
    note_type = ''
    note_template = ''

    def __init__(self,
            note_main_root,
            note_subject,
            note_type,
            note_template):

        self.note_main_root = note_main_root
        self.note_subject = note_subject
        self.note_type = note_type
        self.note_template = note_template

"""NoTeXNoteManager.

Class responsible for creating notes.

TODO: proper management
1. needs to create the note (base functionality for now)
2. needs to create the id of the note (for future navigation)
"""
class NoTeXNoteManager:
    @staticmethod
    def __make_note_path(note_subject, note_type, note_template):
        """Function builds and creates directory for new note.

        Path consists of:
            <path_to_subject_directory>/
                <[id]-[creation_date]-[chosen_template]>
        Where id is (for now) number of directories in the path + 1.
        """
        # subject path
        s_path = NoTeXSubjects.getpath(note_subject)
        if s_path is None:
            raise NoSubjectPathException('Subject path missing.')

        # base for the note path (starting with subject path)
        path = os.path.join(s_path, note_type)
        if os.path.exists(path):
            os.mkdir(path)

        # creating name for the directory
        internal_id = NoTeXUtility.get_dir_size(path)
        dir_name = str(internal_id) + '-'                        \
                + datetime.today().strftime('%a-%d-%b-%Y') + '-' \
                + note_template
        path = os.path.join(path, dir_name)

        os.mkdir(path)

    @staticmethod
    def create_note(note_subject, note_type, note_template):
        pass
