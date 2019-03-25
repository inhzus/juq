# -*- coding: utf-8 -*-
# created by inhzus

from pprint import pprint
from typing import Union, List

from juq.misc.decorators import necessary_params
from juq.misc.request import Request
from juq.serializer import BookSerializer, BookDetailSerializer, BookTocSerializer


def get_user_repos(user_id: Union[int, str], **kwargs) -> List[BookSerializer]:
    uri = f'/users/{user_id}/repos'
    method = 'GET'
    anonymous = True
    return Request.send(method, uri, data=kwargs, anonymous=anonymous)


def get_group_repos(group_id: Union[int, str], **kwargs) -> List[BookSerializer]:
    uri = f'/groups/{group_id}/repos'
    method = 'GET'
    anonymous = True
    return Request.send(method, uri, data=kwargs, anonymous=anonymous)


@necessary_params(('name', 'slug',))
def create_user_repo(user_id: Union[int, str], **kwargs) -> BookDetailSerializer:
    uri = f'/users/{user_id}/repos'
    method = 'POST'
    return Request.send(method, uri, data=kwargs)


@necessary_params(('name', 'slug',))
def create_group_repo(group_id: Union[int, str], **kwargs) -> BookDetailSerializer:
    uri = f'/groups/{group_id}/repos'
    method = 'POST'
    return Request.send(method, uri, data=kwargs)


def get_repo_info(id_: Union[int, str], **kwargs) -> BookDetailSerializer:
    uri = f'/repos/{id_}'
    method = 'GET'
    anonymous = True
    return Request.send(method, uri, data=kwargs, anonymous=anonymous)


def update_repo_info(id_: Union[int, str], **kwargs) -> BookDetailSerializer:
    uri = f'/repos/{id_}'
    method = 'PUT'
    return Request.send(method, uri, data=kwargs)


def delete_repo(id_: Union[int, str], **kwargs) -> BookDetailSerializer:
    uri = f'/repos/{id_}'
    method = 'DELETE'
    return Request.send(method, uri, data=kwargs)


def get_repo_toc(id_: Union[int, str], **kwargs) -> List[BookTocSerializer]:
    uri = f'/repos/{id_}/toc'
    method = 'GET'
    return Request.send(method, uri, data=kwargs)


def search_repos(q: str, type_: str = "") -> List:
    uri = f'/search/repos?q={q}&type={type_}'
    method = 'GET'
    return Request.send(method, uri)


if __name__ == '__main__':
    # print(RepoHandler.get_user_repos_anonymous('nju_nova'))
    pprint(get_repo_info('yuque/developer'))
    # pprint(RepoHandler.search_repos('api', 'Book'))
    pass
