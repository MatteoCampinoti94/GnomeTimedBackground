# GnomeTimedBackground
Utility program that takes all the pictures in a folder and uses them to create an xml file that transitions through them with duration set by the user and optional shuffling and transitions

## Usage
Run through interpreter or compiled.
First argument has to be the duration of each image, expressed in seconds with an integer or float. Duration can be omitted.

Argument `random` shuffles images, omitting it sorts them by name.

Argument `transition` enables transitions between images. Transitions last 1 second. **Warning**: transitions don't seem to work at the moment.