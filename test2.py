#!/user/bin/env python3 -tt

# Imports
import sys


class Test2:
    def __init__(self):
        self.state = 'stop'
        self.moduleName = ''
        self.enable = False
        self.output = ''

    def init(self, name, config):
        self.moduleName = name
        self.state = sys._getframe(0).f_code.co_name

        self.enable = config['enable']
        self.output = config['output']

        print(self.moduleName, self.state, self.enable, self.output)

    def loop(self):
        time.sleep(random.randint(1,4))
        print("[{0}] Hello!".format(self.moduleName))

    def stop(self):
        self.state = sys._getframe(0).f_code.co_name
        print(self.moduleName, self.state)
