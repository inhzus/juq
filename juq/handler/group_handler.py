# -*- coding: utf-8 -*-
# created by inhzus
from typing import Union, List

from juq.misc.request import Request
from juq.serializer import UserSerializer, GroupDetailSerializer, GroupUserSerializer, GroupSerializer


def get_user_groups(user_id: Union[int, str]) -> List[UserSerializer]:
    """
    获取指定 User 的全部 Groups

    Args:
        user_id: 指定 User 的 {login} 或 {id}

    Returns:
        Group 列表, 语雀这里将 Group 均视作 User.
    """
    uri = f'/users/{user_id}/groups'
    method = 'GET'
    anonymous = True
    return Request.send(method, uri, anonymous=anonymous)


def get_public_groups() -> List[UserSerializer]:
    """
    获取一些社区公开的 Groups

    Returns:
        Group 列表
    """
    uri = f'/groups'
    method = 'GET'
    return Request.send(method, uri)


def create_group(**kwargs) -> GroupDetailSerializer:
    """
    创建 Group

    Keyword Args:
        name (str): Group 名称
        login (str): Group 路径名
        description (str): 介绍

    Returns:
        创建的 Group 详细信息
    """
    uri = f'/groups'
    method = 'POST'
    return Request.send(method, uri, data=kwargs)


def get_group_info(id_: Union[int, str]) -> GroupSerializer:
    """
    获取 Group
    Args:
        id_: Group {login} 或 {id}

    Returns:
        id_ 对应的 Group
    """
    uri = f'/groups/{id_}'
    method = 'GET'
    anonymous = True
    return Request.send(method, uri, anonymous=anonymous)


def update_group_info(id_: Union[int, str], **kwargs) -> UserSerializer:
    """
    更新 Group 信息

    Keyword Args:
        name (str): Group 名称
        login (str): Group 路径名
        description (str): 介绍

    Args:
        id_: 更新的 Group 的 {login} 或 {id}

    Returns:
        更新的 Group
    """
    uri = f'/groups/{id_}'
    method = 'PUT'
    return Request.send(method, uri, data=kwargs)


def delete_group(id_: Union[int, str]) -> GroupDetailSerializer:
    """
    删除 Group
    Args:
        id_: Group 的 {login} 或 {id}

    Returns:
        删除的 Group 详细信息
    """
    uri = f'/groups/{id_}'
    method = 'DELETE'
    return Request.send(method, uri)


def get_group_users(id_: Union[int, str]) -> List[GroupUserSerializer]:
    """
    获取某个 Group 的成员
    Args:
        id_: Group 的 {login} 或 {id}

    Returns:
        Group 成员列表
    """
    uri = f'/groups/{id_}/users'
    method = 'GET'
    return Request.send(method, uri)


def add_or_update_group_user(group_id: Union[int, str], login: str, **kwargs) -> GroupUserSerializer:
    """
    向 Group 添加 User 或 更新 User 权限
    Args:
        group_id: Group 的 {login} 或 {id}
        login: User 的 {login}, 不确定 {id} 是否可行

    Keyword Args:
        role: 0: 管理员; 1: 普通成员

    Returns:
        添加或更新的 User 的成员信息
    """
    uri = f'/groups/{group_id}/users/{login}'
    method = 'PUT'
    return Request.send(method, uri, data=kwargs)


def delete_group_user(group_id: Union[int, str], login: str):
    """
    从 Group 中删除 User
    Args:
        group_id: Group 的 {login} 或 {id}
        login: User 的 {login}, 不确定 {id} 是否可行

    Returns:
        删除的 User 的成员信息
    """
    uri = f'/groups/{group_id}/users/{login}'
    method = 'DELETE'
    return Request.send(method, uri)


if __name__ == '__main__':
    from pprint import pprint

    pprint(get_group_users('nju_nova'))
    pass
