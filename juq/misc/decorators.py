# -*- coding: utf-8 -*-
# created by inhzus

from juq.misc.exceptions import MissingFieldsException
from juq.serializer import SerializerBuilder

import types


def necessary_params(params: tuple):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for nec in params:
                if nec not in kwargs.keys():
                    raise MissingFieldsException(f'Param field "{nec}" missing.')
            return func(*args, **kwargs)
        return wrapper
    return decorator


def _build_serializer_for_function(func):
    def wrapper(*args, **kwargs):
        return SerializerBuilder.build(func(*args, **kwargs))
    return wrapper


def build_serializer(module):
    for name in dir(module):
        method = getattr(module, name)
        if isinstance(method, types.FunctionType):
            setattr(module, name, _build_serializer_for_function(method))
    return module
