# -*- coding: utf-8 -*-
# created by inhzus

from dataclasses import dataclass

from .user_serializer import UserSerializer


@dataclass
class BookSerializer:
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


@dataclass
class BookDetailSerializer(BookSerializer):
    toc: str
    toc_yml: str
    archived_at: str
    pinned_at: str
    abilities: dict = None


@dataclass
class BookTocSerializer:
    title: str
    slug: str
    depth: int


if __name__ == '__main__':
    pass
