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
    name="message_insights",
    version="0.3.1",
    url="https://github.com/chaoss/augur",
    license='MIT',
    author="Augur Team",
    author_email="akshblr555@gmail.com",
    description="Message Insights worker that detects novel messages & analyzes sentiment from issue, PR messages",
    packages=find_packages(),
    install_requires=[
        'Flask==2.3.2',
        'Flask-Cors==3.0.10',
        'Flask-Login==0.6.2',
        'Flask-WTF==1.0.0',
        'requests==2.28.2',
        'psycopg2-binary==2.9.6',
        "click <=9.0, >=8.1.3", # 8.1.3
        'scipy>=1.10.1',
        'scikit-learn==1.1.3', #0.24.2',
        'numpy==1.24.2',
        'nltk==3.6.6',
        'pandas==1.5.3',
        'emoji==1.2.0',
        'Keras<2.14, >=2.13.1rc0',
        'Keras-Preprocessing==1.1.2',
        'tensorflow>=2.13.0rc1',
        "h5py~=3.8.0", # 3.7
        'scikit-image==0.19.1',
        'joblib==1.0.1',
        'xgboost==1.7.5',
        'bs4==0.0.1',
        'xlrd==2.0.1',
        'gensim~=4.3.1'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ]
)
