#!/user/bin/env python3 -tt

# Imports
import sys
import configparser
from test1 import *
from test2 import *
# import os

# Global variables


# Class declarations


class Dispatcher:
    def __init__(self):
        self.modArray = []
        self.config = configparser.ConfigParser()

    def setup(self, filename):
        print(filename)

        if self.config.read(filename) == False:
            print("Could't read config file: ", filename)
            return False

    def addModule(self, name):
        self.modArray.append(name)

    def initModules(self):
        for mod in self.modArray:
            className = eval(mod[0:].capitalize())

            try:
                getattr(className, 'init')(className, mod, self.config[mod])
            except AttributeError:
                raise NotImplementedError("Class `{}` does not implement `{}`".format(
                    'className'.__class__.__name__, 'init'))

    def startModules(self):
        for mod in self.modArray:
            className = eval(mod[0:].capitalize())

            try:
                getattr(className, 'start')(className)
            except AttributeError:
                raise NotImplementedError("Class `{}` does not implement `{}`".format(
                    'className'.__class__.__name__, 'start'))

    def loopModules(self):
        for mod in self.modArray:
            className = eval(mod[0:].capitalize())

            try:
                getattr(className, 'loop')(className)
            except AttributeError:
                raise NotImplementedError("Class `{}` does not implement `{}`".format(
                    'className'.__class__.__name__, 'loop'))

    def stopModules(self):
        for mod in self.modArray:
            className = eval(mod[0:].capitalize())

            try:
                getattr(className, 'stop')(className)
            except AttributeError:
                raise NotImplementedError("Class `{}` does not implement `{}`".format(
                    'className'.__class__.__name__, 'stop'))

    def printModules(self):
        for mod in self.modArray:
            print(mod)
