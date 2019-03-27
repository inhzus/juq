# -*- coding: utf-8 -*-
# created by inhzus

from dataclasses import dataclass
from colorama import Fore, Style

from .book_serializer import RepoSerializer
from .user_serializer import UserSerializer


@dataclass
class DocSerializer:
    id: int
    slug: str
    title: str
    description: str
    user_id: str
    book_id: int
    format: str
    public: int
    status: int
    likes_count: int
    comments_count: int
    content_updated_at: str
    created_at: str
    updated_at: str
    published_at: str
    first_published_at: str
    draft_version: int
    last_editor_id: int
    word_count: int
    book: RepoSerializer
    last_editor: UserSerializer
    cover: str
    custom_description: str

    def __repr__(self):
        return f'id: {Fore.BLUE}{self.id}{Style.RESET_ALL}\t' \
               f'slug: {Fore.BLUE}{self.slug}{Style.RESET_ALL}\t' \
               f'title: {Fore.BLUE}{self.title}{Style.RESET_ALL}'


@dataclass
class DocDetailSerializer(DocSerializer):
    body: str
    body_draft: str
    body_html: str
    body_lake: str
    creator: UserSerializer
    creator_id: int
    deleted_at: str
    abilities: dict

    def __repr__(self):
        return f'     id: {Fore.BLUE}{self.id}{Style.RESET_ALL}\n' \
               f'   slug: {Fore.BLUE}{self.slug}{Style.RESET_ALL}\n' \
               f'  title: {Fore.BLUE}{self.title}{Style.RESET_ALL}\n' \
               f'user_id: {Fore.BLUE}{self.user_id}{Style.RESET_ALL}\n' \
               f'book_id: {Fore.BLUE}{self.book_id}{Style.RESET_ALL}\n' \
               f'updated: {Fore.BLUE}{self.updated_at}{Style.RESET_ALL}'


if __name__ == '__main__':
    import json


    class TestSerializer:
        def __init__(self, slug: int, user: UserSerializer):
            self.slug = slug
            self.user = user


    d = json.loads(
        '{'
        '"slug": 1,'
        '"user": {'
        '"id": 13,'
        '"type": "a",'
        '"login": "b",'
        '"name": "c",'
        '"avatar_url": "d",'
        '"created_at": "e",'
        '"updated_at": "f"'
        '}}')
    t = TestSerializer(**d)
    i = 0
