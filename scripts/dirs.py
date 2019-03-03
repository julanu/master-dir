from invoke import run
from time import sleep


def rm_copy_dirs(src, src_copy, dst):
    """
    Will remove all the files from src and src_dest and will copy all the files from src_copy to src. Will revert all
    the changes done by the script and return the folders to normal, removing the files from the back-up after moving
    them to the source folder that has been cleaned before.

    Args:
        src - full path to source folder where the script has to group the files
        src_copy - full path to the folder where the "back-up" will be stored
        dst - full path to the folder where the files shall be grouped
    """
    # Remove all files from src
    run("powershell -Command \"Remove-Item \'{}/*\' -Recurse -Force\" ".format(src))
    sleep(0.3)
    # Copy files from back-up
    run("powershell -Command \" xcopy \'{0}\' "
        " \'{1}\' /e \" ".format(src_copy, src))
    sleep(0.3)
    # Remove all the grouped files
    run("powershell -Command \"Remove-Item \'{}/*\' -Recurse -Force\" ".format(dst))
    print("All remaining files removed and added copies")
