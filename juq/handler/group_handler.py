# -*- coding: utf-8 -*-
# created by inhzus
from typing import Union, List

from juq.misc.request import Request
from juq.serializer import UserSerializer, GroupDetailSerializer, GroupUserSerializer, GroupSerializer


def get_user_groups(user_id: Union[int, str]) -> List[UserSerializer]:
    uri = f'/users/{user_id}/groups'
    method = 'GET'
    anonymous = True
    return Request.send(method, uri, anonymous=anonymous)


def get_public_groups() -> List[UserSerializer]:
    uri = f'/groups'
    method = 'GET'
    return Request.send(method, uri)


def create_group(**kwargs) -> GroupDetailSerializer:
    """

    Keyword Args:
        name (str): 组织名称
        login (str): login
        description (str): 介绍

    Returns:

    """
    uri = f'/groups'
    method = 'POST'
    return Request.send(method, uri, data=kwargs)


def get_group_info(id_: Union[int, str]) -> GroupSerializer:
    uri = f'/groups/{id_}'
    method = 'GET'
    anonymous = True
    return Request.send(method, uri, anonymous=anonymous)


def update_group_info(id_: Union[int, str], **kwargs):
    """

    Keyword Args:
        name (str): 组织名称
        login (str): login
        description (str): 介绍

    Args:
        id_:

    Returns:

    """
    uri = f'/groups/{id_}'
    method = 'PUT'
    return Request.send(method, uri, data=kwargs)


def delete_group(id_: Union[int, str]) -> GroupDetailSerializer:
    uri = f'/groups/{id_}'
    method = 'DELETE'
    return Request.send(method, uri)


def get_group_users(id_: Union[int, str]) -> List[GroupUserSerializer]:
    uri = f'/groups/{id_}/users'
    method = 'GET'
    return Request.send(method, uri)


def add_or_update_group_user(group_id: Union[int, str], login: str, **kwargs):
    uri = f'/groups/{group_id}/users/{login}'
    method = 'PUT'
    return Request.send(method, uri, data=kwargs)


def delete_group_user(group_id: Union[int, str], login: str):
    uri = f'/groups/{group_id}/users/{login}'
    method = 'DELETE'
    return Request.send(method, uri)


if __name__ == '__main__':
    from pprint import pprint

    pprint(get_group_users('nju_nova'))
    pass
