# -*- coding: utf-8 -*-
# created by inhzus


from dataclasses import dataclass

from colorama import Fore, Style


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


@dataclass(repr=False)
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

    def __repr__(self):
        return f'id: {Fore.BLUE}{self.id}{Style.RESET_ALL}\t' \
               f'login: {Fore.BLUE}{self.login}{Style.RESET_ALL}\t' \
               f'name: {Fore.BLUE}{self.name}{Style.RESET_ALL}\t'


@dataclass(repr=False)
class GroupDetailSerializer(GroupSerializer):
    space_id: int
    books_count: int
    public_books_count: int
    public: int
    owner_id: int
    abilities: dict
    members_count: int

    def __repr__(self):
        return f'     id: {Fore.BLUE}{self.id}{Style.RESET_ALL}\n' \
               f'  login: {Fore.BLUE}{self.login}{Style.RESET_ALL}\n' \
               f'   name: {Fore.BLUE}{self.name}{Style.RESET_ALL}\n' \
               f'   desc: {Fore.BLUE}{self.description}{Style.RESET_ALL}\n' \
               f'  books: {Fore.BLUE}{self.books_count}{Style.RESET_ALL}\n' \
               f'  owner: {Fore.BLUE}{self.owner_id}{Style.RESET_ALL}\n' \
               f'members: {Fore.BLUE}{self.members_count}{Style.RESET_ALL}'


@dataclass(repr=False)
class UserSerializer(GroupSerializer):
    type: str
    followers_count: int
    following_count: int

    # def __repr__(self):
    #     return f'id: {Fore.BLUE}{self.id}{Style.RESET_ALL}\t' \
    #            f'login: {Fore.BLUE}{self.id}{Style.RESET_ALL}\t' \
    #            f'name: {Fore.BLUE}{self.id}{Style.RESET_ALL}'


@dataclass(repr=False)
class UserDetailSerializer(GroupDetailSerializer):
    type: str
    account_id: int

    def __repr__(self):
        return f'   id: {Fore.BLUE}{self.id}{Style.RESET_ALL}\n' \
               f'login: {Fore.BLUE}{self.login}{Style.RESET_ALL}\n' \
               f' name: {Fore.BLUE}{self.name}{Style.RESET_ALL}\n' \
               f' desc: {Fore.BLUE}{self.description}{Style.RESET_ALL}'


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
