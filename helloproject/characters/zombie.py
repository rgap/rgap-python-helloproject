#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This changes the properties of an audio file.

Usage:
    zombie.py <asset>
    zombie.py -h

Arguments:
    asset   string (path to image)
"""

# FIXME:
# TODO:

try:
    from helloproject.character import BaseCharacter
except ImportError:
    from character import BaseCharacter


class Zombie(BaseCharacter):
    """
    Implements a zombie class
    """

    def __init__(
            self,
            asset,
            speed=1.0,
            speed_boost=2.0,
            **kwargs
    ):
        """Zombie constructor
        :param asset: Asset
        :type asset: str
        :param speed: Speed
        :type speed: float
        :param speed_boost: Speed
        :type speed_boost: float

        .. note::
            * Sample class
            * Zombie class notes
        """

        assert isinstance(speed_boost, (int, float)), "speed_boost has to be int or float"

        super().__init__(
            asset,
            speed,
            **kwargs
        )
        self.speed_boost = speed_boost

    @property
    def speed_boost(self):
        """Asset decorator
        :return: Speed Boost
        :rtype: float
        """
        return self.__speed_boost

    @speed_boost.setter
    def speed_boost(self, speed_boost):
        """Asset setter
        :param speed_boost: Speed Boost
        :type speed_boost: float
        """
        assert speed_boost > 0, "speed must be a positive number"
        # if speed < 0:
        #     raise ValueError("speed must be a positive number")
        self.__speed_boost = speed_boost

    def follow(self):
        """Follows sth"""
        print('follow')

    def eat(self):
        """Eats sth"""
        print('eat')


def main(args):
    asset = args['<asset>']

    zombie = Zombie(asset, 1.0, 2.0)
    print(zombie.speed_boost)
    zombie.speed_boost = 10.0
    print(zombie.__dict__)

    zombie.asset = 'asset2'
    print(zombie.asset)

    zombie.make_random_noise()


if __name__ == "__main__":
    from docopt import docopt

    main(docopt(__doc__))
