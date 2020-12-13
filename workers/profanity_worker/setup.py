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
    name="profanity_worker",
    version="0.0.0",
    url="https://github.com/YoungBrendanM/augur-eagles",
    license='MIT',
    author="Eagles",
    author_email="awjkcc@umsystem.edu",
    description="Augur worker to be used to find profanity",
    packages=find_packages(),
    install_requires=[
        'flask',
        'requests',
        'psycopg2-binary'
        'click'
    ],
    entry_points={
        'console_scripts': [
            'profanity_worker_start=workers.profanity_worker.runtime:main',
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
