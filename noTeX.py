#!/usr/bin/python

from noTeX.dir.logger import NoTeXLogger
from noTeX.notes.subjects import NoTeXSubjects

class NoTeX:
    def __init__(self):
        NoTeXLogger.export_conf()
        subjects = NoTeXSubjects()
        subjects.get_subjects()

if __name__ == "__main__":
    notex = NoTeX()

