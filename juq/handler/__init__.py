# -*- coding: utf-8 -*-
from . import doc_handler, group_handler, repo_handler, user_handler

# if config['SERIALIZE']:
#     build_serializer(doc_handler)
#     build_serializer(group_handler)
#     build_serializer(repo_handler)
#     build_serializer(user_handler)

__all__ = [
    'doc_handler', 'group_handler', 'repo_handler', 'user_handler'
]
