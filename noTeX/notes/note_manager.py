#!/usr/bin/python

import os
from datetime import datetime

from noTeX.exceptions.exc import NoTeXNoSubjectException
from noTeX.notes.subjects import NoTeXSubjects
from noTeX.utility.utils import NoTeXUtility

"""
    NoTeXNoteManager.

    Class responsible for creating notes.

    TODO: proper management
    1. needs to create the note (base functionality for now)
    2. needs to create the id of the note (for future navigation)
"""
class NoTeXNoteManager:
    @staticmethod
    def __create_note_id(note_main_root, note_subject, note_type, note_template):
        # id, as a following string:
        # <main_root>:<subject>:<type>:<internal_id>
        pass

    @staticmethod
    def __make_note_path(note_subject, note_type, note_template):
        # subject path
        s_path = NoTeXSubjects.getpath(note_subject)
        if s_path is None:
            raise NoTeXNoSubjectException

        # path will be built in path variable
        path = os.path.join(s_path, note_type)
        if os.path.exists(path):
            os.mkdir(path)

        # creating descriptive name for the directory
        # <internal_id>-<date>-<template>
        # where internal_id is simply incremented number of files currently in directory
        internal_id = NoTeXUtility.get_dir_size(path)
        dir_name = str(internal_id) + '-' + datetime.today().strftime('%a-%d-%b-%Y') + '-' + note_template
        path = os.path.join(path, dir_name)

        os.mkdir(path)

    @staticmethod
    def create_note(note_subject, note_type, note_template):
        pass
