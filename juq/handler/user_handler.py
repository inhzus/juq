# -*- coding: utf-8 -*-
# created by inhzus
from pprint import pprint
from typing import Union, List

from juq.misc.request import Request
from juq.misc.decorators import necessary_params
from juq.serializer import UserDetailSerializer, DocSerializer, RepoSerializer


def get_user_info_anonymous(id_: Union[int, str]) -> UserDetailSerializer:
    """
    获取某一 User 的详细信息

    Args:
        id_: 用户的 {login} 或 {id}

    Returns:
        User 详细信息
    """
    uri = f'/users/{id_}'
    method = 'GET'
    anonymous = True
    return Request.send(method, uri, anonymous=anonymous)


def get_user_info() -> UserDetailSerializer:
    """
    获取 TOKEN User 的详细信息

    Returns:
        TOKEN User 的详细信息
    """
    uri = f'/user'
    method = 'GET'
    return Request.send(method, uri)


def get_user_docs(**kwargs) -> List[DocSerializer]:
    """
    获取 TOKEN User 的全部 Docs

    Keyword Args:
        q (str): 文档标题模糊搜索
        offset (int): 分页偏移, 每页 20 条

    Returns:
        User Docs (20 条)列表
    """
    uri = f'/user/docs'
    method = 'GET'
    return Request.send(method, uri, data=kwargs)


@necessary_params(('type',))
def get_recent_updated(**kwargs) -> Union[List[DocSerializer], List[RepoSerializer]]:
    """
    获取 TOKEN User 的最近更新动态

    Keyword Args:
        type (str): 'Doc', 'Book'
        offset (int): 分页偏移, 每页 20 条

    Returns:
        User 最近更新的 Doc 或 Repo 列表
    """
    uri = f'/user/recent-updated'
    method = 'GET'
    return Request.send(method, uri, data=kwargs)


if __name__ == '__main__':
    # pprint(UserHandler.get_user_info_anonymous('inhzus'))
    pprint(get_recent_updated(type='Doc'))
    pass
