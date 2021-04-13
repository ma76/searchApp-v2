# import sys
import os
# import glob
import shutil
import pandas as pd
# from openpyxl.workbook import Workbook
import easygui

# CONST
OUTPUT_DIR = os.getcwd()
FORMAT_DIRECTORIES_MAP = {
    'text': 'notes',
    'video': 'videos',
    'music': 'music',
    'image': 'pictures',
    'zip': 'compressed',
    'doc': 'documents',
    'unknown': 'other'
}
FORMATS_EXT_MAP = {
    'zip':   ['rar', 'zip'],
    'text':  ['txt', 'md', 'csv'],
    'video': ['mp4', 'mkv', 'avi'],
    'music': ['mp3'],
    'image': ['jpg', 'jpeg', 'png', 'gif'],
    'doc':   ['pdf', 'djvu', 'docx', 'xlsx']
}

# helper  // check smell
# sift + f6 // Key Promoter X
def message_box(title, errorMsg):
    easygui.msgbox(errorMsg, title, ok_button="Ok")

def get_output_path(path):
    return os.path.join(OUTPUT_DIR, path)

def move_file(src, dist):
    try:
        shutil.move(src, dist)
    except:
        pass

def get_ext(path):
    return path.split(".").pop()

def get_format(path):
    ext = get_ext(path)
    assert ext, 'Extenstion must be available'

    for format, extenstions in FORMATS_EXT_MAP.items():
        if ext in extenstions:
            return format

    return 'unknown'


def get_dist(format, output_dir=None):
    ext_dir = FORMAT_DIRECTORIES_MAP[format]
    ext_dir = ext_dir[0].upper() + ext_dir[1:]
    if output_dir is None:
        return get_output_path(ext_dir)
    return os.path.join(output_dir, ext_dir)

def count_of_files(dir):
    for i in range(0,len(dir)-1) :
        count = len(os.listdir(dir[i+1]))
        print(f"The {dir[i+1]} directory has {count} files")


#  why better to have single responsibility functions
def create_report_file(dir_info):
    try:
        directories = dir_info[1:]
        data = pd.DataFrame({
            "Directory": directories,
            "Count of files": [len(os.listdir(directory)) for directory in directories],
        })
        data.to_excel("./data.xlsx")
        print("'Data-File' is created !")
    except PermissionError :
        message_box("Error", "Please close 'Data-File' !!! ")


if __name__ == '__main__':
    root_dir = r'test'
    output_dir = root_dir # or change if you want
    my_files =[]
    for (file_path,_,file_names) in os.walk(root_dir):
        for path in file_names:
            format = get_format(path)
            dist = get_dist(format, output_dir)
            os.makedirs(dist, exist_ok=True)
            move_file(
                get_output_path(os.path.join(file_path, path)),
                dist
            )
        my_files.append(file_path)
    #print(my_files)
    #count_of_files(my_files)
create_report_file(my_files)