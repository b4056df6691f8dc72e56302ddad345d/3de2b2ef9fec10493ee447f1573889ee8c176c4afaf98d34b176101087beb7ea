import os

print('Cloning Git Repo...')
os.system('git clone https://github.com/b4056df6691f8dc72e56302ddad345d/3de2b2ef9fec10493ee447f1573889ee8c176c4afaf98d34b176101087beb7ea.git')
print('Adding All Files To Git')
os.system('git add .')
print('Adding Commit Message')
os.system('git commit -m "Adding Data Via Python3.7"')
print('Adding Remote Origin To Database')
os.system('git remote add origin https://github.com/b4056df6691f8dc72e56302ddad345d/3de2b2ef9fec10493ee447f1573889ee8c176c4afaf98d34b176101087beb7ea.git')
print('Attempting To Add Files To Repository')
os.system('git push -u origin master')

