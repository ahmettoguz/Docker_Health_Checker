import os

hasLog = False


def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def findFiles():
    for item in os.listdir():
        if(os.path.isdir(item)):
            # print("Folder->", item)
            os.chdir(item)
            findFiles()
            os.chdir("../")
        else:
            if item.endswith(".log"):
                global hasLog
                if hasLog == False:
                    hasLog = True
                    print(
                        "!!!This folder or its sub-folders contain files that might be a log files which can consume your disk space!!!\n")

                # print(os.getcwd(), item, os.stat(item).st_size)
                print("File Name: ", item)
                print("File Size: ", sizeof_fmt(os.path.getsize(item)))
                print("File Path: ", os.getcwd(), "\n")


findFiles()
if hasLog == False:
    print("This folder or its sub-folders do not contain any file that might be a log files")

print("Press any key to close")
input()
