from pathlib import Path
from PIL import Image


def convert_to_webp(source, x):
    """Convert image to webp.

    Args:
        source (pathlib.Path): Path to source image

    Returns:
        pathlib.Path: path to new image
    """
    destination = Path("output/" + str(x) + ".webp")

    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    # return destination


def main():
    for x in range(1, 1501):
        print(x)
        path = Path("images/" + str(x) + ".png")
        convert_to_webp(path, x)


main()