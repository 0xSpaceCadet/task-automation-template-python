import random
from idlelib.run import capture_warnings
from pathlib import Path as m_path
import shutil # shell utilities
import os

def functionality() :
    for q_num in range(5):
        q_file_path=f'q_file_{q_num+1}.txt'
        q_file = open(file=q_file_path, mode='w', encoding='UTF-8')

        a_file_path = f'a_file_{q_num+1}.txt'
        a_file = open(file=a_file_path, mode='w', encoding='UTF-8')

        q_file.write('UUID:\n\nPassphrase:')

        state = list(capitals.keys())
        random.shuffle(state)

        for num in range(50):
            c_ans = capitals[state[num]]
            w_ans = list(capitals.values())
            del w_ans[w_ans.index(c_ans)] # actual c_ans
            w_ans = random.sample(w_ans, 3)
            a_options = w_ans+[c_ans]
            random.shuffle(a_options)

        q_file.close()
        a_file.close()

d_path = m_path.cwd()
(d_path / 'spam').mkdir(parents=True, exist_ok=True)

# # setup and teardown using WITH operator
# with open(file=d_path/'spam'/'spam_20251105.txt', mode='w', encoding='utf-8') as c_file:
#     c_file.write('****\nSpam File Logged on November 5, 2025\n****')
#
# # graceful execution as it doesn't COPY it bu just copies it
# shutil.copy(d_path/'spam'/'spam_20251105.txt', d_path)
# shutil.copy(d_path/'spam'/'spam_20251105.txt', d_path/'spam'/'spam_20251105_2.txt')
#
# shutil.copytree(d_path/'spam', d_path/'spam_bkp')

# just like copy we have MOVE
# rmtree, rmdir, unlink

for l_cntr in range(3):
    with open(d_path/f'\nTOML_Configuration_{l_cntr+1}.toml', 'w', encoding='utf-8') as t_file:
        t_file.write('**** TOML Configuration ****\n')

try:
    #if input('Confirm Delete >') == 'Yes':
    for f_name in d_path.glob('*.toml'):
        os.unlink(f_name)
except FileNotFoundError:
    pass # do nothing

print()
print(os.listdir(d_path)) # what directory contains
print()
print(list(d_path.iterdir())) # what directory contains

# walk across folders subfolders
for fl_name, sbfl_name, f_name in os.walk(d_path):
    print(fl_name, sbfl_name, f_name)

print()
print(list(os.walk(d_path))) # combinatorial setup

shutil.rmtree(d_path/'spam_bkp') # removees everything
# to delete and then remove director, SAFE DELETE
