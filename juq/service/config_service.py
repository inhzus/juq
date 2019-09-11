# -*- coding: utf-8 -*-
# created by inhzus

from juq.config import config


# noinspection PyShadowingBuiltins
def set(key: str, value: str, **_):
    config[key] = str(value)
    config.save()
    return ''


def get(key: str, **_):
    return config[key]


def reset(**_):
    config.data.clear()
    config.save()
    return ''
