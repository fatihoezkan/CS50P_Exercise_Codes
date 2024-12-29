import sys
from PIL import Image, ImageOps

def main():
    check()
    dress()


def check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments ")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    first = str(sys.argv[1])
    second = str(sys.argv[2])

    if not second[-4:] in ['.png', '.jpg', 'jpeg']  :
        sys.exit("Invalid output")

    if first[-4:] != second[-4:]:
        sys.exit("Input and output have different extensions")


def dress():

    image = Image.open(f"{sys.argv[1]}")
    shirt = Image.open("shirt.png")
    #get size
    size = shirt.size

    #resize muppet image to fit shirt
    kukla = ImageOps.fit(image, size)

    #paste

    kukla.paste(shirt,shirt)

    kukla.save(sys.argv[2])






if __name__ == "__main__":
    main()
