import sys
import time
import numpy as np
from subprocess import check_output
from os import mkdir
#import tqdm

manualStr = '''
Welcome. This script will help you acquire images in batches using the custom set-up implemented by Stephan and John.
'''

#Additional parameters, change if you know what you are doing
geometries = ['1800x2700+310+130', 
'1800x2700+2550+130',
'1800x2700+310+3290',
'1800x2700+2550+3290',
]

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
        
if False:#Deprecated, remove eventually
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
'''%(n, plateStart, prefix, postfix)

wdir = '%s_%s/'%(prefix,postfix)
mkdir(wdir)
rdir = wdir + 'raw_scans/'
mkdir(rdir)
print 'Successfully created directories. Please make sure the scanner is turned on.'

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
            inp = raw_input('If ready, enter y to start scan > ')
            if inp == 'y':
                ready = True
            else:
                raise Exception
        except Exception:
            print 'Invalid input'
    
    cmdStr = 'scanimage --source TPU8x10 --mode Gray --resolution 600 --format=tiff  > %s%s_rawscan%s_%s.tiff'%(rdir, prefix, i, postfix)
    check_output(cmdStr, shell=True)

    for plate in range(4):
        plateNr = (i-1)*4+plate
        if plateNr < n:
            cmdStr = 'convert %s%s_rawscan%s_%s.tiff -crop %s +repage -rotate 90 %s%s_%i_%s.tiff'%(rdir, prefix, i, postfix, geometries[plate], wdir, prefix, plateNr+plateStart, postfix)
            check_output(cmdStr, shell=True)
        
print 'Done'
    
    
    
    
