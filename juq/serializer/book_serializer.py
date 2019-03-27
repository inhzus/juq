# -*- coding: utf-8 -*-
# created by inhzus

from dataclasses import dataclass

from colorama import Fore, Style

from .user_serializer import UserSerializer


@dataclass
class RepoSerializer:
    id: int
    type: str
    slug: str
    name: str
    user_id: int
    user: UserSerializer
    public: int
    items_count: int
    likes_count: int
    watches_count: int
    created_at: str
    updated_at: str
    description: str
    creator_id: int
    namespace: str

    def __repr__(self):
        return f'id: {Fore.BLUE}{self.id}{Style.RESET_ALL}\t' \
               f'slug: {Fore.BLUE}{self.slug}{Style.RESET_ALL}\t' \
               f'name: {Fore.BLUE}{self.name}{Style.RESET_ALL}'


@dataclass
class RepoDetailSerializer(RepoSerializer):
    toc: str
    toc_yml: str
    archived_at: str
    pinned_at: str
    abilities: dict = None

    def __repr__(self):
        return f'     id: {Fore.BLUE}{self.id}{Style.RESET_ALL}\n' \
               f'   slug: {Fore.BLUE}{self.slug}{Style.RESET_ALL}\n' \
               f'   name: {Fore.BLUE}{self.name}{Style.RESET_ALL}\n' \
               f'  items: {Fore.BLUE}{self.items_count}{Style.RESET_ALL}\n' \
               f' public: {Fore.BLUE}{self.public}{Style.RESET_ALL}\n' \
               f'user_id: {Fore.BLUE}{self.user_id}{Style.RESET_ALL}\n' \
               f'updated: {Fore.BLUE}{self.updated_at}{Style.RESET_ALL}'


@dataclass
class RepoTocSerializer:
    title: str
    slug: str
    depth: int

    def __repr__(self):
        return '|-' * self.depth + \
               f'depth: {Fore.BLUE}{self.depth}{Style.RESET_ALL}\t' \
               f'slug: {Fore.BLUE}{self.slug}{Style.RESET_ALL}\t' \
               f'title: {Fore.BLUE}{self.title}{Style.RESET_ALL}'
