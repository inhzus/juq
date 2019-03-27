# -*- coding: utf-8 -*-
# created by inhzus

import dataclasses

from juq.serializer import *


class SerializerBuilder:
    STR_CLASS_MAP = {
        'v2.book': RepoSerializer,
        'v2.book_toc': RepoTocSerializer,
        'v2.book_detail': RepoDetailSerializer,
        'v2.doc': DocSerializer,
        'v2.doc_detail': DocDetailSerializer,
        'v2.group_user': GroupUserSerializer,
        **dict.fromkeys(('v2.user', 'v2.group'), UserSerializer),
        **dict.fromkeys(('v2.group_detail', 'v2.user_detail'), UserDetailSerializer)
    }

    @staticmethod
    def _gen_serializer(param: dict):
        if '_serializer' not in param:
            if 'body_html' in param:
                param['_serializer'] = 'v2.doc_detail'
            elif 'slug' in param:
                param['_serializer'] = 'v2.book_toc'
            else:
                return None
        serializer = SerializerBuilder.STR_CLASS_MAP[param['_serializer']]
        field_names = set(f.name for f in dataclasses.fields(serializer))
        candi = {k: None for k in field_names}
        candi.update({k: v for k, v in param.items() if k in field_names})
        return serializer(**candi)

    @staticmethod
    def build(param: dict):
        data = param.pop('data')
        if not isinstance(data, dict):
            return [SerializerBuilder._gen_serializer(item) for item in data]
        # data['abilities'] = param['abilities'] if 'abilities' in param else None
        # data['meta'] = param['meta'] if 'meta' in param else None
        data.update(param)
        return SerializerBuilder._gen_serializer(data)


if __name__ == '__main__':
    pass
