Freezer
=======

Static blog generator based on Flask and Frozen Flask.

You can run your web site with Flask to theme it (or add new features) and
freeze it when it is ready for deployment. Once the your web site is frozen,
you can deploy it as static content with a single nginx.

This small project is based on code from https://github.com/SimonSapin/exyr.org
See http://exyr.org/2010/Flask-Static/ for details. Simon Sapin is the author of
awesome Frozen-Flask.

I wanted to set up my own blog from Simon's code so I think others want to do the same.
That's why I rewrote Exyr to extract its nice skeleton in this app called 'freezer'.

I really want to keep this code very simple and basic so I recommend you to fork
the project and make your changes in a branch (style, layout, features, etc).

Install
-------

To install it in a virtualenv, run:

    pip install -e .

Launch app for dev
------------------

Copy `freezer/config.py.sample` to `freezer/config.py` and launch the Web app with:

    ./manage run

Create a post
-------------

To create a post of blog for 2015, you first need to create a directory for the
year:

    mkdir freezer/articles/2015

Then in this new directory, you can create a file for each post of blog (see the
examples provided).

It's also possible to create a page outside of the chronology by putting the
article at the root of the articles directory.

    vi freezer/articles/about.md

Build Web site
--------------

To build the static blog:

    ./manage freeze
