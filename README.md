![screenshot]("/screenshot.png")

## Summary:
These scripts fetch the did you know and news sections from wikipedia. They're made to be used with conky, so I've also included my conkyrc files and a script for wifi signal strength.

## Dependencies:
BeautifulSoup

## Installation

1. Put dyk.py and news.py in your $PATH (something like ~/bin or ~/scripts). Make sure they're chmod +x'd
2. If you want the clock window, you'll also need the signalstrength\_now.sh script in your $PATH. You might also need to find a DotMatrix.ttf or similar font if it's not already on your system. Alternatively just comment out the line from .conkyrc_clock
3. Put fetchy/ in ~/.conky/fetchy
4. Run conkystart.sh, you might want to put this file in your $PATH as well.


