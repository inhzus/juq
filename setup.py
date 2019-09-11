# -*- coding: utf-8 -*-
# created by inhzus

import setuptools
import codecs

with codecs.open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='juq',
    version='1.4.1',
    author='Zhi Sun',
    author_email='inhzus@gmail.com',
    description='Yuque SDK and command line tool.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/inhzus/juq',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    entry_points={
        'console_scripts': ['juq=juq.caller:run']
    },
    install_requires=[
        'colorama>=0.4.1',
        'PyYAML>=5.1',
        'requests>=2.21.0'
    ]
)
