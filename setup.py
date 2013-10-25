import os
import sys

from os.path import join as pjoin

from setuptools import setup


def read_version_string():
    version = None
    sys.path.insert(0, pjoin(os.getcwd()))
    from django_visitor_information import __version__
    version = __version__
    sys.path.pop(0)
    return version

with open('requirements.txt', 'r') as fp:
    content = fp.read().strip()
    requirements = content.split('\n')


setup(
    name='django-visitor-information-middleware',
    version=read_version_string(),
    long_description=open('README.rst').read() + '\n\n' +
    open('CHANGES.rst').read(),
    packages=[
        'django_visitor_information'
    ],
    package_dir={
        'django_visitor_information': 'django_visitor_information'
    },
    package_data={
        'django_visitor_information': ['static/*.dat']
    },
    install_requires=requirements,
    url='https://github.com/Kami/django-visitor-information-middleware/',
    license='Apache License (2.0)',
    author='Tomaz Muraus',
    author_email='tomaz+pypi@tomaz.me',
    description='A collection of Django middleware classes which make '
                'writing timezone and location aware applications easier',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
