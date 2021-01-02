"""Fixes for Stronghold Crusader HD
"""
from protonfixes import util


def main():
    """
    Enable virtual desktop and install corefonts, directplay
    """

    util.protontricks('vd=1280x720')
    util.protontricks('corefonts')

    util.protontricks('directplay')