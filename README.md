# plate-scanner
Plate-scanner: A lightweight script for scanning plate batches. After collecting some meta-data from the user, 
images are acquired using SANE and then cropped using ImageMagick.

To use the NanoDrop, reboot/turn on the laptop and select Windows in boot menu.

To scan plates:

1. Boot Ubuntu and log in. The account is                and the password is                

2. Open the file manager and navigate to the folder in which you want to save your images. The script will create a sub-folder that begins with the current date to save all your images. 

3. Right click and select 'Open in Terminal'

4. Type in 'plate-scanner' and follow the on-screen instructions. 

Tips:
- Wipe off any condensation from your plate bottoms. Remove lids before scanning.
- When you are done, please wipe down the scanner with a soft tissue. Do not use ethanol.
- The folder raw_scans will contain the original scans, please check these if you suspect that the automatic numbering is wrong.
- Press Ctr+C at any time to terminate the program
- The program will terminate and you have to start from the beginning if you try to create a folder with the same postfix on the same day. 

- For Singer Plates. With the new scanomatic fixture (ID: som3), there are now two supported cropping modes. som3_edge will include edges of the plate, which sometimes helps with gitter's thresholding. With som3_noEdge_sameGrid, images will not contain the edge but colonies will be in the same position for all 4 images. This makes use of gitterbatch() with reference image and spotsizer two in batch/timecourse mode a lot easier.

# Scan a single image directly
This offers more flexibility and can be easier if you just want to scan one image. Go to the command line and run:

scanimage --source TPU8x10 --mode Gray --resolution 600 --format=tiff  > outputImage.tiff  
  
Source: This can be TPU8x10 or Flatbed. The first is transmission as used by sacnomatic, the second is a reflective mode. When using reflective mode, cover the glass surface of the lid with the white inset.   
Mode: This should be Gray or Color  
Resolution: in dpi  
Format: This must be tiff. JPG or other compressed formats are not allowed. If you want a jpg run this after scanning: convert yourImage.tiff yourImage.jpg

