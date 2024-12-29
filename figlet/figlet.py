from pyfiglet import Figlet
import random as random
import sys

try:
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        s = input("Input: ")
        fnt = random.choices(fonts)
        fnt = str(fnt[0])
        figlet.setFont(font = fnt )
        print(f"Output: {figlet.renderText(s)}")
    elif len(sys.argv)== 3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font"):
        if sys.argv[2] in fonts:
            s = input("Input: ")
            figlet.setFont(font = sys.argv[2])
            print(f"Output: {figlet.renderText(s)}")
        else:
            sys.exit(1)
    else:
        sys.exit(1)
except:
    print("Invalid usage")
    sys.exit(1)

