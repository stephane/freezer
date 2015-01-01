# -*- coding: utf-8 -*-

import io
import itertools
import os

from flask import abort, url_for
import markdown as markdown_module
import yaml
import werkzeug

from .app import app

@app.template_filter()
def markdown(text):
    return markdown_module.markdown(
        text, extensions=['codehilite(guess_lang=False)'])


class Article(object):
    root = os.path.join(app.root_path, u"articles")
    suffix = '.md'
    _cache = {}

    @classmethod
    def load(cls, year, name):
        filename = os.path.join(cls.root, year, name) + cls.suffix
        if not os.path.isfile(filename):
            abort(404)

        # Compare file modication time to cache of this file
        mtime = os.path.getmtime(filename)
        article, old_mtime = cls._cache.get(filename, (None, None))
        if not article or mtime != old_mtime:
            with io.open(filename, encoding='utf8') as fd:
                head = ''.join(itertools.takewhile(lambda s: s.strip(), fd))
                body = fd.read()
            article = cls(year, name, head, body)
            cls._cache[filename] = (article, mtime)
        return article

    @classmethod
    def get_years(cls):
        for year in os.listdir(cls.root):
            if year.isdigit():
                yield year

    @classmethod
    def get_posts(cls, year=None):
        """An article with a year is a post indeed"""
        years = cls.get_years() if not year else [year]

        for year in years:
            directory = os.path.join(cls.root, year)
            if not os.path.isdir(directory):
                abort(404)

            for name in os.listdir(directory):
                if name.endswith(cls.suffix):
                    yield cls.load(year, name[:-len(cls.suffix)])

    def __init__(self, year, name, head, body):
        self.year = year
        self.name = name
        self.head = head
        self.body = body

    def __str__(self):
        return "%s-%s" % (self.year, self.name)

    @werkzeug.cached_property
    def meta(self):
        return yaml.safe_load(self.head) or {}

    def __getitem__(self, name):
        return self.meta[name]

    @werkzeug.cached_property
    def html(self):
        return markdown(self.body)

    def url(self, **kwargs):
        return url_for('article', year=int(self.year), name=self.name, **kwargs)
