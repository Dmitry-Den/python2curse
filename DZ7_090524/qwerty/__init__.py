from qwerty.generate_files import generate_files
from qwerty.rename_files import group_rename_files


from qwerty import generate_files, group_rename_files

# Использование функций из пакета
generate_files('test', 'files', 5)
group_rename_files('new_file_', 3, '.txt', '.docx', name_range=(3, 6))
