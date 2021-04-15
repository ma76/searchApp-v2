#  remove all files in output directory
import os
import glob
import shutil
def remove_all_files(dir):
    if os.listdir(dir):
        try:
            file_list = glob.glob(os.path.join(dir, "*"))
            for file_name in file_list:
                #print(file_name)
                shutil.rmtree(file_name)
        except NotADirectoryError:
            os.remove(file_name)
