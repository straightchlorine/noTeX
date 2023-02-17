"""
    Note class - base class of every single created note.
"""
class NoTeXNote:
    # Identifies the note - for now it is simply the number of
    # notes currently in the directory.
    __id = None
    # Where the note belongs (if there are multiple trees)
    __root = None
    # Creation date (also in the name of the folder)
    __date = None

    # Type of the note (for example lecture or tutorial)
    __type = None
    # Chosen template
    __template = None
    # What is the note about (for example physics or mathematics)
    __subject = None

    def __init__(self, root, template, type, subject):
        # todo: create root manager
        pass
