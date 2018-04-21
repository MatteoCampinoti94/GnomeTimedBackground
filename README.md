# GnomeTimedBackground
Utility program that takes all the pictures in a folder and uses them to create an xml file that transitions through them with duration set by the user and optional shuffling and transitions.

## Usage
Run through interpreter or compiled.

`timebackground.py [options]`

Options:
* `-d [path]` Specify a directory where to search images, if directory does not exist current one will be used instead.
* `-t [time]` Specify the time in seconds that each image will be shown (fractions of a second accepted, e.g. 0.3).
* `-r` Randomize Images
* `-T` Enable 1 second transitions between images.

The program will create a 'background.xml' file in the folder the program is run into.

`findimage.py background.xml`
