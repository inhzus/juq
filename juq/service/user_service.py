# -*- coding: utf-8 -*-
# created by inhzus

from juq.handler import user_handler, group_handler, repo_handler
from .utils import filter_empty_params


def info(id_: str = '', **_):
    if not id_:
        info_ = user_handler.get_user_info()
    else:
        info_ = user_handler.get_user_info_anonymous(id_)
    return info_


def docs(q: str, offset: int, **_):
    docs_ = user_handler.get_user_docs(**filter_empty_params(locals()))
    return '\n'.join(map(repr, docs_))


def groups(id_: str, **_):
    user_info = info(id_)
    return '\n'.join(map(repr, group_handler.get_user_groups(user_info.id)))


# noinspection PyShadowingBuiltins
def repos(id_: str, type: str, offset: int, **_):
    user_info = info(id_)
    return '\n'.join(map(repr, repo_handler.get_user_repos(user_info.id, **filter_empty_params(locals()))))


# noinspection PyShadowingBuiltins
def recent(type: str, offset: int, **_):
    return '\n'.join(map(repr, user_handler.get_recent_updated(**filter_empty_params(locals()))))
