"""
    Creation and management of the directory tree, each object manages separate
    root - for example terms at the university:
    university
        +- 1_term
        |
        +- ...
        |
        +- 2_termn
    In such case each term is separate root.
    TODO - base on root /uni in this case find the subroots and expand the config
"""
class NoTeXFileManager:
    # Path to the root directory
    __root = None
    # General titles for group of notes (for example mathematics or physics)
    __subjects = None
