import os

"""
    Creation and management of the directory tree, each object manages separate
    root - for example terms at the university:
    university
        +- term1
        |
        +- ...
        |
        +- termn
    In such case each term is separate root.
"""
class NoTeXFileManager:
    # Path to the root directory (for example 
    __root = None
    # General titles for group of notes (for example mathematics or physics)
    __subjects = None
