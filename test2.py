#!/user/bin/env python3 -tt

# Imports
import sys
# import os

# Global variables

# Class declarations


class Test2:
    def __init__(self):
        self.state = 'stopped'
        self.moduleName = ''

    def init(self, name):
        self.moduleName = name
        print(self.moduleName, "init")

    def start(self):
        print(self.moduleName, "start")

    def loop(self):
        print(self.moduleName, "loop")

    def stop(self):
        print(self.moduleName, "stop")
