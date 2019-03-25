# -*- coding: utf-8 -*-
# created by inhzus

from typing import Callable
from juq.exceptions import RequestException, EXCEPTION_MESSAGE_MAP


class Caller:
    @staticmethod
    def call(func: Callable, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except RequestException as e:
            print(EXCEPTION_MESSAGE_MAP[e.__class__])
            exit(1)


if __name__ == '__main__':
    pass
