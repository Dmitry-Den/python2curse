import os

def group_rename_files(target_name, digits_count, original_extension, new_extension, name_range=None):
    files = [f for f in os.listdir() if f.endswith(original_extension)]

    if name_range:
        start, end = name_range
    else:
        start, end = 0, None

    counter = 1
    for file_name in files[start:end]:
        new_file_name = target_name + file_name[name_range[0]:name_range[1]] + str(counter).zfill(digits_count) + new_extension
        os.rename(file_name, new_file_name)
        counter += 1
