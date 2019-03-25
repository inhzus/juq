# -*- coding: utf-8 -*-
# created by inhzus
from pprint import pprint
from typing import Union, List

from juq.misc.request import Request
from juq.misc.decorators import necessary_params
from juq.serializer import UserDetailSerializer, DocSerializer, BookSerializer


def get_user_info_anonymous(id_: Union[int, str]) -> UserDetailSerializer:
    uri = f'/users/{id_}'
    method = 'GET'
    anonymous = True
    return Request.send(method, uri, anonymous=anonymous)


def get_user_info() -> UserDetailSerializer:
    uri = f'/user'
    method = 'GET'
    return Request.send(method, uri)


def get_user_docs(**kwargs) -> List[DocSerializer]:
    """

    Keyword Args:
        q (str): 文档标题模糊搜索
        offset (int): 分页偏移, 每页 20 条

    Returns:

    """
    uri = f'/user/docs'
    method = 'GET'
    return Request.send(method, uri, data=kwargs)


@necessary_params(('type',))
def get_recent_updated(**kwargs) -> Union[List[DocSerializer], List[BookSerializer]]:
    """

    Keyword Args:
        type (str): 'Doc', 'Book'
        offset (int): 分页偏移, 每页 20 条

    Returns:

    """
    uri = f'/user/recent-updated'
    method = 'GET'
    return Request.send(method, uri, data=kwargs)


if __name__ == '__main__':
    # pprint(UserHandler.get_user_info_anonymous('inhzus'))
    pprint(get_recent_updated(type='Doc'))
    pass
