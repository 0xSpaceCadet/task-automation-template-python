from pathlib import Path as m_path
import os as m_os
import pyperclip

path = (
    "/Users/sskunall/Documents/engineering_repository/"
    "software_engineering_repository/python_systems/"
    "task-automation-template-python".split('/')
)

returnable_path = (m_path('/', *path))
print(returnable_path) # PATH(some str) / 'STR'
print(m_path.cwd())

print(m_os.getcwd())
m_os.chdir("/Users/sskunall/Documents/engineering_repository/software_engineering_repository/python_systems/task-automation-template-python")
cwd = m_os.getcwd()

print(m_path.home() / m_path('Documents', 'engineering_repository'))
for attr in ['parent', 'name', 'stem', 'suffix', 'drive']:
    print(f"{attr}: {getattr(returnable_path, attr)}") # getattr to call attrs dynamically

print(getattr(returnable_path.stat(), 'st_nlink'))
print(getattr(returnable_path.stat(), 'st_uid'))
print(returnable_path.glob('?.py'))

for file in returnable_path.glob('*.*'): print(file) # print all file in cwd

# call attributes and methods recursively
for name in ['parent', 'name', 'exists', 'is_file']:
    print(getattr(returnable_path, name)() if callable(getattr(returnable_path, name)) else attr)

print(m_path.cwd() / 'README.md')

for name in m_path.cwd().glob('*.*'):
    print(name)

h_file = open(m_path.cwd() / 'README.md', encoding='utf-8')
print(*h_file.readlines()) #.read() is an attribute method on it

h2_file = open(m_path.cwd() / 'README.md', mode='w', encoding='utf-8')
h2_file.write('\nThis overwrites everything\n-0xSpaceCadet')
h2_file.close()

h3_file = open(m_path.cwd() / 'README.md', mode='r', encoding='utf-8')
h3_file.read()







