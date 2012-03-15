#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
urllib3-bug.py
~~~~~~~~~~~~~~

This module shows some odd behavior from urllib3's PoolManager.
"""

from urllib3.poolmanager import PoolManager

import logging
logging.basicConfig(level=logging.INFO)

url = 'http://httpbin.org:80/get'

pool = PoolManager(num_pools=10, maxsize=1, block=False)

for i in range(14):
    # c = pool.connection_from_url(url + '/' + str(i))
    # print pool.__dict__
    # print pool.pools.__dict__
    pool.urlopen('GET', url)
    print '.'