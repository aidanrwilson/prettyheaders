#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
╭─────────────────────────────────────────────╮
│ ╔═╗┬─┐┌─┐┌┬┐┌┬┐┬ ┬  ╦ ╦┌─┐┌─┐┌┬┐┌─┐┬─┐┌─┐ ┬ │
│ ╠═╝├┬┘├┤  │  │ └┬┘  ╠═╣├┤ ├─┤ ││├┤ ├┬┘└─┐ │ │
│ ╩  ┴└─└─┘ ┴  ┴  ┴   ╩ ╩└─┘┴ ┴─┴┘└─┘┴└─└─┘ o │
╰─────────────────────────────────────────────╯

This setup script can be used the following ways w/python3:
* `python3 setup.py install`
* `python3 setup.py install --user`
* `python3 setup.py develop`
* `python3 setup.py develop --user`
* `python3 setup.py test`
'''

from setuptools import setup
setup(
    name='prettyheaders',
    version='0.0.1',
    author='Aidan Wilson',
    author_email='aidanrwilson@gmail.com',
    test_suite='tests',
    packages=['prettyheaders'],
    install_requires=[
        'numpy',  # For quick string to formatted header generation
    ],
    description='Prettified Headers',
    long_description=__doc__
)
