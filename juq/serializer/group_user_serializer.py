# -*- coding: utf-8 -*-
# created by inhzus

from dataclasses import dataclass

from .user_serializer import UserDetailSerializer, GroupSerializer


@dataclass
class GroupUserSerializer:
    id: int
    group_id: int
    group: GroupSerializer
    user_id: int
    user: UserDetailSerializer
    role: int
    status: int
    created_at: str
    updated_at: str


if __name__ == '__main__':
    pass
