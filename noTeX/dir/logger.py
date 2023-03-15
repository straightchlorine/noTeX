#!/usr/bin/python

import json
import os

"""
    Class reads and adds subjects of notes (general titles for example 'mathematics'
    would contain notes from math class etc.)
"""
class NoTeXLogger:
    __config = {
        'root' : os.path.join(os.path.expanduser('~'), 'uni'),
        'subroot' : os.path.join(os.path.expanduser('~'), 'uni', '2_term'),
        'templates' : os.path.join(os.path.expanduser('~'), 'latex-template'),
    }
    __path = os.path.expanduser('../.config.json')

    @staticmethod
    def add_opt(opt, val):
        NoTeXLogger.__config[opt] = val

    @staticmethod
    def get_opt(opt):
        if NoTeXLogger.__config[opt] is not None:
            return NoTeXLogger.__config[opt]
        else:
            return None

    @staticmethod
    def export_conf():
        with open(NoTeXLogger.__path, 'w') as conf:
            json.dump(json.dumps(NoTeXLogger.__config), conf)

    @staticmethod
    def import_conf():
        with open(NoTeXLogger.__path) as conf:
            NoTeXLogger.__config = json.load(conf)
