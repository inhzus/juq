# -*- coding: utf-8 -*-
# created by inhzus

import argparse

from colorama import Fore, Style, init

# noinspection PyUnresolvedReferences
from juq.service import user_service, group_service, repo_service, doc_service, config_service

init(convert=True)


def set_user_parser(user_parser: argparse.ArgumentParser):
    _parser = user_parser.add_subparsers(dest='user', help='identifier: login/id')
    _parser.required = True

    info = _parser.add_parser('info', help='get user detailed info')
    info.add_argument('id_', help='user login or id, self by default', nargs='?',
                      default='', type=str, metavar='id')

    docs = _parser.add_parser('docs')
    docs.add_argument('-q', help='Search keywords', default='', type=str)
    docs.add_argument('--offset', '-o', help='page offset', default=0, type=int)

    groups = _parser.add_parser('groups')
    groups.add_argument('id_', help='user login or id, self by default',
                        nargs='?', default='', type=str, metavar='id')

    repos = _parser.add_parser('repos')
    repos.add_argument('id_', help='user login or id, self by default',
                       nargs='?', default='', type=str, metavar='id')
    repos.add_argument('--type', '-t', choices=['Book', 'Design', 'all'], type=str,
                       help='[Book|Design|all], all by default', default='all')
    repos.add_argument('--offset', '-o', help='page offset', default=0, type=int)

    recent = _parser.add_parser('recent', help='get user recent updated')
    recent.add_argument('--type', '-t', choices=['Book', 'Doc'], help='[Book|Doc], Book by default',
                        type=str, default='Book')
    recent.add_argument('--offset', '-o', help='page offset', default=0, type=int)


def set_group_parser(group_parser: argparse.ArgumentParser):
    _parser = group_parser.add_subparsers(dest='group', help='identifier: login/id')
    _parser.required = True

    info = _parser.add_parser('info', help='get group detailed info')
    info.add_argument('id_', help='group login or id', default='', type=str, metavar='group_id')

    repos = _parser.add_parser('repos', help='get group repos')
    repos.add_argument('group_id', help='group login or id', type=str)
    repos.add_argument('--type', '-t', choices=['Book', 'Design', 'all'], default='all', type=str)
    repos.add_argument('--offset', '-o', help='page offset', default=0, type=int)


def set_repo_parser(repo_parser: argparse.ArgumentParser):
    _parser = repo_parser.add_subparsers(dest='repo', help='identifier: [user_id]/[slug] or repo_id')
    _parser.required = True

    info = _parser.add_parser('info', help='get repo detailed info')
    info.add_argument('id_', help='[user_id|group_id]/repo_slug or repo_id',
                      type=str, metavar='repo_id')
    info.add_argument('--type', '-t', choices=['Book', 'Design'], type=str,
                      help='[Book|Design], Book by default', default='Book')

    toc = _parser.add_parser('toc', help='get repo toc(table of content)')
    toc.add_argument('id_', help='[user_id|group_id]/repo_slug or repo_id',
                     type=str, metavar='repo_id')

    docs = _parser.add_parser('docs', help='get repo docs')
    docs.add_argument('repo_id', help='[user_id|group_id]/repo_slug or repo_id', type=str)

    search = _parser.add_parser('search', help='search repos by keywords and type')
    search.add_argument('q', help='keywords', type=str)
    search.add_argument('--type', '-t', choices=['Book', 'Design'], type=str,
                        help='[Book|Design]', default='Book')

    create = _parser.add_parser('create', help='create a new repo')
    create.add_argument('slug', help='repo identifier', type=str)
    create.add_argument('name', help='repo name', type=str)
    create.add_argument('--group_id', '-g', help='group id to create a group repo',
                        default='', type=str)
    create.add_argument('--public', '-p', choices=[0, 1, 2], type=int,
                        help='0: private, 1: public to yuque users, 2: public to all',
                        default=0)
    create.add_argument('--description', '-d', help='repo description', default='', type=str)

    update = _parser.add_parser('update', help='update repo info')
    update.add_argument('id_', help='[user_id|group_id]/repo_slug or repo_id', type=str, metavar='id')
    update.add_argument('--slug', '-s', help='repo identifier', type=str, default='')
    update.add_argument('--name', '-n', help='repo name', type=str, default='')
    update.add_argument('--public', '-p', choices=[0, 1, 2], type=int,
                        help='0: private, 1: public to yuque users, 2: public to all',
                        default=None)
    update.add_argument('--description', '-d', help='repo description', default='', type=str)

    delete = _parser.add_parser('delete', help='delete repo')
    delete.add_argument('id_', help='[user_id|group_id]/repo_slug or repo_id', type=str, metavar='id')


