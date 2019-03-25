# -*- coding: utf-8 -*-
# created by inhzus


from dataclasses import dataclass


# class UserSerializer:
#     # noinspection PyShadowingBuiltins
#     def __init__(self, id: int, type: str, login: str, name: str, avatar_url: str, created_at: str, updated_at: str):
#         self.id = id
#         self.type = type
#         self.login = login
#         self.name = name
#         self.avatar_url = avatar_url
#         self.created_at = created_at
#         self.updated_at = updated_at
# UserSerializer = namedtuple('UserSerializer', "id type login name avatar_url created_at updated_at")


@dataclass
class GroupSerializer:
    id: int
    login: str
    name: str
    description: str
    avatar_url: str
    large_avatar_url: str
    medium_avatar_url: str
    small_avatar_url: str
    created_at: str
    updated_at: str


@dataclass
class GroupDetailSerializer(GroupSerializer):
    space_id: int
    books_count: int
    public_books_count: int
    public: int
    owner_id: int = 0
    abilities: dict = None
    members_count: int = 0


@dataclass
class UserSerializer(GroupSerializer):
    type: str
    followers_count: int
    following_count: int


@dataclass
class UserDetailSerializer(GroupDetailSerializer):
    type: str = None
    account_id: int = 0


if __name__ == '__main__':
    import json

    d = json.loads(
        '{'
        '"id": 13,'
        '"type": "a",'
        '"login": "b",'
        '"name": "c",'
        '"avatar_url": "d",'
        '"created_at": "e",'
        '"updated_at": "f"'
        '}')
    u = UserSerializer(**d)
