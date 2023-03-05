#!/usr/bin/python

import os
from posix import DirEntry
from noTeX.dir.logger import NoTeXLogger

"""
    Class reads and adds subjects of notes (general titles for example 'mathematics'
    would contain notes from math class etc.)
"""
class NoTeXSubjects:
    # Directory root, where the subjects are stored.
    __root = None
    # DirEntry objects containing the subjects
    __subjects = []

    def __init__(self):
        root = NoTeXLogger.get_opt('root')
        if root is not None:
            self.__root = str(root)
            self.__get_entries()

    def __get_entries(self):
        with os.scandir(self.__root) as it:
            for entry in it:
                self.__subjects.append(entry)

    def get_subjects(self):
        names = []
        for subject in self.__subjects:
            names.append(subject.name)
        return names

    def get_paths(self):
        paths = []
        for subject in self.__subjects:
            paths.append(subject.path)
        return paths

    def add_subject(self, subject):
        names = self.get_subjects()
        if subject not in names:
            new_path = os.path.join(str(self.__root), subject)
            os.mkdir(new_path)
            os.mkdir(os.path.join(new_path, 'materials'))

    @staticmethod
    def getpath(subject):
        for entry in NoTeXSubjects.__subjects:
            if entry.name == subject:
                return entry.path
        return None

    def get_subject_entry(self, subject):
        for entry in self.__subjects:
            if entry.name == subject:
                return entry
        return None
