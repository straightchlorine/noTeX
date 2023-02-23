#!/usr/bin/python

import os

class NoTeXUtility:
    @staticmethod
    def get_dir_size(path):
        return len(os.listdir(path)) + 1
