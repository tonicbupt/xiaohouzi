import os
from PIL import Image


def fill(path, new_path):
    with Image.open(path) as img:
        x, y = img.size
        if 3 * x <= 4 * y:
            fill1(path, new_path, img, x, y)
        else:
            fill2(path, new_path, img, x, y)


def fill1(path, new_path, img, x, y):
    filename = os.path.basename(path)
    name, ext = filename.rsplit('.', 1)
    xx = int(y * 4 / 3)
    with Image.new('RGB', (int(xx), y), (255, 255, 255)) as p:
        p.paste(img, (int((xx - x) / 2), 0))
        p.save(os.path.join(new_path, '{}_4_3.{}'.format(name, ext)))


def fill2(path, new_path, img, x, y):
    filename = os.path.basename(path)
    name, ext = filename.rsplit('.', 1)
    yy = int(x * 3 / 4)
    with Image.new('RGB', (x, int(yy)), (255, 255, 255)) as p:
        p.paste(img, (0, int((yy - y) / 2)))
        p.save(os.path.join(new_path, '{}_4_3.{}'.format(name, ext)))


def main():
    dpath = 'pictures_4_3'
    os.makedirs(dpath)
    for f in os.listdir('.'):
        filename = os.path.join(os.getcwd(), f)
        ext = filename.split('.')[-1]
        if ext.lower() not in ('jpg', 'jpeg', 'png'):
            continue
        fill(filename, dpath)


if __name__ == '__main__':
    main()
