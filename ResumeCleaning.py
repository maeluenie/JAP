import re
import os
import glob
from pathlib import Path

init_path = 'init_path'
final_path = 'final_path'


def cleaner(filename, f):
    content = f.read()
    if len(content) > 0 :
        text = re.split(r'\W+',content)
        fname = str(Path(filename).stem)
        complete_name = os.path.join(final_path, fname+".txt")
        NewtextFile = open(complete_name, 'w', encoding='utf-8')
        for W in text:
            if re.match(r'[a-zA-Z0-9]',W) != None:
                NewtextFile.write(W+"\n")
        NewtextFile.close()
        if os.stat(complete_name).st_size == 0:
            os.remove(complete_name)

for filename in glob.glob(os.path.join(init_path,'*.txt')):
    with open(filename, 'r', encoding='utf-8') as f:
        cleaner(filename, f)
    f.close()
print('done')