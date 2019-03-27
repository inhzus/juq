# -*- coding: utf-8 -*-
# created by inhzus

from juq.handler import group_handler, repo_handler
from .utils import filter_empty_params


# noinspection PyShadowingBuiltins
def info(id_: str, **_):
    return group_handler.get_group_info(id_=id_)


# noinspection PyShadowingBuiltins
def repos(group_id: str, type: str, offset: int, **_):
    return '\n'.join(map(repr, repo_handler.get_group_repos(**filter_empty_params(locals()))))
