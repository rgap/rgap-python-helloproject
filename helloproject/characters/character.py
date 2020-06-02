#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: ADD MORE PATTERNS


class BaseCharacter:
    """Base class

    .. note::
        Base class
    """

    def __init__(
            self, asset, speed, _id=0
    ):
        """Constructor for BaseModel.
        """
        assert isinstance(asset, str)
        assert isinstance(speed, (int, float))
        assert speed > 0, "speed must be a positive number"
        # if speed < 0:
        #     raise ValueError("speed must be a positive number")
        self.speed = speed
        self.asset = asset
        self._id = _id

    def __str__(self):
        print("Character: speed {}, {}, {}".format(self.speed, self.asset, self._id))

    @staticmethod
    def make_random_noise():
        print('NOISE')
