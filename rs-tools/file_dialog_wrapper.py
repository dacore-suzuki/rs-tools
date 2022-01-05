""" Author: Ryo Suzuki, Python Version: 3.8 """
import os
import tkinter as tk
from pathlib import Path
from tkinter import filedialog

OPEN_DIRECTORY = 1
ASK_OPEN_FILE = 2

constant_list = [OPEN_DIRECTORY, ASK_OPEN_FILE]


class FileDialogWrapper:
    r"""Wraps a tkinter filedialog.
    If you want to display multiple file dialogs, you can display them
    consecutively by specifying the tuple array (title, dialog type)
    as the instance argument.
    """

    def __init__(self, title_dialog_type: any = None):
        if title_dialog_type is None:
            raise TypeError('FileSelectingDialogs module is arguments must be given')
        try:
            if not isinstance(title_dialog_type, (tuple, list)):
                raise TypeError
            if isinstance(title_dialog_type, list):
                if not isinstance(title_dialog_type[0][0], str):
                    raise TypeError
                if not isinstance(title_dialog_type[0][1], int):
                    raise TypeError
            else:
                if not isinstance(title_dialog_type[0], str):
                    raise TypeError
                if not isinstance(title_dialog_type[1], int):
                    raise TypeError
                title_dialog_type = list(title_dialog_type)
            for t in title_dialog_type:
                if t[1] not in constant_list:
                    raise TypeError
        except TypeError:
            raise TypeError('title_dialog_type is not a (str, int) or [(str, int)]. str specifies the title of'
                            ' the filedialog. int can be a constant of FileDialogWrapper.')

        self.__title_dialog_type = title_dialog_type
        self.__initialize_file_name = 'files_selecting_dialog.ini'

        tk.Tk().withdraw()

    @property
    def title_dialog_type(self):
        return self.__title_dialog_type

    @title_dialog_type.setter
    def title_dialog_type(self, title_dialog_type: (str, int)):
        self.__title_dialog_type = title_dialog_type

    @property
    def initialize_file_name(self):
        return self.__initialize_file_name

    @initialize_file_name.setter
    def initialize_file_name(self, initialize_file_name: str):
        extension = '.ini'
        if initialize_file_name not in extension:
            initialize_file_name += extension
        self.__initialize_file_name = initialize_file_name

    def show(self):
        current_target_dir = ''
        directory = []
        if os.path.isfile(self.__initialize_file_name):
            with open(self.__initialize_file_name, encoding='utf-8') as file:
                directory = str(file.readline()).split(',')

        result_path_list = []

        current_selected_dir = ''
        select = ''
        for i, d in enumerate(self.__title_dialog_type):
            if len(directory) != 0:
                if directory[i] != '':
                    current_selected_dir = directory[i]
            else:
                current_selected_dir = str(Path(select).parent)
            if d[1] == OPEN_DIRECTORY:
                select = filedialog.askdirectory(
                    title=d[0], initialdir=current_selected_dir
                )
            elif d[1] == ASK_OPEN_FILE:
                select = filedialog.askopenfilename(
                    title=d[0], initialdir=current_selected_dir
                )
            result_path_list.append(select)
        with open(self.__initialize_file_name, encoding='utf-8', mode='w') as file:
            file.write(','.join(result_path_list))
        return result_path_list
