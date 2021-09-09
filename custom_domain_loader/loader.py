#!/usr/bin/python
# -*- coding: utf-8 -*-
from tornado.concurrent import return_future
from thumbor.loaders.http_loader import _normalize_url, load_sync
from tornado.httpclient import AsyncHTTPClient

AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient", max_clients=100)


@return_future
def load(context, url, callback, normalize_url_func=_normalize_url):
    if not any([True for schema in ('http%3A//', 'https%3A//') if schema in url]):
        url = context.config.LOADER_CUSTOM_DOMAIN + url
    load_sync(context, url, callback, normalize_url_func)