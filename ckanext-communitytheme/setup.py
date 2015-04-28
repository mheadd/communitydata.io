#!/usr/bin/env/python
from setuptools import setup

setup(
    name='ckanext-communitytheme',
    version='0.1',
    description='',
    license='AGPL3',
    author='',
    author_email='',
    url='',
    namespace_packages=['ckanext'],
    packages=['ckanext.communitytheme'],
    zip_safe=False,
    entry_points = """
        [ckan.plugins]
        community_theme = ckanext.communitytheme.plugins:CustomTheme
    """
)
