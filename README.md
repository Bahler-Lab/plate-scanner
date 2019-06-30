# plate-scanner
Plate-scanner: A lightweight script for scanning plate batches written by Stephan Kamrad (stephan.kamrad@crick.ac.uk). On a linux operating system, this tool can be used to acquire scan aimges (using SANE) which are then cropped using ImageMagick.

## Installation
1. Make sure your scanner is installed correctly and you can acquire images using the scanimage command. We use the TPU8x10 transmission scanning source on an Epson V800 Photo scanner. This was first implemented in by Zackrisson et al in the [scanomatics pipeline](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5015956/) and requires the installation of a hacked SANE driver. See the instructions in their [wiki](https://github.com/Scan-o-Matic/scanomatic/wiki/Installing-scanners) for how to do this.

2. Make sure [ImageMagick](https://imagemagick.org/index.php) is installed and can be called from the command line.

3. Clone this repository and add the folder to your path. You should now be able to run the program by typing 'scanplates' in your terminal.

4. With a laser cutter, make a fixture to hold your plates in place. We provide an svg file with the cutting shape in this repository. Use tape to hold your fixture into place, it should be pushed against the back of the scanner (where the cables are) with the top of the plates facing left. Scanplates uses the position of the four placeholders for cropping of individual plate images from the initial scan image. If you are using your own fixture, see below of how to add the geometry information to scanplates. 

## Scan plates 

1. Open the file manager and navigate to the folder in which you want to save your images. The script will create a sub-folder that begins with the current date to save all your images. 

2. Right click and select 'Open in Terminal'

3. Run scanplates with the options as detaild below. 

```
usage: scanplates [-h] [-i] [--nplates NPLATES] [--start START]
                  [--prefix PREFIX] [--postfix POSTFIX]
                  [--fixture {som3_edge,pp2,pp1,null,som3_noEdge_sameGrid,petrie1,square1,som2,maria}]
                  [--resolution {150,300,600,900,1200}] [--scanner {1,2,3}]
                  [--mode {Gray,Color}]

Welcome to scanplates. Written by stephan.kamrad@crick.ac.uk and maintained at
https://github.com/Bahler-Lab/scanplates.

optional arguments:
  -h, --help            show this help message and exit
  -i                    Use interactive mode for setting arguments.
  --nplates NPLATES     Number of plates to scan. This defaults to 100 and the
                        script can be terminated by Ctr+C when done.
  --start START         Where to start numbering from. Defaults to 1.
  --prefix PREFIX       Name prefix for output files. The default is the
                        current date YYYYMMDD.
  --postfix POSTFIX     Name postfix for output files. Defaults to empty
                        string.
  --fixture {som3_edge,pp2,pp1,null,som3_noEdge_sameGrid,petrie1,square1,som2,maria}
                        ID of the fixture you are using.
  --resolution {150,300,600,900,1200}
                        Resolution for scanning in dpi. Default is 600.
  --scanner {1,2,3}     Which scanner to use. Scanners are not uniquely
                        identified and may switch when turned off/unplugged.
                        This option does not need to be set when only one
                        scanner is connected.
  --mode {Gray,Color}   Which color mode to use for scanning. Defaults to
                        Gray. Use Color for phloxine B colour images.
```

All arguments except the fixture have default values and are optional.

## Tips and Tricks:
- Wipe off any condensation from your plate bottoms. Remove lids before scanning.
- When you are done, please wipe down the scanner with a soft tissue. Do not use ethanol.
- The folder raw_scans will contain the original scans, please check these if you suspect that the automatic numbering is wrong.
- Press Ctr+C at any time to terminate the program
- The program will terminate and you have to start from the beginning if you try to create a folder with the same postfix on the same day. 
- For Singer Plates, with the new som3 fixture, there are now two supported cropping modes. som3_edge will include edges of the plate, which sometimes helps with gitter's thresholding. With som3_noEdge_sameGrid, images will not contain the edge but colonies will be in the same position for all 4 images. This makes use of gitterbatch() with reference image and spotsizer two in batch/timecourse mode a lot easier.

## Using your own fixtures
You can use your own fixtures with varying number and shapes of plate holders. In order for the cropping to work, you need to provide information describing the position of plates in your fixture. Open the scanplates program in a text editor, towards the top you will find the definition of a python dictionary called 'geometries'. Each key in this dictionary is the name of a fixture which can be used in the --fixture argument. Each value is a list of strings, with each string defining the position of a plate in scanned image (or raw_scan), following the [format of ImageMagick](https://www.imagemagick.org/Magick++/Geometry.html). For your own fixture, add an entry to the dictionary following the format above.