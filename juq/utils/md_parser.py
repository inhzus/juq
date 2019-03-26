# -*- coding: utf-8 -*-
# created by inhzus

import codecs
import os
import re
from urllib.parse import urlparse

from juq.utils import ImageHost


class MarkdownParser:
    """Parse markdown content and transform it to be ready to upload to Yuque Knowledge Base"""
    def __init__(self, filename):
        self.filename = filename
        self.content = codecs.open(self.filename, 'r', encoding='utf-8').read()

    @staticmethod
    def is_url(path: str):
        """Check if image path is already a url"""
        return urlparse(path).scheme in ('http', 'https',)

    def generate_image_url(self, image_rel_path):
        """Upload local image and return http(s) image url

        Args:
            image_rel_path: image relative path displayed in markdown content

        Returns: image url
        """
        if self.is_url(image_rel_path):
            return image_rel_path
        dir_ = os.path.dirname(self.filename)
        image_abs_path = os.path.join(dir_, image_rel_path)
        return ImageHost.upload(image_abs_path)

    def parse_image(self):
        """Upload local image to image hosting service, and replace local image path location"""
        self.content = re.sub(  # Match the regex below
            r'!'  # markdown image identifier
            r'\[(.*?)\]'  # image name as first variable
            r'\((.*)\)',  # image url/path as second variable

            lambda m: '![{name}]({uri})'.format(
                name=m.group(1),
                uri=self.generate_image_url(m.group(2))),
            self.content,
            re.X
        )

    def remove_hexo_header(self):
        self.content = re.sub(
            r'^-{3,}\n'  # first line of hexo header
            r'[\s\S]*\n'  # every thing inside
            r'-{3,}\n',  # last line of hexo header
            '',
            self.content,
            re.X
        )
        # self.content = re.sub(
        #     r'-*.'
        # )

    def run(self):
        self.remove_hexo_header()
        self.parse_image()

    def __repr__(self):
        return self.content


def parse_md(filename: str):
    parser = MarkdownParser(filename)
    parser.run()
    return parser.content


if __name__ == '__main__':
    markdown_filename = '../../test/assets/2019-03-20-octree-color-quantization.md'
    content = codecs.open(markdown_filename, 'r', encoding='utf-8').read()
    print(re.findall(r'^-{3,}\n[\s\S]*\n-{3,}\n', content))
    # print(parse_md(markdown_filename))
    # print(parser.generate_image_url(None))
    # print(parser.parse_image())
    pass
