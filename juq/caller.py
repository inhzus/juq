# -*- coding: utf-8 -*-
# created by inhzus

import argparse

from colorama import Fore, Style

# noinspection PyUnresolvedReferences
from juq.service import user_service, group_service, repo_service, doc_service


def p(id_, **_):
    print(f'what does {id_} says')


def set_user_parser(user_parser: argparse.ArgumentParser):
    _parser = user_parser.add_subparsers(dest='user')
    _parser.required = True

    info = _parser.add_parser('info')
    info.add_argument('id_', help='Login or id', nargs='?', default='', type=str, metavar='id')

    docs = _parser.add_parser('docs')
    docs.add_argument('-q', help='Search keywords', default='', type=str)
    docs.add_argument('--offset', '-o', help='Page offset', default=0, type=int)

    _parser.add_parser('groups')

    repos = _parser.add_parser('repos')
    repos.add_argument('--type', '-t', choices=['Book', 'Design', 'all'],
                       help='[Book|Design|all]', default='all')
    repos.add_argument('--offset', '-o', help='Page offset', default=0, type=int)

    recent = _parser.add_parser('recent')
    recent.add_argument('--type', '-t', choices=['Book', 'Doc'], help='[Book|Doc]',
                        type=str, default='Book')
    recent.add_argument('--offset', '-o', help='Page offset', default=0, type=int)


def set_group_parser(group_parser: argparse.ArgumentParser):
    _parser = group_parser.add_subparsers(dest='group')
    _parser.required = True

    info = _parser.add_parser('info')
    info.add_argument('id_', help='Login or id', default='', type=str, metavar='group_id')

    repos = _parser.add_parser('repos')
    repos.add_argument('group_id', help='Group login or id', type=str)
    repos.add_argument('--type', '-t', choices=['Book', 'Design', 'all'], default='all')
    repos.add_argument('--offset', '-o', help='Page offset', default=0, type=int)


def set_repo_parser(repo_parser: argparse.ArgumentParser):
    _parser = repo_parser.add_subparsers(dest='repo')
    _parser.required = True

    info = _parser.add_parser('info')
    info.add_argument('id_', help='[user_id|group_id]/repo_slug or repo_id',
                      type=str, metavar='repo_id')
    info.add_argument('--type', '-t', choices=['Book', 'Design'],
                      help='[Book|Design]', default='Book')

    toc = _parser.add_parser('toc')
    toc.add_argument('id_', help='[user_id|group_id]/repo_slug or repo_id',
                     type=str, metavar='repo_id')

    docs = _parser.add_parser('docs')
    docs.add_argument('repo_id', help='[user_id|group_id]/repo_slug or repo_id', type=str)

    search = _parser.add_parser('search')
    search.add_argument('q', help='Search keywords', type=str)
    search.add_argument('--type', '-t', choices=['Book', 'Design'],
                        help='[Book|Design]', default='Book')


def set_doc_parser(doc_parser: argparse.ArgumentParser):
    _parser = doc_parser.add_subparsers(dest='doc')
    _parser.required = True

    info = _parser.add_parser('info')
    info.add_argument('repo_id', help='[user_id|group_id]/repo_slug or repo_id', type=str)
    info.add_argument('id_', help='Doc id', type=str, metavar='doc_id')

    toc = _parser.add_parser('toc')
    toc.add_argument('repo_id', help='[user_id|group_id]/repo_slug or repo_id', type=str)
    toc.add_argument('id_', help='Doc id', type=str, metavar='doc_id')
    pos = toc.add_mutually_exclusive_group(required=True)
    pos.add_argument('--before', '-b', help='Doc id to insert before', default='', type=str)
    pos.add_argument('--after', '-a', help='Doc id to insert after', default='', type=str)
    toc.add_argument('--depth', '-d', help='Doc toc depth', default=0, type=int)

    create = _parser.add_parser('create')
    create.add_argument('repo_id', help='[user_id|group_id]/repo_slug or repo_id', type=str)
    create.add_argument('file', help='Markdown file location', type=str)
    create.add_argument('--slug', '-s', help='Unique identifier', default='', type=str)
    create.add_argument('--title', '-t', help='Doc title', default='', type=str)
    create.add_argument('--public', '-p', action='store_const', const=1, default=0)


def get_func(args_):
    return getattr(globals()[f'{args_.sub}_service'],
                   getattr(args_, args_.sub))


parser = argparse.ArgumentParser()
sub_parser = parser.add_subparsers(dest='sub')
sub_parser.required = True

set_user_parser(sub_parser.add_parser('user', help='User operations'))
set_group_parser(sub_parser.add_parser('group', help='Group operations'))
set_repo_parser(sub_parser.add_parser('repo', help='Repo operations'))
set_doc_parser(sub_parser.add_parser('doc', help='Doc operations'))


def run():
    # args = parser.parse_args('doc toc inhzus/book 1396908 -b 1396889'.split())
    args = parser.parse_args()
    # noinspection PyBroadException
    try:
        print(getattr(
            globals()[f'{args.sub}_service'],
            getattr(args, args.sub))
              (**vars(args)))
    except Exception as e:
        print(f'Error: {Fore.RED}{e}{Style.RESET_ALL}')


if __name__ == '__main__':
    run()

    # ret = repo_service.toc('nju_nova/manager', type='all')
    # print(ret)
    i = 0
    i += 1
    pass
