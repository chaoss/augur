#SPDX-License-Identifier: MIT
import io
import os
import re

from setuptools import find_packages
from setuptools import setup

def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())

setup(
    name="contributor_breadth_worker",
    version="0.0.0",
    url="https://github.com/chaoss/augur",
    license='MIT',
    author="AugurLabs",
    author_email="gabe@gabehe.im",
    description="Augur worker that collects the repos people have contirbuted to",
    packages=find_packages(),
    install_requires=[
        'Flask==2.3.2',
        'Flask-Cors==3.0.10',
        'Flask-Login==0.6.2',
        'Flask-WTF==1.0.0',
        'requests==2.28.2',
        'psycopg2-binary==2.9.6'
    ],
    entry_points={
        'console_scripts': [
            'contributor_breadth_worker_start=workers.contributor_breadth_worker.runtime:main',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ]
)
