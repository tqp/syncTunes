import os
srcDirectory = "Z:\MUSIC\iPod Music"


def look_for_folder_by_name():
    search_name = "Beach - Cheesy"

    # for dir_path, dirs, files in os.walk(srcDirectory):
    #     print(dir_path)
    #     if search_name in dir_path:
    #         print("YES: " + dir_path)
    #     else:
    #         print("NO")

    if not any(search_name in dir_path for dir_path, dirs, files in os.walk(srcDirectory)):
        print(search_name)

    # if not any(x.replace(" - ", "") == search_name for x in os.listdir(srcDirectory)):
    #     print("Checking: " + search_name)
    #     print("There is no directory named '" + search_name + "'. Deleting playlist...")


look_for_folder_by_name()
