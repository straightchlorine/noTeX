#!/usr/bin/python

import os

from PyInquirer import style_from_dict, Token, prompt, Separator, print_json
from noTeX.dir.logger import NoTeXLogger
from noTeX.notes.note import NoTeXNote
from noTeX.notes.subjects import NoTeXSubjects
from noTeX.templates.templates import NoTeXTemplates

class NoTeXUI:
    # style for the graphical UI
    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })

    @staticmethod
    def select_subject(notex_subjects):
        options = notex_subjects.get_subjects()
        options.append('new subject')
        subject_list = [
            {
                'type' : 'list',
                'name' : 'subject_list',
                'message' : 'subject:',
                'choices' : options,
            }
        ]

        selected = prompt(subject_list, style = NoTeXUI.style).get('subject_list')

        def select_new_subject():
            new_subject = [
                {
                    'type' : 'input',
                    'name' : 'new_subject',
                    'message' : 'name of the subject:',
                }
            ]

            return prompt(new_subject, style = NoTeXUI.style).get('new_subject')

        # if there is no such topic, create one
        if selected == 'new subject':
            selected = select_new_subject()
            notex_subjects.add_subject(selected)
        
        print(selected)
        return selected

    @staticmethod
    def select_template(notex_templates):
        options = notex_templates.get_template_names()
        print(options)
        template_list = [
            {
                'type' : 'list',
                'name' : 'template_list',
                'message' : 'subject:',
                'choices' : options,
            }
        ]

        return prompt(template_list, style = NoTeXUI.style).get('template_list')

    @staticmethod
    def select_note_type():
        notetype = [
            {
                'type' : 'list',
                'name' : 'note_type',
                'message' : 'type:',
                'choices' : [
                    'lecture',
                    'tutorial',
                    'assignment',
                    'code',
                ],
            }
        ]

        return prompt(notetype, style = NoTeXUI.style).get('note_type')

class NoTeX:

    def new_note(self):
        notex_subjects = NoTeXSubjects()
        notex_templates = NoTeXTemplates()

        notex_subject = NoTeXUI.select_subject(notex_subjects)
        notex_type = NoTeXUI.select_note_type()
        notex_template = NoTeXUI.select_template(notex_templates)

        NoTeXNote(
            notex_subject,
            notex_type,
            notex_template)

    def __init__(self):
        NoTeXLogger.export_conf()
        self.new_note()

if __name__ == "__main__":
    notex = NoTeX()
