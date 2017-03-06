#!/usr/bin/python
# -*- coding: utf-8 -*-


@return_future
def load(context, url, callback, normalize_url_func=_normalize_url):
    if not any([True for schema in ('http://', 'https://') if schema in url]):
        url = context.config.LOADER_CUSTOM_DOMAIN + url
    load_sync(context, url, callback, normalize_url_func)