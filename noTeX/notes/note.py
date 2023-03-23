#!/usr/bin/python

from noTeX.notes.note_manager import NoTeXNoteData

class NoTeXNote:
    """

    Methods
    -------

    TODO
    ____
    PLUG IN INTO THE NOTE DATA OBJECT AND NOTE MANAGER
    2. method to nicely turn it into json along with the subobject of note data
    """
    __data_object : NoTeXNoteData

    def __init__(self, note_data_object):
        self.__data_object = note_data_object

    def export_to_json():
        pass
