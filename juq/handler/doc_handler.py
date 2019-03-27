# -*- coding: utf-8 -*-
# created by inhzus

from typing import Union, List

from juq.misc.decorators import necessary_params
from juq.misc.request import Request
from juq.serializer import DocDetailSerializer, DocSerializer


def get_repo_docs(repo_id: Union[int, str]) -> List[DocSerializer]:
    """
    获取 Repo 的 Docs

    Args:
        repo_id: Repo id

    Returns:
        Repo 的全部 Docs 列表
    """
    uri = f'/repos/{repo_id}/docs'
    method = 'GET'
    return Request.send(method, uri)


def get_doc_info(repo_id: Union[int, str], id_: Union[int, str], **kwargs) -> DocDetailSerializer:
    """
    获取某个 Repo 中某个 Doc

    Args:
        repo_id: Repo id
        id_: Doc {slug} 或 {id}

    Keyword Args:
        raw (int): raw=1 返回文档最原始的格式

    Returns:
        Doc 的详细信息
    """
    uri = f'/repos/{repo_id}/docs/{id_}'
    method = 'GET'
    return Request.send(method, uri, kwargs)


@necessary_params(('title', 'slug', 'body',))
def create_doc(repo_id: Union[int, str], **kwargs) -> DocDetailSerializer:
    """
    在 Repo 下创建 Doc

    Args:
        repo_id: Repo id

    Keyword Args:
        title: Doc 标题
        slug: 文档路径名
        public: 0 私密, 1 公开
        format: markdown / lake, 默认 markdown
        body: format 描述的正文, 最大 5MB

    Returns:
        创建的 Doc 的详细信息
    """
    uri = f'/repos/{repo_id}/docs'
    method = 'POST'
    return Request.send(method, uri, kwargs)


def update_doc(repo_id: Union[int, str], id_: Union[int, str], **kwargs) -> DocDetailSerializer:
    """
    更新 Repo 中的 Doc

    Args:
        repo_id: Repo id
        id_: Doc id, 不允许使用 {slug}

    Keyword Args:
        title: Doc 标题
        slug: 文档路径名
        public: 0 私密, 1 公开
        body: 仅支持 markdown, 不能更新原文为 lake 格式的 Doc, 最大 5MB

    Returns:
        更新的 Doc 详细信息
    """
    uri = f'/repos/{repo_id}/docs/{id_}'
    method = 'PUT'
    return Request.send(method, uri, kwargs)


def delete_doc(repo_id: Union[int, str], id_: Union[int, str]) -> DocDetailSerializer:
    """
    删除 Repo 中的 Doc

    Args:
        repo_id: Repo id
        id_: Doc id, 可能不支持 {slug}

    Returns:
        被删除的 Doc 的详细信息
    """
    uri = f'/repos/{repo_id}/docs/{id_}'
    method = 'DELETE'
    return Request.send(method, uri)


if __name__ == '__main__':
    pass
