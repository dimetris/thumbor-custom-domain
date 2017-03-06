#!/usr/bin/python
# -*- coding: utf-8 -*-
from tornado.concurrent import return_future
from thumbor.loaders.http_loader import _normalize_url, load_sync


@return_future
def load(context, url, callback, normalize_url_func=_normalize_url):
    if not any([True for schema in ('http://', 'https://') if schema in url]):
        url = context.config.LOADER_CUSTOM_DOMAIN + url
    load_sync(context, url, callback, normalize_url_func)