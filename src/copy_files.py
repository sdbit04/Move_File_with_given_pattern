import shutil
import os
import json


def read_config(config_file):
    with open(config_file, 'r') as config:
        json_ob = json.load(config)
        return json_ob


def search_and_copy():
    config = read_config("config.ini")
    # config = {}
    _file_name_contain = config.get("search_pattern")
    base_directory = config.get("base_directory")
    out_directory = config.get("out_directory")
    dir_gen = os.walk(base_directory, topdown=True)
    # print("{}".format(next(dir_gen)))
    for dir, dirs, files in dir_gen:
        path_from_base = os.path.relpath(dir, base_directory)
        print("path_from_base = {}".format(path_from_base), end="\t")
        corresponding_out_dir = os.path.join(out_directory, path_from_base)
        print("corresponding_out_dir = {}".format(corresponding_out_dir))
        if not os.path.exists(corresponding_out_dir):
            try:
                os.mkdir(corresponding_out_dir)
            except FileExistsError:
                print("dir already exist")
            else:
                print("{} created".format(corresponding_out_dir))

        for file_name in files:
            if file_name.split("_")[3] in _file_name_contain:
                try:
                    shutil.copy(os.path.join(dir, file_name), os.path.join(corresponding_out_dir, file_name))
                except (FileExistsError, FileNotFoundError):
                    print("File already exist")
                else:
                    print("Copied file at : {}".format(os.path.join(corresponding_out_dir, file_name)))


if __name__ == "__main__":
    search_and_copy()

