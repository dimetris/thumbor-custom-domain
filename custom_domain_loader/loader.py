#!/usr/bin/python
# -*- coding: utf-8 -*-
from thumbor.loaders.http_loader import _normalize_url, return_contents, encode
from thumbor.loaders.http_loader import load as load_fn


async def load(
    context,
    url,
    normalize_url_func=_normalize_url,
    return_contents_fn=return_contents,
    encode_fn=encode,
):
    if not any([True for schema in ('http%3A//', 'https%3A//') if schema in url]):
        url = context.config.LOADER_CUSTOM_DOMAIN + url
    return load_fn(context, url, normalize_url_func, return_contents_fn, encode_fn)