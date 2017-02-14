# plate-scanner
Plate-scanner: A lightweight script for scanning plate batches. After collecting some meta-data from the user, 
images are acquired using SANE and then cropped using ImageMagick.

To use the NanoDrop, reboot/turn on the laptop and select Windows in boot menu.

To scan plates:
1. Boot Ubuntu and log in

2. Open the file manager and navigate to the folder in which you want to save your images. The script will create a sub-folder that begins with the current date to save all your images. 

3. Right click and select 'Open in Terminal'

4. Type in 'plate-scanner' and follow the on-screen instructions. 

Tips:
- Wipe off any condensation from your plate bottoms. Remove lids before scanning.
- When you are done, please wipe down the scanner with a soft tissue. Do not use ethanol.
- The folder raw_scans will contain the original scans, please check these if you suspect that the automatic numbering is wrong.
