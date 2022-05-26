import re
import os
import glob
from pathlib import Path
import time
import shutil

"""THIS FILE NEED TO:
    1. CLEANED TXT FILES AND OVERWRITE THE TXT FILE MOVE TO TxtMapCleaned DIRECTORY"""

TextPath = '/root/Filesys/TxtMapUncleaned/'
CleanedPath = '/root/Filesys/TxtMapCleaned/'


file_size = -1

while True:
    textFile = glob.glob(os.path.join(TextPath,'*.txt'))
    time.sleep(1)
    if len(textFile) != 0:
        file = textFile[0]
        while file_size != os.path.getsize(file):
            file_size = os.path.getsize(file)
            time.sleep(1)
        file_size = -1


        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        f.close()


        with open(file, 'w', encoding='utf-8') as f:
            if len(content) > 0:
                text = re.split(r'\W+', content)
                f.truncate(0)
                for W in text:
                    if re.match(r'[a-zA-Z0-9]',W) != None:
                        f.write(W+' '+'\n')
        f.close()
        
        
        if os.stat(file).st_size == 0:
            os.remove(file)    
        basename = os.path.basename(file)
        newf = str(Path(file).stem)
        newPath = os.path.join(CleanedPath+newf+'_Cleaned.txt')
        shutil.move(TextPath+basename, newPath)        
        print('done')
    else:
        pass