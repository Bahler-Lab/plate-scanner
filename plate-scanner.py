import sys
import time
import numpy as np
#import tqdm

manualStr = '''
Welcome. This script will help you acquire images in batches using the custom set-up implemented by Stephan and John.
'''

scriptParams = []

if len(sys.argv) > 1:
    if sys.argv[1] == '-help':
        print manualStr

print '''Welcome. This script will help you acquire images in batches using the custom set-up implemented by Stephan and John.
Please enter the required information below.'''

n=None
while not n:
    try:
        n = int(raw_input('How many plates will you need to scan? > '))
        assert n > 0
    except Exception:
        n = None
        print 'Invalid input'

plateStart = None
while plateStart==None:
    try:
        plateStart = int(raw_input('Set the index number for the first image. This should normally be 0 or 1 but might be different. > '))
    except Exception:
        plateStart = None
        print 'Invalid input'

prefix = None
while not prefix:
    try:
        i = raw_input('Plate image files will be prepended by the current date YYYYMMDD by default. I believe the current date is %s. Enter y to accept this or define another prefix. The prefix should not contain any spaces or weird characters. > '%time.strftime('%Y%m%d'))
        if i=='y':
            prefix = time.strftime('%Y%m%d')
        else:
            prefix = i
            assert ' ' not in prefix
            print 'Successfully defined custom prefix: '+prefix
    except Exception:
        prefix = None
        print 'Invalid input'

postfix = None
while not postfix:
    try:
        postfix = raw_input('Set the postfix for your image file names. This should normally be your name or an ID of the experiment you are doing. The postfix should not contain any spaces or weird characters. > ')
        assert ' ' not in postfix
    except Exception:
        postfix = None
        print 'Invalid input'
        
saveRaw = None
while saveRaw==None:
    try:
        i = raw_input('Do you want to save the raw, uncropped scans? Please type y or n. > ')
        if i=='y':
            saveRaw = True
        if i=='n':
            saveRaw = False
        else:
            raise Exception
    except Exception:
        saveRaw = None
        print 'Invalid input'

print '''Ready to start scanning using the following parameters:
Number of plates to scan: %i
Start numbering at: %i
Prefix: %s
Postfix: %s
save raw scans?: %s'''%(n, plateStart, prefix, postfix, str(saveRaw))

nscans = int(np.ceil(n/4.0))
labels = map(str, range(plateStart, plateStart+n))
labels += ['empty', 'empty', 'empty']#Max number of emtpy bays in last scan
for i in range(1, nscans+1):
    print 'Preparing to for scan %i out of %i'%(i,nscans)
    print 'Please load the scanner as follows:'
    print 'Bay 1 -> Plate %s, Bay 2 -> Plate %s, Bay 3 -> Plate %s, Bay 4 -> Plate %s'%tuple(labels[(i-1)*4:(i-1)*4+4])
    
    ready = None
    while not ready:
        try:
            i = raw_input('If ready, enter y to start scan')
            if i == 'y':
                ready = True
            else:
                raise Exception
        except Exception:
            print 'Invalid input'
    
    #scan

print 'Done with scanning. Please wait a few seconds while all your images are being cropped'


print 'Done'
    
    
    
    
