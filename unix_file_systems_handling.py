from pathlib import Path as m_path
import os as m_os
path = ('/Users/sskunall/Documents/engineering_repository/software_engineering_repository/python_systems/task-automation-template-python'.split('/'))
returnable_path = (m_path('/', *path))
print(returnable_path)
# PATH(some str) / 'STR'
print(m_path.cwd())

print(m_os.getcwd())
m_os.chdir("/Users/sskunall/Documents/engineering_repository/software_engineering_repository/python_systems/")
cwd = m_os.getcwd()

print(m_path.home() / m_path('Documents', 'engineering_repository'))

for attr in ['parent', 'name', 'stem', 'suffix', 'drive']:
    print(f"{attr}: {getattr(returnable_path, attr)}") # getattr to call attrs dynamically

print(getattr(returnable_path.stat(), 'st_nlink'))
print(getattr(returnable_path.stat(), 'st_uid'))

print(returnable_path.glob('?.py'))

for file in returnable_path.glob('*.*'): print(file) # print all file in cwd