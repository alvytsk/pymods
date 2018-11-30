#!/user/bin/env python3 -tt
"""
Module documentation.
"""

# Imports
import sys
from dispatcher import Dispatcher
#import os

# Global variables

# Class declarations

# Function declarations


def main():
    print("main")
    dispatcher = Dispatcher()
    dispatcher.addModule('test1')
    dispatcher.addModule('test2')
    dispatcher.printModules()

    # Main body
if __name__ == '__main__':
    main()
