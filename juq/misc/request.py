# -*- coding: utf-8 -*-
# created by inhzus

import json
from pprint import pprint

import requests

from juq.config import config
from juq.misc.exceptions import STATUS_EXCEPTION_MAP
from juq.serializer import SerializerBuilder


class Request:

    @staticmethod
    def wrap_uri(uri):
        """Wrap original url with API_BASE_URL"""
        return config.API_BASE_URL + uri

    @staticmethod
    def send(method, uri, data=None, anonymous=False):
        headers = {
            'User-Agent': config['API_APP_NAME']
        }
        if not anonymous or 'TOKEN' in config:
            headers['X-Auth-Token'] = config['TOKEN']
        if method != 'GET':
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
        response = requests.request(method=method, url=Request.wrap_uri(uri), headers=headers, data=data,
                                    timeout=config['TIMEOUT'])
        d = json.loads(response.text)
        if response.status_code in STATUS_EXCEPTION_MAP:
            message = d['message']
            raise STATUS_EXCEPTION_MAP[response.status_code](f"{method} {uri}: {message}")
        if config['SERIALIZE']:
            return SerializerBuilder.build(d)
        else:
            return d


if __name__ == '__main__':
    pprint(Request.send('GET', '/user/docs'))
