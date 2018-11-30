#!/user/bin/env python3 -tt

# Imports
import sys
#import os

# Global variables

# Class declarations


class Dispatcher:
    def __init__(self):
        self.cfgFilePath = ''
        self.modArray = []

    def addModule(self, name):
        self.modArray.append(name)

    def printModules(self):
        for mod in self.modArray:
            print(mod)
        # Function declarations
