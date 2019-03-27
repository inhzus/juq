# -*- coding: utf-8 -*-
# created by inhzus

import re

from colorama import Fore, Style

from juq.serializer import DocDetailSerializer


def filter_empty_params(params: dict):
    params.pop('_')
    return {k: v for k, v in params.items() if v or isinstance(v, int)}


def toc_line_repr(line: dict):
    return f'{Fore.RED}|-' * line['depth'] + \
           f'{Style.RESET_ALL}' \
           f'id: {Fore.BLUE}{line["id"]}{Style.RESET_ALL}\t' \
           f'slug: {Fore.BLUE}{line["slug"]}{Style.RESET_ALL}\t' \
           f'title: {Fore.BLUE}{line["title"]}{Style.RESET_ALL}'


def toc_repr(toc_: list):
    if not toc_:
        return ''
    return '\n'.join(map(toc_line_repr, toc_))


# e.g. '  - [标题](slug "12312")'
# '  ', '标题', 'slug', '12312'
pattern = re.compile(r'^(?P<depth>\s*?)'  # get depth on blank numbers
                     r'-\s'
                     r'\[(?P<title>.*)\]'  # title between square brackets
                     r'\((?P<slug>\S*)'  # slug after left bracket
                     r'\s'
                     r'"(?P<id>\d*)"\)',  # id before right bracket
                     re.X)


def load_toc_line(line: str):
    matches = pattern.match(line)
    return {'depth': int(len(matches['depth']) / 2), 'title': matches['title'],
            'slug': matches['slug'], 'id': matches['id']}


def load_toc(toc_: str):
    # for line in toc_.split('\n'):
    #     yield load_toc_line(line)
    if not toc_:
        return []
    return list(map(load_toc_line, toc_.split('\n')))


def dump_toc_line(line: dict):
    return '  ' * line['depth'] + \
           f'- [{line["title"]}]' \
           f'({line["slug"]} \"{line["id"]}\")'


def dump_toc(toc_list):
    return '\n'.join(map(dump_toc_line, toc_list))


def change_doc_toc(toc: str, insert: DocDetailSerializer, before: str, after: str, depth: int = 0):

    if before:
        after = before
    if toc:
        src_toc = load_toc(toc if toc else '')
    else:
        src_toc = []
    toc_list = [line for line in src_toc if line['id'] != str(insert.id)]
    insert_toc = {'depth': depth, 'title': insert.title, 'slug': insert.slug, 'id': insert.id}
    if not before and not after:
        toc_list.append(insert_toc)
        return toc_list
    # Find the pos to insert after/before
    for i, line in enumerate(toc_list):
        if line['id'] == after:
            idx = i if before else i + 1
            break
    else:
        return src_toc
    toc_list.insert(idx, insert_toc)
    return toc_list
