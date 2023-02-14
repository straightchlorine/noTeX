#!/usr/bin/python
'''
    faster LaTeX notes management
'''
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator, print_json
from pprint import pprint
import os
from datetime import datetime

class NoTeXFile:
    @staticmethod
    def get_lecture_folders():
        dir = os.listdir('./lectures/')
        return dir

    @staticmethod
    def get_tutorial_folders():
        dir = os.listdir('./tutorials/')
        return dir

    @staticmethod
    def get_dir_type(type):
        return type + 's'

    @staticmethod
    def get_dir_size(path):
        return len(os.listdir(path))

    @staticmethod
    def class_list(type):
        directory = []
        if type == 'lecture':
            directory = NoTeXFile.get_lecture_folders()
        elif type == 'tutorial':
            directory = NoTeXFile.get_tutorial_folders()
        directory.append('new class')
        return directory

    @staticmethod
    def new_for_existing_class():
        type = NoTeXUI.select_class_type()
        sclass = NoTeXUI.select_class(type)

        # directory of selected class of selected type <id>_<date>
        c_path = os.path.join(os.getcwd(), NoTeXFile.get_dir_type(type), sclass)

        if not os.path.exists(c_path):
            os.mkdir(c_path)

        # name for the new directory <id
        new_dir_name = str(NoTeXFile.get_dir_size(c_path) + 1) + '-'+ datetime.today().strftime('%a-%d-%b-%Y')

        # path of the folder for the current class
        new_path = os.path.join(c_path, new_dir_name)
        os.mkdir(new_path)

        # getting into the new directory
        os.chdir(new_path)

        # name of the new .tex file <class>-<type>-notes.tex
        f_name = sclass + '-' + type + '-notes.tex'

        # copy the template and rename accordingly
        os.system('cp ~/latex-template/notes/*.tex .')
        os.rename('template.tex', f_name)

        os.system('nvim -c "VimtexCompile" ' + f_name)

class NoTeXUI:
    filemodule = NoTeXFile()

    # class-wide style for the PyInquirer
    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })

    def select_class_type():

        lessontype = [
            {
                'type' : 'list',
                'name' : 'lessontype',
                'message' : 'type:',
                'choices' : [
                    'lecture',
                    'tutorial',
                ],
            }
        ]

        # type (lecture/tutorial)
        return prompt(lessontype, style = NoTeXUI.style).get('lessontype')


    @staticmethod
    def select_class(type):

        classes = [
            {
                'type' : 'list',
                'name' : 'dir',
                'message' : 'class:',
                'choices' : NoTeXFile.class_list(type)
            }
        ]

        sclass = prompt(classes, style = NoTeXUI.style).get('dir')

        if sclass == 'new class':
            new_class = NoTeXUI.select_new_class()
            sclass = new_class

        # class (linear algebra for an instance)
        return sclass

    @staticmethod
    def select_new_class():

        new_class = [
            {
                'type' : 'input',
                'name' : 'nclass',
                'message' : 'name of the class:',
            }
        ]

        return prompt(new_class, style = NoTeXUI.style).get('nclass')

class NoTeX:
    def new_tex_note(self):
        NoTeXFile.new_for_existing_class()

if __name__ == '__main__':
    notex = NoTeX()
    notex.new_tex_note()

