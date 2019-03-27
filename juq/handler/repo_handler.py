# -*- coding: utf-8 -*-
# created by inhzus

from pprint import pprint
from typing import Union, List

from juq.misc.decorators import necessary_params
from juq.misc.request import Request
from juq.serializer import RepoSerializer, RepoDetailSerializer, RepoTocSerializer


def get_user_repos(user_id: Union[int, str], **kwargs) -> List[RepoSerializer]:
    """
    获取 User 的全部 Repos

    Args:
        user_id: User 的 {login} 或 {id}

    Keyword Args:
        type (str): Book, Design, all
        offset (int): 用于分页, 一页 20 条

    Returns:
        User 的 Repos 列表
    """
    uri = f'/users/{user_id}/repos'
    method = 'GET'
    anonymous = True
    return Request.send(method, uri, data=kwargs, anonymous=anonymous)


def get_group_repos(group_id: Union[int, str], **kwargs) -> List[RepoSerializer]:
    """
    获取 Group 的全部 Repos

    Args:
        group_id: Group 的 {login} 或 {id}

    Keyword Args:
        type (str): Book, Design, all
        offset (int): 用于分页, 一页 20 条

    Returns:
        Group 的 Repos 列表
    """
    uri = f'/groups/{group_id}/repos'
    method = 'GET'
    anonymous = True
    return Request.send(method, uri, data=kwargs, anonymous=anonymous)


@necessary_params(('name', 'slug',))
def create_user_repo(user_id: Union[int, str], **kwargs) -> RepoDetailSerializer:
    """
    在自己账户下创建 Repo

    Args:
        user_id: User 的 {login} 或 {id}

    Keyword Args:
        name (str): Repo 名称
        slug (str): Repo 路径
        description (str): Repo 介绍
        public (int): 0: 私密, 1: 内网公开, 2: 全网公开
        type (str): Book, Design

    Returns:
        创建的 Repo 的详细信息
    """
    uri = f'/users/{user_id}/repos'
    method = 'POST'
    return Request.send(method, uri, data=kwargs)


@necessary_params(('name', 'slug',))
def create_group_repo(group_id: Union[int, str], **kwargs) -> RepoDetailSerializer:
    """
    在 Group 中创建 Repo

    Args:
        group_id: Group 的 {login} 或 {id}

    Keyword Args:
        name (str): Repo 名称
        slug (str): Repo 路径
        description (str): Repo 介绍
        public (int): 0: 私密, 1: 内网公开, 2: 全网公开
        type (str): Book, Design

    Returns:
        创建的 Repo 的详细信息
    """
    uri = f'/groups/{group_id}/repos'
    method = 'POST'
    return Request.send(method, uri, data=kwargs)


def get_repo_info(id_: Union[int, str], **kwargs) -> RepoDetailSerializer:
    """
    获取 Repo
    Args:
        id_: Repo id

    Keyword Args:
        type (str): Repo 类型, Book, Design

    Returns:
        Repo 的详细信息
    """
    uri = f'/repos/{id_}'
    method = 'GET'
    anonymous = True
    return Request.send(method, uri, data=kwargs, anonymous=anonymous)


def update_repo_info(id_: Union[int, str], **kwargs) -> RepoDetailSerializer:
    """
    更新 Repo

    Args:
        id_: Repo id

    Keyword Args:
        name (str): Repo 名称
        slug (str): Repo 路径
        toc (str): Repo 目录信息
        description (str): Repo 介绍
        public (int): 0: 私密, 1: 内网公开, 2: 全网公开

    Returns:
        Repo 的详细信息
    """
    uri = f'/repos/{id_}'
    method = 'PUT'
    return Request.send(method, uri, data=kwargs)


def delete_repo(id_: Union[int, str]) -> RepoDetailSerializer:
    """
    删除 Repo

    Args:
        id_: Repo id

    Returns:
        Repo 的详细信息
    """
    uri = f'/repos/{id_}'
    method = 'DELETE'
    return Request.send(method, uri)


def get_repo_toc(id_: Union[int, str]) -> List[RepoTocSerializer]:
    """
    获取 Repo 的目录结构

    Args:
        id_: Repo id

    Returns:
        Repo 的目录结构
    """
    uri = f'/repos/{id_}/toc'
    method = 'GET'
    return Request.send(method, uri)


def search_repos(q: str, type_: str = "") -> List:
    """
    在全部 Repos 中搜索

    Args:
        q: 搜索关键词
        type_: Book, Design

    Returns:
        搜索 Repos 列表
    """
    uri = f'/search/repos?q={q}&type={type_}'
    method = 'GET'
    return Request.send(method, uri)


if __name__ == '__main__':
    # print(RepoHandler.get_user_repos_anonymous('nju_nova'))
    pprint(get_repo_info('yuque/developer'))
    # pprint(RepoHandler.search_repos('api', 'Book'))
    pass
