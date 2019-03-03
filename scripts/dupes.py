import os


# ToDo remake
def find_duplicates(src):
    """
        Takes in an iterable of folders and prints & returns the duplicate files
    Args:
        src - full path to a folder
    Returns:
         list of duplicate files
    """
    files = [files for _, _, files in os.walk(src)]
    iter_files = flat_list(files)
    dupes = [j for i, j in enumerate(iter_files) if j in iter_files[:i]]
    print(dupes)
    return dupes


# ToDo remake
def rename_dupes(src, dupes_list):
    files = os.walk(src)
    for dupe in dupes_list:

        for file in files:
            if file == dupe:
                print('found dupe')
                # name, ext = os.path.splitext(file)
                # os.rename(os.path.join(src,file), '{0}_{1}.{2}'.format(name, count, ext))
                # count += 1


# ToDo test more
def flat_list(list_of_items):
    """"
    Takes nested lists as argument and return a flat list

    Args:
        list_of_items - nested list
    Returns:
         a flat list
    """
    return [item for sublist in list_of_items for item in sublist]


def main():
    src = r'H:\Downloads'
    dupes = find_duplicates(src)
    rename_dupes(src, dupes)


if __name__ == '__main__':
    main()
