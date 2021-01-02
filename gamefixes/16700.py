""" Fixes for Stronghold Crusader Extreme HD
Imported from fixes for Stronghold Crusader HD (40970)
"""
from protonfixes import util


def main():
    """
    Enable virtual desktop and install corefonts, directplay
    """

    util.protontricks('vd=1280x720')
    util.protontricks('corefonts')

    util.protontricks('directplay')
