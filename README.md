#Julia Set Animator
The Julia set, defined by a complex number c, is every point z in the complex plane that does not approach infinity when repeatedly squared and added to c. If your screen resolution and computing time are high enough, the points that remain ("prisoners") can create a fractal shape.

julia_anim.py accepts a beginning c and an end c, then evenly spaces out intermediate c's and creates a frame for each Julia set, and then it stores each frame in an animated gif. You can specify any amount of intermediate frames that you wish.

This script does not contribute any creative mathematics to this process. I only wanted to write it for making pretty pictures.

This creates a folder in the directory you run the script from, named "ja-$timestamp", and puts all the frames and final gif in there.

##Dependencies
On Ubuntu I had to install the "python-tk" apt package, to get matplotlib to show plots. The other python libraries were built-in or I installed them pretty easily with pip (imageio, numpy, matplotlib, argparse).

##Arguments
./julia_anim.py -h  

|  |  |
|:---|:---|
|  -h, --help            |show this help message and exit|
|  -sr SR                |start real|
|  -si SI                |start imag|
|  -er ER                |end real|
|  -ei EI                |end imag|
|  -frames FRAMES        |number of frames|
|  -spacesize SPACESIZE  |pixels in each dimension|
|  -fg FG                |color of prisoner points|
|  -bg BG                |color of the complex plane|
|  -rev                  |reverse animation (doubles frames in output gif)|
|  -o O                  |filename|
  
  
The first frame will be defined by the starting complex c, composed of (sr, si) and the final frame will be defined by the end c, which is assigned as (er, ei). spacesize controls how many pixels will be tested as escapees within the complex plane. Using -rev will animate frames generated between the start and end constants, then will animate in the reverse order back to the start frame.

The bg and fg parameters accept RRGGBB hex values preceded by a hash. In bash the hash mark has to be escaped with \ or the entire value put in quotes.

##Examples
These use a spacesize of 512 which takes all day to generate, since it's squaring complex numbers 200 * 512 * 512 times each (52428800), for each frame. An animation with the default 60 frames and a spacesize of 64 would take a few minutes.

![](samples/a/a.gif)  
./julia_anim.py -sr=0.34379 -er=0.34379 -si=-0.356086 -ei=-0.05086 -spacesize 512 -fg \#bdded6 -bg \#2b3331  

![](samples/b/b.gif)  
./julia_anim.py -sr=-0.47 -er=0.338 -si=-0.326 -ei=-0.647 -spacesize 512 -fg \#ff99ff -bg \#56178c  

![](samples/c/c.gif)  
./julia_anim.py -sr=-0.71883 -er=0.23961 -si=0.0 -ei=0.0 -rev -spacesize 512 -fg \#82f0fa -bg \#000000  

![](samples/d/d.gif)  
./julia_anim.py -sr=0.0 -er=0.0 -si=-0.6123 -ei=0.6123 -spacesize 512 -fg \#68b654 -bg \#040804  

##Misc
If you have any issues, suggestions, or questions, e-mail slorm@tutanota.de.
