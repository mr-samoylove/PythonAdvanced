import os


def rename_group_files(new_filename: str, target_extension: str, new_extension: str,
                       range_of_name_to_keep=(0, 0), width_of_id=3):
    """
    please set extensions with a dot, like ".txt", or ".jpg"
    """

    files_counter = 1
    keep_from = range_of_name_to_keep[0]
    keep_to = range_of_name_to_keep[1]
    for name in os.listdir(os.getcwd()):
        if name.endswith(target_extension):
            while os.path.isfile(new_filename + str(files_counter).zfill(width_of_id) + new_extension):
                files_counter += 1
            os.rename(name,
                      name[keep_from:keep_to] + new_filename + str(files_counter).zfill(width_of_id) + new_extension)
            files_counter += 1


if __name__ == '__main__':
    rename_group_files("result", ".txt", ".bin", range_of_name_to_keep=(0, 3), width_of_id=2)
