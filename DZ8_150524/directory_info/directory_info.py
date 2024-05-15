import os
from directory_info.json_handler import save_as_json
from directory_info.csv_handler import save_as_csv
from directory_info.pickle_handler import save_as_pickle

def get_directory_info(directory):
    result = {}

    for root, dirs, files in os.walk(directory):
        total_size = sum(os.path.getsize(os.path.join(root, name)) for name in files)
        total_size += sum(os.path.getsize(os.path.join(root, name)) for name in dirs)
        
        result[root] = {
            'type': 'directory',
            'size': total_size,
            'subdirectories': dirs,
            'files': files
        }

    save_as_json(result, 'directory_info.json')
    save_as_csv(result, 'directory_info.csv')
    save_as_pickle(result, 'directory_info.pkl')

get_directory_info('K:\gb\python gb\python2kurs\python2curse\DZ8_150524\directory_info')