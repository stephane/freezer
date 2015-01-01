# -*- coding: utf-8 -*-
import os

from setuptools import setup

__version__ = '0.1'

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='freezer',
    version=__version__,
    description='Static blog generator based on Frozen Flask',
    long_description=README,
    author=u"Stéphane Raimbault",
    author_email='stephane.raimbault@gmail.com',
    url="http://github.com/stephane/freezer",
    keywords="static blog generator flask frozen",
    packages=['freezer'],
    package_data={'': ['LICENSE']},
    include_package_data=True,
    license='BSD License',
    zip_safe=False,
    install_requires=[
        'Flask>=0.10.1',
        'Flask-Script',
        'Frozen-Flask>=0.11',
        'Markdown>=2.5',
        'PyYAML',
        'Pygments>=1.6',
    ],
    classifiers=(
        'Environment :: Web Environment',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
