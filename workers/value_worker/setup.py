#SPDX-License-Identifier: MIT
import io
import os
import re

from setuptools import find_packages
from setuptools import setup

setup(
    name="value_worker",
    version="1.0.0",
    url="https://github.com/chaoss/augur",
    license='MIT',
    author="Augurlabs",
    author_email="s@goggins.com",
    description="Augur Worker that gathers value data",
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'flask',
        'requests',
        'psycopg2-binary',
    ],
    entry_points={
        'console_scripts': [
            'value_worker_start=workers.value_worker.runtime:main',
        ],
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
