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
    name="discourse_analysis_worker",
    version="0.0.0",
    url="https://github.com/chaoss/augur",
    license='MIT',
    author="Augur Team",
    author_email="",
    description="Worker to classify messages into discourse acts",
    packages=find_packages(),
    install_requires=[
        'Flask==1.1.4',
        'Flask-Cors==3.0.10',
        'Flask-Login==0.5.0',
        'Flask-WTF==0.14.3',
        'requests==2.22.0',
        'psycopg2-binary==2.8.6',
        'click==7.1.2', 
        'scipy==1.6.3',
        'nltk==3.5',
        'pandas==1.1.3',
        'scikit-learn==0.24.1',
        'textblob==0.15.3',
        'sklearn-crfsuite==0.3.6'
    ],
    entry_points={
        'console_scripts': [
            'discourse_analysis_worker_start=workers.discourse_analysis_worker.runtime:main',
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
