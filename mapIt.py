#! python3
# mapIt.py - this script launches a map in the browser using an address from the
# command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # get address from command line.
    address = ''.join(sys.argv[1:])


else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address)
