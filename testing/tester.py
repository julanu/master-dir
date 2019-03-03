#!/usr/bin/env python3
import os
import ast
import shutil
from scripts import dirs
from scripts import identify
from testing import config
# from scripts import dupes


def get_key(dic, val):
    """
    Get the key from a dict based on the value
    """
    for key, value in dic.items():
        for ext in value:
            if ext == val:
                return key
    return None


def group_files(src, dst, dic):
    """
    Find the files with a specific extension and move them to the correct folder
    """
    list_files = os.walk(src)  # files

    for root, _, files in list_files:
        for file_name in files:
            name, ext = os.path.splitext(file_name)
            del name
            ext = ext[1:].lower()  # in case the file is .PNG -> 'PNG' -> 'png'
            group = get_key(dic, ext)
            dir_name = '\_{}'.format(group)
            dst_final = dst + dir_name

            if group is None and group not in dst_final:
                dst_final = dst + dir_name

            if group is not None:
                src_file = os.path.join(root, file_name)
                dst_file = os.path.join(dst_final, file_name)
                shutil.move(src_file, dst_file)


def create_dirs(src, dst):
    """
    Create directories to move the files and for every file type move the files to the right folder
    """
    exts = identify.get_file_exts(src)
    cats = read_group()

    for ext in exts:
        category = get_key(cats, ext)
        dir_name = r'\_{}'.format(category)
        new_dir = dst + dir_name
        if not os.path.exists(new_dir) and category is not None:
            os.mkdir(new_dir)


def read_group():
    """
    Read file and evaluate dict
    """
    with open('..\extensions\extensions.json', 'r') as f:
        dic = f.read()
        dic = ast.literal_eval(dic)
    return dic


def clean_dir(init_list, path):
    """
    Will clean the source directory after all the files have been moved and categorized
    """
    files = os.listdir(path)
    # folders = identify.get_folder_names(path)
    for item in files:
        if item in init_list:
            rmv = os.path.join(path, item)
            shutil.rmtree(rmv)


def main():
    file_path = '../files/files.xlsx'
    print("Give sections: ", end='')
    section = input()
    params = config.get_params(section)
    src = params[0]
    src_cpy = params[1]
    dst = params[2]

    # print(dupes.find_duplicates(src))
    dic = read_group()

    # Count how many files are initially
    files_start = identify.count_files(src)

    # Save a list of all the initial files
    identify.save_files(src, file_path, 1)

    # Save a list of all the initial folders
    init_list = identify.get_folder_names(src)

    # Group files
    create_dirs(src, src)
    group_files(src, src, dic)
    clean_dir(init_list, src)

    # See how many files were moved and grouped
    files_end = identify.count_files(src)

    print("Files found {0} | Files moved {1} | Files renamed ".format(files_start, files_end))

    # Count how many files are after the grouping
    identify.save_files(src, file_path, 2)

    # Bring back all the folders to the initial state
    print("Run dirs? y/n", end='')
    answer = input()

    if answer in ['y', 'yes', 'YES', 'Yes']:
        dirs.rm_copy_dirs(src, src_cpy, dst)


if __name__ == '__main__':
    main()
