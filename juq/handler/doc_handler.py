# -*- coding: utf-8 -*-
# created by inhzus

from typing import Union

from juq.misc.decorators import necessary_params
from juq.misc.request import Request


def get_repo_docs(repo_id: Union[int, str]):
    uri = f'/repos/{repo_id}/docs'
    method = 'GET'
    return Request.send(method, uri)


def get_doc_info(repo_id: Union[int, str], id_: Union[int, str], **kwargs):
    uri = f'/repos/{repo_id}/docs/{id_}'
    method = 'GET'
    return Request.send(method, uri, kwargs)


@necessary_params(('title', 'slug', 'body',))
def create_doc(repo_id: Union[int, str], **kwargs):
    uri = f'/repos/{repo_id}/docs'
    method = 'POST'
    return Request.send(method, uri, kwargs)


def update_doc(repo_id: Union[int, str], id_: Union[int, str], **kwargs):
    uri = f'/repos/{repo_id}/docs/{id_}'
    method = 'PUT'
    return Request.send(method, uri, kwargs)


def delete_doc(repo_id: Union[int, str], id_: Union[int, str]):
    uri = f'/repos/{repo_id}/docs/{id_}'
    method = 'DELETE'
    return Request.send(method, uri)


if __name__ == '__main__':
    pass
