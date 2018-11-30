#!/user/bin/env python3 -tt

# Imports
import sys


class Test1:
    def __init__(self):
        self.state = 'stop'
        self.moduleName = ''
        self.enable = False
        self.count = 0

    def init(self, name, config):
        self.moduleName = name
        self.state = sys._getframe(0).f_code.co_name

        self.enable = config['enable']
        self.count = config['count']

        print(self.moduleName, self.state, self.enable, self.count)

    def start(self):
        self.state = sys._getframe(0).f_code.co_name
        print(self.moduleName, self.state)

    def loop(self):
        self.state = sys._getframe(0).f_code.co_name
        print(self.moduleName, self.state)

    def stop(self):
        self.state = sys._getframe(0).f_code.co_name
        print(self.moduleName, self.state)
