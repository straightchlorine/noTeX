import os

"""
    Class reads and adds subjects of notes (general titles for example 'mathematics'
    would contain notes from math class etc.)
"""
class NoTeXSubjects:
    __root = None
    __subjects = []

    def __init__(self, root):
        self.__root = root
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
            os.mkdir(os.path.join(self.__root, subject))

    def get_subject_path(self, subject):
        for entry in self.__subjects:
            if entry.name == subject:
                return entry.path

if __name__ == "__main__":
    group = NoTeXSubjects(os.path.join(os.path.expanduser('~'), 'uni', 'lectures'))
    print(group.get_subjects())
    print(group.get_subject_path('base_management'))
