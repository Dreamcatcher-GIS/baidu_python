from distutils.core import setup
import sys

import baidumap

kw = dict(
    name = 'baidumap',
    version = baidumap.__version__,
    description = 'BaiduMap API Python SDK',
    author = 'DreamCatcher',
    author_email = 'kp_clown@126.com',
    url = 'https://github.com/Dreamcatcher-GIS/baidumap_python',
    download_url = 'https://github.com/Dreamcatcher-GIS/baidumap_python',
    py_modules = ['baidumap'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])

setup(**kw)
