from zipfile import ZipFile as m_zip
import os
from pathlib import Path as m_path


def backup_folder_to_file(folder):
    """
    :param folder:
    :return: nothing but creates a path name
    """
    fl_name = m_path(folder)
    numeric = 1
    while True:
        zip_f_name = m_path(folder.parts[-1] + '_' + str(numeric) + '.zip')
        if not zip_f_name.exists():
            break  # the loop
        numeric = numeric + 1
    print(f'Creating zip file {zip_f_name}')
    bkp_zip = m_zip(file=zip_f_name, mode='w')

    for folder_name, subfolder_name, file_name in os.walk(folder):
        folder_name = m_path(folder_name)  # org a str type
        print(f'Adding this file from folder {folder_name}')
        for file_name_individual in file_name:
            print(f'Adding this file from folder {folder_name} and file {file_name_individual}')
            bkp_zip.write(folder_name / file_name_individual)
    bkp_zip.close()
    print('Done')


fl_path = m_path.cwd()
print('Tuple of Parts\n', m_path(fl_path.parts[-1] + '_' + str(1) + '.zip'))

backup_folder_to_file(m_path.cwd() / 'spam')


def backup_folder_recursive_show(folder):
    cntr = 1
    for folder_name, subfolder_name, file_name in os.walk(m_path(folder)):
        print(cntr,
              'FolderName= ', folder_name, '\n',
              'SubFolderName= ', subfolder_name, '\n',
              'FileName= ', file_name,
              end='\n\n')
        cntr = cntr + 1
