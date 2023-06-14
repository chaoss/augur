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
    version="0.1.0",
    url="https://github.com/chaoss/augur",
    license='MIT',
    author="Augur Team",
    author_email="s@goggins.com",
    description="Worker to classify messages into discourse acts",
    packages=find_packages(),
    install_requires=[
        'Flask==2.3.2',
        'Flask-Cors==3.0.10',
        'Flask-Login==0.6.2',
        'Flask-WTF==1.0.0',
        'requests==2.28.2',
        'psycopg2-binary==2.9.6',
        "click <=9.0, >=8.1.3", # 8.1.3
        'scipy==1.10.1',
        'nltk==3.6.6',
        'pandas==1.5.3',
        'scikit-learn==1.1.3',
        'textblob==0.15.3', 
        'python-crfsuite==0.9.9',
        'sklearn-crfsuite==0.3.6',
        'tabulate==0.8.9'
    ], # python-crfsuite-0.9.8 sklearn-crfsuite-0.3.6 tabulate-0.8.9
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
