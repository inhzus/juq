# -*- coding: utf-8 -*-
# created by inhzus

from os.path import expanduser

import yaml


class Config:
    # Configuration
    API_BASE_URL = 'https://www.yuque.com/api/v2'
    API_APP_NAME = 'juq'
    TIMEOUT = 5

    # Constant
    CONFIG_PATH = expanduser('~/.juq')

    def __init__(self):
        self.fields = {}
        for k in dir(self):
            v = getattr(self, k)
            self.fields[k] = v
        try:
            with open(Config.CONFIG_PATH, 'r') as fin:
                self.data: dict = yaml.safe_load(fin)
        except FileNotFoundError:
            self.data = {}

    def __getitem__(self, item):
        if item in self.data:
            return self.data[item]
        elif item in self.fields:
            return self.fields[item]
        else:
            raise KeyError('Configuration attribute not found: %s. '
                           'Please set it in \"%s\" first.' % (item, Config.CONFIG_PATH))

    def __contains__(self, item):
        return item in self.data or item in self.fields

    def __del__(self):
        # if len(self.data):
        #     with open(Config.CONFIG_PATH, 'w') as out:
        #         yaml.dump(self.data, out)
        pass


config = Config()


if __name__ == '__main__':
    print(config['API_BASE_URL'])
