#!/user/bin/env python3 -tt
"""
Module documentation.
"""

# Imports
import sys
from dispatcher import Dispatcher
import argparse

#import os


# Global variables

# Class declarations

# Function declarations


def main():
    print("main")
    dispatcher = Dispatcher()
    dispatcher.addModule('test1')
    dispatcher.addModule('test2')

    dispatcher.setup('./config.ini')

    dispatcher.initModules()
    # dispatcher.startModules()
    # dispatcher.loopModules()
    # dispatcher.stopModules()

    # Main body
if __name__ == '__main__':
    main()
