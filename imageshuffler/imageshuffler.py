from PIL import Image
import argparse

chunks = [
    {'x': 0, 'y': 0, 'w': 200, 'h': 280, 'dstx': 0, 'dsty': 0},
    {'x': 200, 'y': 0, 'w': 200, 'h': 280, 'dstx': 0, 'dsty': 280},
    {'x': 400, 'y': 0, 'w': 200, 'h': 280, 'dstx': 0, 'dsty': 560},
    {'x': 600, 'y': 0, 'w': 200, 'h': 280, 'dstx': 0, 'dsty': 840},

    {'x': 0, 'y': 280, 'w': 200, 'h': 280, 'dstx': 200, 'dsty': 0},
    {'x': 200, 'y': 280, 'w': 200, 'h': 280, 'dstx': 200, 'dsty': 280},
    {'x': 400, 'y': 280, 'w': 200, 'h': 280, 'dstx': 200, 'dsty': 560},
    {'x': 600, 'y': 280, 'w': 200, 'h': 280, 'dstx': 200, 'dsty': 840},

    {'x': 0, 'y': 560, 'w': 200, 'h': 280, 'dstx': 400, 'dsty': 0},
    {'x': 200, 'y': 560, 'w': 200, 'h': 280, 'dstx': 400, 'dsty': 280},
    {'x': 400, 'y': 560, 'w': 200, 'h': 280, 'dstx': 400, 'dsty': 560},
    {'x': 600, 'y': 560, 'w': 200, 'h': 280, 'dstx': 400, 'dsty': 840},

    {'x': 0, 'y': 840, 'w': 200, 'h': 280, 'dstx': 600, 'dsty': 0},
    {'x': 200, 'y': 840, 'w': 200, 'h': 280, 'dstx': 600, 'dsty': 280},
    {'x': 400, 'y': 840, 'w': 200, 'h': 280, 'dstx': 600, 'dsty': 560},
    {'x': 600, 'y': 840, 'w': 200, 'h': 280, 'dstx': 600, 'dsty': 840},
]


def process(sourcefilename, destfilename):
    srcimg = Image.open(sourcefilename)
    dstimg = Image.open(sourcefilename)
    for chunk in chunks:
        srcbox = (chunk['x'], chunk['y'], chunk['x'] + chunk['w'], chunk['y'] + chunk['h'])
        region = srcimg.crop(srcbox)

        dstbox = (chunk['dstx'], chunk['dsty'], chunk['dstx'] + chunk['w'], chunk['dsty'] + chunk['h'])
        dstimg.paste(region, dstbox)

    dstimg.save(destfilename, "JPEG")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('sourcefilename')
    parser.add_argument('destfilename')
    args = parser.parse_args()
    process(args.sourcefilename, args.destfilename)
