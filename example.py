import os

menu = '''
[
  Element('Option 1'),
  Element('Option 2')
]
'''

res = os.WEXITSTATUS(os.system(f'python3 main.py --menu "{menu}"'))
print(f'output : {res}')


