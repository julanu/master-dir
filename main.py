#!/usr/bin/env python3
import os
import ast
import shutil
from scripts import identify
import json


#
def get_key(dic, val):
    """
    Get the key from a dict based on the value
    :param dic: dictionary
    :param val: search value
    :return: key
    """
    for key, value in dic.items():
        for ext in value:
            if ext == val:
                return key
    return None


def group_files(src, dst, dic):
    """
    Find the files with a specific extension and move them to the correct folder
    Improve working of the function
    :param src:
    :param dst:
    :param dic:
    :return:
    """
    list_files = os.walk(src)  # files

    for root, _, files in list_files:
        for file_name in files:
            name, ext = os.path.splitext(file_name)
            del name
            ext = ext[1:].lower()  # in case the file is .PNG -> 'PNG' -> 'png'
            group = get_key(dic, ext)
            dir_name = '\\_{}'.format(group)
            dst_final = dst + dir_name

            if group is None and group not in dst_final:
                dst_final = dst + dir_name

            if group is not None:
                src_file = os.path.join(root, file_name)
                dst_file = os.path.join(dst_final, file_name)
                shutil.move(src_file, dst_file)


# Create directories to move the files and for every file type move the files to the right folder
def create_dirs(src, dst):
    exts = identify.get_file_exts(src)
    cats = read_group()

    for ext in exts:
        category = get_key(cats, ext)
        dir_name = r'\_{}'.format(category)
        new_dir = dst + dir_name
        if not os.path.exists(new_dir) and category is not None:
            os.mkdir(new_dir)


# Read file and evaluate dict
def read_group():
    with open(r'..\extensions\extensions.json', 'r') as f:
        dic = f.read()
        dic = ast.literal_eval(dic)
    return dic


# Will clean the source directory after all the files have been moved and categorized
def clean_dir(path):
    files = os.listdir(path)
    folders = identify.get_folder_names(path)
    for item in files:
        if item in folders:
            rmv = os.path.join(path, item)
            shutil.rmtree(rmv)


def main():
    dic = read_group()

    create_dirs(src, dst)
    group_files(src, dst, dic)
    clean_dir(src)


if __name__ == '__main__':
    main()