def set_doc_parser(doc_parser: argparse.ArgumentParser):
    _parser = doc_parser.add_subparsers(dest='doc', help='DO NOT USE DOC SLUG AS IDENTIFIER WHICH MAY CAUSE ERROR')
    _parser.required = True

    info = _parser.add_parser('info', help='get doc detailed info')
    info.add_argument('repo_id', help='[user_id|group_id]/repo_slug or repo_id', type=str)
    info.add_argument('id_', help='Doc id', type=str, metavar='doc_id')

    toc = _parser.add_parser('toc', help='change the position of doc in the repo toc, append to end by default.')
    toc.add_argument('repo_id', help='[user_id|group_id]/repo_slug or repo_id', type=str)
    toc.add_argument('id_', help='doc id', type=str, metavar='doc_id')
    pos = toc.add_mutually_exclusive_group(required=False)
    pos.add_argument('--before', '-b', help='doc id to insert before', default='', type=str)
    pos.add_argument('--after', '-a', help='doc id to insert after', default='', type=str)
    toc.add_argument('--depth', '-d', help='doc toc depth', default=0, type=int)

    create = _parser.add_parser('create', help='post a local markdown file to some repo.')
    create.add_argument('repo_id', help='[user_id|group_id]/repo_slug or repo_id', type=str)
    create.add_argument('file', help='markdown file location', type=str)
    create.add_argument('--slug', '-s', help='unique identifier', default='', type=str)
    create.add_argument('--title', '-t', help='doc title', default='', type=str)
    create.add_argument('--public', '-p', help='doc privilege, private by default.',
                        action='store_const', const=1, default=0)

    update = _parser.add_parser('update', help='update some remote doc')
    update.add_argument('repo_id', help='[user_id|group_id]/repo_slug or repo_id', type=str)
    update.add_argument('id_', help='remote doc id', type=str, metavar='id')
    update.add_argument('file', help='markdown file location', type=str)
    update.add_argument('--slug', '-s', help='unique identifier', default='', type=str)
    update.add_argument('--title', '-t', help='doc title', default='', type=str)
    update.add_argument('--public', '-p', help='doc privilege, private by default.',
                        action='store_const', const=1, default=0)

    delete = _parser.add_parser('delete')
    delete.add_argument('repo_id', help='[user_id|group_id]/repo_slug or repo_id', type=str)
    delete.add_argument('id_', help='doc id', type=str, metavar='id')


def set_config_parser(config_parser: argparse.ArgumentParser):
    _parser = config_parser.add_subparsers(dest='config')

    set_ = _parser.add_parser('set', help='set configuration value')
    set_.add_argument('key', help='configuration key',
                      choices=['API_BASE_URL', 'API_APP_NAME', 'TIME_OUT', 'TOKEN'], type=str)
    set_.add_argument('value', help='configuration value', type=str)

    get = _parser.add_parser('get', help='get configuration value')
    get.add_argument('key', help='configuration key',
                     choices=['API_BASE_URL', 'API_APP_NAME', 'TIME_OUT', 'TOKEN'], type=str)

    _parser.add_parser('reset', help='RESET all configuration')


parser = argparse.ArgumentParser()
sub_parser = parser.add_subparsers(dest='sub')
sub_parser.required = True

set_user_parser(sub_parser.add_parser('user', help='user info, recent, groups, docs, repos'))
set_group_parser(sub_parser.add_parser('group', help='group info, repos'))
set_repo_parser(sub_parser.add_parser('repo', help='repo info, docs, toc, search'))
set_doc_parser(sub_parser.add_parser('doc', help='doc info, toc, create'))
set_config_parser(sub_parser.add_parser('config', help='config get, set, reset'))


def run():
    # args = parser.parse_args(''.split())
    args = parser.parse_args()
    # noinspection PyBroadException
    try:
        print(getattr(
            globals()[f'{args.sub}_service'],
            getattr(args, args.sub))
              (**vars(args)))
    except Exception as e:
        print(f'{e.__class__.__name__}: {Fore.RED}{e}{Style.RESET_ALL}')


if __name__ == '__main__':
    run()
