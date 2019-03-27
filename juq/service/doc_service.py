# -*- coding: utf-8 -*-
# created by inhzus

import hashlib
from os.path import basename

from juq.handler import doc_handler, repo_handler
from juq.utils import parse_md
from .utils import filter_empty_params, change_doc_toc, dump_toc, toc_repr, load_toc


def info(repo_id: str, id_: str, **_):
    return doc_handler.get_doc_info(repo_id, id_)


def toc(repo_id: str, id_: str, before: str = '', after: str = '', depth: int = 0, **_):
    src_toc = repo_handler.get_repo_info(repo_id).toc
    insert = doc_handler.get_doc_info(repo_id, id_)
    toc_ = change_doc_toc(src_toc, insert, before, after, depth)
    repo_handler.update_repo_info(repo_id, toc=dump_toc(toc_))
    return toc_repr(load_toc(repo_handler.get_repo_info(repo_id).toc))
    # return '\n'.join(map(toc_line_repr, load_toc(repo_handler.get_repo_info(repo_id).toc)))


def create(repo_id: str, file: str, slug: str, title: str, public: int, **_):
    params = filter_empty_params(locals())
    title = basename(file)
    params.setdefault('title', title)
    params.setdefault('slug', hashlib.md5(f'{title}'.encode('utf-8')).hexdigest()[:7])
    params['body'] = parse_md(file)
    ret = doc_handler.create_doc(**params)
    toc(repo_id, str(ret.id))
    return ret


def update(repo_id: str, id_: str, file: str, slug: str, title: str, public: int, **_):
    params = filter_empty_params(locals())
    params['body'] = parse_md(file)
    return doc_handler.update_doc(**params)


def delete(repo_id: str, id_: str, **_):
    return doc_handler.delete_doc(repo_id, id_)
