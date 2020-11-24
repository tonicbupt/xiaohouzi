#!/usr/bin/env python

import os
import argparse
from PIL import Image


def fill(path, new_path):
    with Image.open(path) as img:
        x, y = img.size
        if 3 * x <= 4 * y:
            return fill1(path, new_path, img, x, y)
        else:
            return fill2(path, new_path, img, x, y)


def fill1(path, new_path, img, x, y):
    filename = os.path.basename(path)
    name, ext = filename.rsplit('.', 1)
    xx = int(y * 4 / 3)

    new_name = '{}_4_3.{}'.format(name, ext)
    with Image.new('RGB', (int(xx), y), (255, 255, 255)) as p:
        p.paste(img, (int((xx - x) / 2), 0))
        p.save(os.path.join(new_path, new_name))
    return new_name


def fill2(path, new_path, img, x, y):
    filename = os.path.basename(path)
    name, ext = filename.rsplit('.', 1)
    yy = int(x * 3 / 4)

    new_name = '{}_4_3.{}'.format(name, ext)
    with Image.new('RGB', (x, int(yy)), (255, 255, 255)) as p:
        p.paste(img, (0, int((yy - y) / 2)))
        p.save(os.path.join(new_path, new_name))
    return new_name


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', nargs='?', default='.', help='source dir for pictures, default current dir')
    parser.add_argument('target', nargs='?', default='pictures_4_3', help='target dir name for pictures, default pictures_4_3')
    args = parser.parse_args()

    os.chdir(args.source)
    dpath = os.path.join(os.getcwd(), args.target)
    os.makedirs(dpath)

    for f in os.listdir('.'):
        filename = os.path.join(os.getcwd(), f)
        ext = filename.split('.')[-1]
        if ext.lower() not in ('jpg', 'jpeg', 'png'):
            continue
        fill(filename, dpath)
        print('{} to {}'.format(filename, dpath))


if __name__ == '__main__':
    main()
