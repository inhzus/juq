# -*- coding: utf-8 -*-
# created by inhzus

import requests
import json


class UploadException(Exception):
    pass


class ImageHost:
    url = 'https://sm.ms/api/upload'
    method = 'POST'

    @staticmethod
    def upload(filename: str):
        response = requests.request(method=ImageHost.method, url=ImageHost.url, files={
            'smfile': open(filename, 'rb')
        })
        ret = json.loads(response.text)
        if ret['code'] == 'error':
            raise UploadException(ret['msg'])
        return ret['data']['url']


if __name__ == '__main__':
    # print(requests.get('https://sm.ms/api/list').text)
    print(ImageHost.upload('./h.jpg'))
