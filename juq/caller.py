# -*- coding: utf-8 -*-
# created by inhzus

from typing import Callable
import argparse
from juq.misc.exceptions import RequestException, EXCEPTION_MESSAGE_MAP


class Caller:
    @staticmethod
    def call(func: Callable, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except RequestException as e:
            print(EXCEPTION_MESSAGE_MAP[e.__class__])
            exit(1)


def p(id_):
    print(f'what does {id_} says')


def set_user_parser(user_parser_: argparse.ArgumentParser):
    user_sub_parser = user_parser_.add_subparsers(dest='user')
    user_sub_parser.required = True

    user_info = user_sub_parser.add_parser('info')
    user_info.set_defaults(func=p)
    user_info.add_argument('id', help='Login or id', nargs='?', default='', type=str)

    user_sub_parser.add_parser('docs')
    user_sub_parser.add_parser('groups')
    user_sub_parser.add_parser('repos')

    user_recent = user_sub_parser.add_parser('recent')
    user_recent.add_argument('type', help='Book or Doc', nargs='?', type=str, default='Book')


def set_group_parser(group_parser_: argparse.ArgumentParser):
    group_sub_parser = group_parser_.add_subparsers(dest='group')
    group_sub_parser.required = True

    group_info = group_sub_parser.add_parser('info')
    group_info.add_argument('id', help='Login or id', nargs='?', const='', type=str)

    group_sub_parser.add_parser('repos')


def set_repo_parser(repo_parser_: argparse.ArgumentParser):
    repo_sub_parser = repo_parser_.add_subparsers(dest='repo')
    repo_sub_parser.required = True

    repo_info = repo_sub_parser.add_parser('info')
    repo_info.add_argument('id', help='[user|group]/repo_slug', type=str)

    repo_toc = repo_sub_parser.add_parser('toc')
    repo_toc.add_argument('toc', help='[user|group]/repo_slug', type=str)

    repo_search = repo_sub_parser.add_parser('search')
    repo_search.add_argument('key', help='Search keywords', type=str)
    repo_search.add_argument('type', help='[Book|Design]', nargs='?', const='', type=str)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers(dest='sub')
    sub_parser.required = True

    user_parser = sub_parser.add_parser('user', help='User operations')
    group_parser = sub_parser.add_parser('group', help='Group operations')
    repo_parser = sub_parser.add_parser('repo', help='Repo operations')
    set_user_parser(user_parser)
    set_group_parser(group_parser)
    set_repo_parser(repo_parser)
    res = parser.parse_args('user recent'.split())
    print(res.__dict__)
    pass
