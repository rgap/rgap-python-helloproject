#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This is the main file

Usage:
    helloproject.py <asset>
    helloproject.py -h

Arguments:
    asset   string (path to image)
"""

from characters.zombie import Zombie


def hello():
    print('Hello!')


def hellov2():
    print('Hello_v2!')


def hello_zombie(asset):
    zombie = Zombie(asset)
    zombie.follow()


def main(args):
    asset = args['<asset>']
    hello_zombie(asset)


if __name__ == "__main__":
    from docopt import docopt

    main(docopt(__doc__))
