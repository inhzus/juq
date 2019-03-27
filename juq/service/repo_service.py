# -*- coding: utf-8 -*-
# created by inhzus

from juq.handler import repo_handler, doc_handler, user_handler
from .utils import filter_empty_params, load_toc, toc_repr


# noinspection PyShadowingBuiltins
def info(id_: str, type: str, **_):
    return repo_handler.get_repo_info(**filter_empty_params(locals()))


def toc(id_: str, **_):
    src_toc = repo_handler.get_repo_info(id_).toc
    if not src_toc:
        return 'Empty'
    # return '\n'.join(map(toc_line_repr, load_toc(src_toc)))
    return toc_repr(load_toc(src_toc))


# noinspection PyShadowingBuiltins
def search(q: str, type: str, **_):
    return '\n'.join(map(repr, repo_handler.search_repos(**filter_empty_params(locals()))))


def docs(repo_id: str, **_):
    return '\n'.join(map(repr, doc_handler.get_repo_docs(repo_id=repo_id)))


# noinspection PyShadowingBuiltins
def create(group_id: str, name: str, slug: str, description: str, public: int, **_):
    params = filter_empty_params(locals())
    if 'group_id' in params:
        return repo_handler.create_group_repo(**params)
    else:
        user_id = str(user_handler.get_user_info().id)
        return repo_handler.create_user_repo(user_id, **params)


def update(id_: str, name: str, slug: str, description: str, public: int, **_):
    return repo_handler.update_repo_info(**filter_empty_params(locals()))


def delete(id_: str, **_):
    return repo_handler.delete_repo(id_)
