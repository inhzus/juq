# -*- coding: utf-8 -*-
# created by inhzus

from dataclasses import dataclass

# from juq.serializer import UserSerializer, BookSerializer
from .book_serializer import BookSerializer
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
    book: BookSerializer
    # user: UserSerializer
    last_editor: UserSerializer
    cover: str
    custom_description: str


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
