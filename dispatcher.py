#!/user/bin/env python3 -tt

# Imports
import sys
import configparser
import multiprocessing
from test1 import *
from test2 import *
# import os

# Global variables


# Class declarations


class Dispatcher:
    def __init__(self):
        self.modArray = []
        self.processes = []
        self.config = configparser.ConfigParser()

    def setup(self, filename):
        print(filename)

        if self.config.read(filename) == False:
            print("Could't read config file: ", filename)
            return False

    def addModule(self, name):
        self.modArray.append(name)

    def exec(self, mod, cmd):
        className = eval(mod[0:].capitalize())
        try:
            if cmd == 'init':
                getattr(className, cmd)(className, mod, self.config[mod])
            else:
                getattr(className, cmd)(className)
        except AttributeError:
            raise NotImplementedError("Class `{}` does not implement `{}`".format(
                'className'.__class__.__name__, 'init'))

    def runModules(self):
        self.initModules()
        self.startModules()


    def initModules(self):
        for mod in self.modArray:
            self.exec(mod, 'init')

    def startModules(self):
        for mod in self.modArray:
            className = eval(mod[0:].capitalize())
            t = multiprocessing.Process(target=className.loop, args=())
            self.processes.append(t)
            t.start()

        for one_process in self.processes:
            one_process.join()

    def stopModules(self):
        self.exec(mod, 'stop')

    def printModules(self):
        for mod in self.modArray:
            print(mod)
