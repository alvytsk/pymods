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
    dispatcher.setup('./config.ini')
    
    dispatcher.addModule('test1')
    dispatcher.addModule('test2')

    dispatcher.runModules()

    # Main body
if __name__ == '__main__':
    main()
