Last login: Thu Apr 21 09:42:23 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) mu-581988:~ dmiller$ cd augur
(base) mu-581988:augur dmiller$ ls
CODE_OF_CONDUCT.md	augur_service.sh	readthedocs.yml
CONTRIBUTING.md		augurface		repos
LICENSE			conftest.py		runtime
MANIFEST.in		database-compose.yml	schema
Makefile		docker-compose.yml	scripts
README.md		docker-setup.sh		setup.py
SECURITY.md		docs			ssl
Vagrantfile		frontend		tests
augur			frontend-compose.yml	tox.ini
augur.config.json	lib-0.16.1.md		util
augur.egg-info		log_analysis		workers
augur_service.md	metadata.py
(base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.0.1

Configuration error:
There is a programmable error in your configuration file:

Traceback (most recent call last):
  File "/opt/anaconda3/lib/python3.8/site-packages/sphinx/config.py", line 323, in eval_config_file
    exec(code, namespace)
  File "/Users/dmiller/augur/docs/source/conf.py", line 22, in <module>
    import sphinx_rtd_theme
ModuleNotFoundError: No module named 'sphinx_rtd_theme'

make[1]: *** [html] Error 2
make: *** [docs] Error 2
(base) mu-581988:augur dmiller$ cd doc
-bash: cd: doc: No such file or directory
(base) mu-581988:augur dmiller$ cd docs
(base) mu-581988:docs dmiller$ ls
Makefile			pull_request_template.md
augur.0.21.0.release-notes.md	source
fedora-install.md
(base) mu-581988:docs dmiller$ make docs-view
Running Sphinx v4.0.1

Configuration error:
There is a programmable error in your configuration file:

Traceback (most recent call last):
  File "/opt/anaconda3/lib/python3.8/site-packages/sphinx/config.py", line 323, in eval_config_file
    exec(code, namespace)
  File "/Users/dmiller/augur/docs/source/conf.py", line 22, in <module>
    import sphinx_rtd_theme
ModuleNotFoundError: No module named 'sphinx_rtd_theme'

make: *** [docs-view] Error 2
(base) mu-581988:docs dmiller$ ls
Makefile			pull_request_template.md
augur.0.21.0.release-notes.md	source
fedora-install.md
(base) mu-581988:docs dmiller$ python3 -m venv $HOME/.virtualenvs/augur_env
(base) mu-581988:docs dmiller$ source $HOME/.virtualenvs/augur_env/bin/activate
(augur_env) (base) mu-581988:docs dmiller$ make docs-view
Running Sphinx v4.2.0

Sphinx error:
Builder name docs-view not registered or available through entry point
make: *** [docs-view] Error 2
(augur_env) (base) mu-581988:docs dmiller$ ls
Makefile			pull_request_template.md
augur.0.21.0.release-notes.md	source
fedora-install.md
(augur_env) (base) mu-581988:docs dmiller$ make docs
Running Sphinx v4.2.0

Sphinx error:
Builder name docs not registered or available through entry point
make: *** [docs] Error 2
(augur_env) (base) mu-581988:docs dmiller$ cd source/
(augur_env) (base) mu-581988:source dmiller$ ls
auggie			docker			schema
conf.py			index.rst		web-server-config
detailed-installation	quick-start.rst
development-guide	rest-api
(augur_env) (base) mu-581988:source dmiller$ make docs-view
make: *** No rule to make target `docs-view'.  Stop.
(augur_env) (base) mu-581988:source dmiller$ make docs
make: *** No rule to make target `docs'.  Stop.
(augur_env) (base) mu-581988:source dmiller$ ls
auggie			docker			schema
conf.py			index.rst		web-server-config
detailed-installation	quick-start.rst
development-guide	rest-api
(augur_env) (base) mu-581988:source dmiller$ cd ..
(augur_env) (base) mu-581988:docs dmiller$ cd ..
(augur_env) (base) mu-581988:augur dmiller$ ls
CODE_OF_CONDUCT.md	augur_service.sh	readthedocs.yml
CONTRIBUTING.md		augurface		repos
LICENSE			conftest.py		runtime
MANIFEST.in		database-compose.yml	schema
Makefile		docker-compose.yml	scripts
README.md		docker-setup.sh		setup.py
SECURITY.md		docs			ssl
Vagrantfile		frontend		tests
augur			frontend-compose.yml	tox.ini
augur.config.json	lib-0.16.1.md		util
augur.egg-info		log_analysis		workers
augur_service.md	metadata.py
(augur_env) (base) mu-581988:augur dmiller$ cd ..
(augur_env) (base) mu-581988:~ dmiller$ cd augur/
(augur_env) (base) mu-581988:augur dmiller$ make rebuild-dev
Cleaning up!
Removing Python caches...
resetting python libraries
find . -name /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/IPython/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/PIL/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/_pytest/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/_yaml/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/absl/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/alabaster/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/appnope/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/asttokens/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/astunparse/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/attr/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/attrs/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/babel/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/backcall/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/beaker/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/blinker/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/bokeh/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/boto3/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/botocore/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/bs4/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/cachetools/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/certifi/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/charset_normalizer/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/clang/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/click/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/cloudpickle/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/coloredlogs/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/dask/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/dateutil/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/distlib/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/distributed/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/docutils/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/emoji/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/executing/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/filelock/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/flask/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/flask_cors/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/flask_login/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/flask_wtf/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/flatbuffers/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/fontTools/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/fsspec/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/gast/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/gensim/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/google_auth_oauthlib/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/grpc/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/gunicorn/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/h5py/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/humanfriendly/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/idna/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/imageio/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/importlib_metadata/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/importlib_resources/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/iniconfig/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/ipdb/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/itsdangerous/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/jedi/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/jinja2/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/jmespath/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/joblib/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/jsonschema/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/keras/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/keras_preprocessing/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/kiwisolver/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/locket/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/markdown/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/markupsafe/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/matplotlib/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/matplotlib_inline/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/msgpack/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/networkx/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/nltk/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/numpy/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/oauthlib/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/opt_einsum/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/packaging/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pandas/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/parso/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/partd/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pasta/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pexpect/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pip/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pkg_resources/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/platformdirs/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pluggy/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/prompt_toolkit/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/psutil/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/psycopg2/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/ptyprocess/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pure_eval/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/py/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pyasn1/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pyasn1_modules/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pygments/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pyparsing/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pyrsistent/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pytest/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pytz/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/pywt/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/regex/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/requests/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/requests_oauthlib/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/rsa/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/s3transfer/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/scipy/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/seaborn/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/selenium/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/setuptools/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/skimage/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/sklearn/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/slack/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/smart_open/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/snowballstemmer/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/sortedcontainers/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/soupsieve/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/sphinx/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/sphinx_rtd_theme/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/sphinxcontrib/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/sqlalchemy/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/stack_data/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/tblib/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/tensorboard/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/tensorboard_data_server/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/tensorboard_plugin_wit/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/tensorflow/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/tensorflow_estimator/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/tensorflow_io_gcs_filesystem/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/textblob/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/tifffile/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/tlz/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/toml/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/toolz/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/tornado/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/tox/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/tqdm/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/traitlets/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/urllib3/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/virtualenv/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/wcwidth/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/werkzeug/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/wheel/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/wrapt/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/wtforms/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/xgboost/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/xlrd/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/xlsxwriter/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/yaml/__pycache__ /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/zict/__pycache__ -delete
find . -name /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/_pyrsistent_version.cpython-38.pyc /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/cycler.cpython-38.pyc /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/decorator.cpython-38.pyc /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/easy_install.cpython-38.pyc /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/heapdict.cpython-38.pyc /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/imagesize.cpython-38.pyc /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/m2r.cpython-38.pyc /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/mistune.cpython-38.pyc /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/pickleshare.cpython-38.pyc /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/pylab.cpython-38.pyc /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/six.cpython-38.pyc /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/termcolor.cpython-38.pyc /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/threadpoolctl.cpython-38.pyc /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/typing_extensions.cpython-38.pyc /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages/__pycache__/zipp.cpython-38.pyc -delete
Cleaning output files...
Removing build files...
Done cleaning!
Installing backend dependencies...
**********************************

Obtaining file:///Users/dmiller/augur
  Preparing metadata (setup.py) ... done
Requirement already satisfied: wheel in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (0.37.1)
Requirement already satisfied: coloredlogs==15.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (15.0)
Requirement already satisfied: Beaker==1.11.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (1.11.0)
Requirement already satisfied: SQLAlchemy==1.3.23 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (1.3.23)
Requirement already satisfied: itsdangerous==2.0.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (2.0.1)
Requirement already satisfied: Jinja2==3.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (3.0.2)
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (1.0.0)
Requirement already satisfied: pandas==1.3.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (1.3.5)
Requirement already satisfied: numpy==1.21 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (1.21.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (2.9.3)
Requirement already satisfied: click==8.0.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (8.0.3)
Requirement already satisfied: psutil==5.8.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (5.8.0)
Requirement already satisfied: gunicorn==20.1.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (20.1.0)
Requirement already satisfied: six==1.15.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (1.15.0)
Requirement already satisfied: bokeh==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (2.0.2)
Requirement already satisfied: selenium==3.141.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (3.141.0)
Requirement already satisfied: dask>=2021.6.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (2022.4.0)
Requirement already satisfied: cloudpickle>=0.2.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (2.0.0)
Requirement already satisfied: fsspec>=0.6.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (2022.3.0)
Requirement already satisfied: toolz>=0.8.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (0.11.2)
Requirement already satisfied: partd>=0.3.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (1.2.0)
Requirement already satisfied: distributed>=2021.03.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (2022.4.0)
Requirement already satisfied: nltk==3.6.6 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (3.6.6)
Requirement already satisfied: h5py~=3.6.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (3.6.0)
Requirement already satisfied: scipy==1.7.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (1.7.3)
Requirement already satisfied: blinker==1.4 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (1.4)
Requirement already satisfied: protobuf>3.6.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (3.20.0)
Requirement already satisfied: slack==0.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (0.0.2)
Requirement already satisfied: boto3==1.17.57 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (1.17.57)
Requirement already satisfied: toml in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (0.10.2)
Requirement already satisfied: mistune==0.8.4 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (0.8.4)
Requirement already satisfied: pyYaml in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (6.0)
Requirement already satisfied: tox==3.24.4 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (3.24.4)
Requirement already satisfied: pytest==6.2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (6.2.5)
Requirement already satisfied: ipdb==0.13.9 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (0.13.9)
Requirement already satisfied: sphinx==4.2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (4.2.0)
Requirement already satisfied: sphinx_rtd_theme==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (1.0.0)
Requirement already satisfied: sphinxcontrib-openapi==0.7.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (0.7.0)
Requirement already satisfied: sphinxcontrib-redoc==1.6.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (1.6.0)
Requirement already satisfied: docutils==0.17.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from augur==0.25.18) (0.17.1)
Requirement already satisfied: python-dateutil>=2.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from bokeh==2.0.2->augur==0.25.18) (2.8.2)
Requirement already satisfied: pillow>=4.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from bokeh==2.0.2->augur==0.25.18) (9.1.0)
Requirement already satisfied: packaging>=16.8 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from bokeh==2.0.2->augur==0.25.18) (21.3)
Requirement already satisfied: tornado>=5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from bokeh==2.0.2->augur==0.25.18) (6.1)
Requirement already satisfied: typing_extensions>=3.7.4 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from bokeh==2.0.2->augur==0.25.18) (4.1.1)
Requirement already satisfied: s3transfer<0.5.0,>=0.4.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from boto3==1.17.57->augur==0.25.18) (0.4.2)
Requirement already satisfied: jmespath<1.0.0,>=0.7.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from boto3==1.17.57->augur==0.25.18) (0.10.0)
Requirement already satisfied: botocore<1.21.0,>=1.20.57 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from boto3==1.17.57->augur==0.25.18) (1.20.112)
Requirement already satisfied: humanfriendly>=9.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from coloredlogs==15.0->augur==0.25.18) (10.0)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->augur==0.25.18) (2.1.1)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->augur==0.25.18) (3.0.1)
Requirement already satisfied: setuptools>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gunicorn==20.1.0->augur==0.25.18) (49.2.1)
Requirement already satisfied: ipython>=7.17.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from ipdb==0.13.9->augur==0.25.18) (8.2.0)
Requirement already satisfied: decorator in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from ipdb==0.13.9->augur==0.25.18) (5.1.1)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2==3.0.2->augur==0.25.18) (2.1.1)
Requirement already satisfied: tqdm in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from nltk==3.6.6->augur==0.25.18) (4.64.0)
Requirement already satisfied: joblib in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from nltk==3.6.6->augur==0.25.18) (1.0.1)
Requirement already satisfied: regex>=2021.8.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from nltk==3.6.6->augur==0.25.18) (2022.3.15)
Requirement already satisfied: pytz>=2017.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pandas==1.3.5->augur==0.25.18) (2022.1)
Requirement already satisfied: attrs>=19.2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pytest==6.2.5->augur==0.25.18) (21.4.0)
Requirement already satisfied: pluggy<2.0,>=0.12 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pytest==6.2.5->augur==0.25.18) (1.0.0)
Requirement already satisfied: iniconfig in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pytest==6.2.5->augur==0.25.18) (1.1.1)
Requirement already satisfied: py>=1.8.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pytest==6.2.5->augur==0.25.18) (1.11.0)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->augur==0.25.18) (2021.10.8)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->augur==0.25.18) (1.26.9)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->augur==0.25.18) (3.3)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->augur==0.25.18) (2.0.12)
Requirement already satisfied: sphinxcontrib-devhelp in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sphinx==4.2.0->augur==0.25.18) (1.0.2)
Requirement already satisfied: sphinxcontrib-jsmath in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sphinx==4.2.0->augur==0.25.18) (1.0.1)
Requirement already satisfied: sphinxcontrib-serializinghtml>=1.1.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sphinx==4.2.0->augur==0.25.18) (1.1.5)
Requirement already satisfied: sphinxcontrib-qthelp in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sphinx==4.2.0->augur==0.25.18) (1.0.3)
Requirement already satisfied: snowballstemmer>=1.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sphinx==4.2.0->augur==0.25.18) (2.2.0)
Requirement already satisfied: Pygments>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sphinx==4.2.0->augur==0.25.18) (2.11.2)
Requirement already satisfied: alabaster<0.8,>=0.7 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sphinx==4.2.0->augur==0.25.18) (0.7.12)
Requirement already satisfied: imagesize in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sphinx==4.2.0->augur==0.25.18) (1.3.0)
Requirement already satisfied: sphinxcontrib-htmlhelp>=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sphinx==4.2.0->augur==0.25.18) (2.0.0)
Requirement already satisfied: sphinxcontrib-applehelp in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sphinx==4.2.0->augur==0.25.18) (1.0.2)
Requirement already satisfied: babel>=1.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sphinx==4.2.0->augur==0.25.18) (2.9.1)
Requirement already satisfied: sphinxcontrib-httpdomain>=1.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sphinxcontrib-openapi==0.7.0->augur==0.25.18) (1.8.0)
Requirement already satisfied: jsonschema>=2.5.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sphinxcontrib-openapi==0.7.0->augur==0.25.18) (4.4.0)
Requirement already satisfied: m2r>=0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sphinxcontrib-openapi==0.7.0->augur==0.25.18) (0.2.1)
Requirement already satisfied: filelock>=3.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tox==3.24.4->augur==0.25.18) (3.6.0)
Requirement already satisfied: virtualenv!=20.0.0,!=20.0.1,!=20.0.2,!=20.0.3,!=20.0.4,!=20.0.5,!=20.0.6,!=20.0.7,>=16.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tox==3.24.4->augur==0.25.18) (20.14.1)
Requirement already satisfied: sortedcontainers!=2.0.0,!=2.0.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from distributed>=2021.03.0->augur==0.25.18) (2.4.0)
Requirement already satisfied: tblib>=1.6.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from distributed>=2021.03.0->augur==0.25.18) (1.7.0)
Requirement already satisfied: zict>=0.1.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from distributed>=2021.03.0->augur==0.25.18) (2.1.0)
Requirement already satisfied: msgpack>=0.6.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from distributed>=2021.03.0->augur==0.25.18) (1.0.3)
Requirement already satisfied: locket in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from partd>=0.3.10->augur==0.25.18) (0.2.1)
Requirement already satisfied: matplotlib-inline in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (0.1.3)
Requirement already satisfied: jedi>=0.16 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (0.18.1)
Requirement already satisfied: traitlets>=5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (5.1.1)
Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (3.0.29)
Requirement already satisfied: appnope in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (0.1.3)
Requirement already satisfied: stack-data in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (0.2.0)
Requirement already satisfied: pexpect>4.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (4.8.0)
Requirement already satisfied: backcall in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (0.2.0)
Requirement already satisfied: pickleshare in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (0.7.5)
Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from jsonschema>=2.5.1->sphinxcontrib-openapi==0.7.0->augur==0.25.18) (0.18.1)
Requirement already satisfied: importlib-resources>=1.4.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from jsonschema>=2.5.1->sphinxcontrib-openapi==0.7.0->augur==0.25.18) (5.6.0)
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from packaging>=16.8->bokeh==2.0.2->augur==0.25.18) (3.0.8)
Requirement already satisfied: platformdirs<3,>=2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from virtualenv!=20.0.0,!=20.0.1,!=20.0.2,!=20.0.3,!=20.0.4,!=20.0.5,!=20.0.6,!=20.0.7,>=16.0.0->tox==3.24.4->augur==0.25.18) (2.5.1)
Requirement already satisfied: distlib<1,>=0.3.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from virtualenv!=20.0.0,!=20.0.1,!=20.0.2,!=20.0.3,!=20.0.4,!=20.0.5,!=20.0.6,!=20.0.7,>=16.0.0->tox==3.24.4->augur==0.25.18) (0.3.4)
Requirement already satisfied: heapdict in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from zict>=0.1.3->distributed>=2021.03.0->augur==0.25.18) (1.0.1)
Requirement already satisfied: zipp>=3.1.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from importlib-resources>=1.4.0->jsonschema>=2.5.1->sphinxcontrib-openapi==0.7.0->augur==0.25.18) (3.8.0)
Requirement already satisfied: parso<0.9.0,>=0.8.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from jedi>=0.16->ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (0.8.3)
Requirement already satisfied: ptyprocess>=0.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pexpect>4.3->ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (0.7.0)
Requirement already satisfied: wcwidth in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (0.2.5)
Requirement already satisfied: pure-eval in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from stack-data->ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (0.2.2)
Requirement already satisfied: executing in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from stack-data->ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (0.8.3)
Requirement already satisfied: asttokens in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from stack-data->ipython>=7.17.0->ipdb==0.13.9->augur==0.25.18) (2.0.5)
Installing collected packages: augur
  Attempting uninstall: augur
    Found existing installation: augur 0.25.18
    Uninstalling augur-0.25.18:
      Successfully uninstalled augur-0.25.18
  Running setup.py develop for augur
Successfully installed augur-0.25.18
Installing workers and their dependencies...
**********************************


**********************************
Installing clustering_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/clustering_worker
  Preparing metadata (setup.py) ... done
WARNING: clustering-worker 0.0.1 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from clustering-worker==0.0.1) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from clustering-worker==0.0.1) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from clustering-worker==0.0.1) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from clustering-worker==0.0.1) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from clustering-worker==0.0.1) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from clustering-worker==0.0.1) (2.9.3)
Requirement already satisfied: sklearn==0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from clustering-worker==0.0.1) (0.0)
Requirement already satisfied: numpy==1.21.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from clustering-worker==0.0.1) (1.21.0)
Requirement already satisfied: nltk==3.6.6 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from clustering-worker==0.0.1) (3.6.6)
Requirement already satisfied: seaborn==0.11.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from clustering-worker==0.0.1) (0.11.1)
Requirement already satisfied: pandas==1.3.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from clustering-worker==0.0.1) (1.3.5)
Requirement already satisfied: matplotlib==3.5.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from clustering-worker==0.0.1) (3.5.1)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->clustering-worker==0.0.1) (2.1.1)
Requirement already satisfied: click>=7.1.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->clustering-worker==0.0.1) (8.0.3)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->clustering-worker==0.0.1) (3.0.2)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->clustering-worker==0.0.1) (2.0.1)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->clustering-worker==0.0.1) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->clustering-worker==0.0.1) (3.0.1)
Requirement already satisfied: cycler>=0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from matplotlib==3.5.1->clustering-worker==0.0.1) (0.11.0)
Requirement already satisfied: python-dateutil>=2.7 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from matplotlib==3.5.1->clustering-worker==0.0.1) (2.8.2)
Requirement already satisfied: packaging>=20.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from matplotlib==3.5.1->clustering-worker==0.0.1) (21.3)
Requirement already satisfied: fonttools>=4.22.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from matplotlib==3.5.1->clustering-worker==0.0.1) (4.32.0)
Requirement already satisfied: pillow>=6.2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from matplotlib==3.5.1->clustering-worker==0.0.1) (9.1.0)
Requirement already satisfied: kiwisolver>=1.0.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from matplotlib==3.5.1->clustering-worker==0.0.1) (1.4.2)
Requirement already satisfied: pyparsing>=2.2.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from matplotlib==3.5.1->clustering-worker==0.0.1) (3.0.8)
Requirement already satisfied: regex>=2021.8.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from nltk==3.6.6->clustering-worker==0.0.1) (2022.3.15)
Requirement already satisfied: joblib in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from nltk==3.6.6->clustering-worker==0.0.1) (1.0.1)
Requirement already satisfied: tqdm in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from nltk==3.6.6->clustering-worker==0.0.1) (4.64.0)
Requirement already satisfied: pytz>=2017.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pandas==1.3.5->clustering-worker==0.0.1) (2022.1)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->clustering-worker==0.0.1) (2.0.12)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->clustering-worker==0.0.1) (1.26.9)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->clustering-worker==0.0.1) (2021.10.8)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->clustering-worker==0.0.1) (3.3)
Requirement already satisfied: scipy>=1.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from seaborn==0.11.1->clustering-worker==0.0.1) (1.7.3)
Requirement already satisfied: scikit-learn in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sklearn==0.0->clustering-worker==0.0.1) (1.0.2)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->clustering-worker==0.0.1) (2.1.1)
Requirement already satisfied: threadpoolctl>=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scikit-learn->sklearn==0.0->clustering-worker==0.0.1) (3.1.0)
Installing collected packages: clustering-worker
  Attempting uninstall: clustering-worker
    Found existing installation: clustering-worker 0.0.1
    Uninstalling clustering-worker-0.0.1:
      Successfully uninstalled clustering-worker-0.0.1
  Running setup.py develop for clustering-worker
Successfully installed clustering-worker-0.0.1

**********************************
Installing contributor_breadth_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/contributor_breadth_worker
  Preparing metadata (setup.py) ... done
WARNING: contributor-breadth-worker 0.0.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-breadth-worker==0.0.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-breadth-worker==0.0.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-breadth-worker==0.0.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-breadth-worker==0.0.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-breadth-worker==0.0.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-breadth-worker==0.0.0) (2.9.3)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->contributor-breadth-worker==0.0.0) (2.0.1)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->contributor-breadth-worker==0.0.0) (3.0.2)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->contributor-breadth-worker==0.0.0) (2.1.1)
Requirement already satisfied: click>=7.1.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->contributor-breadth-worker==0.0.0) (8.0.3)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->contributor-breadth-worker==0.0.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->contributor-breadth-worker==0.0.0) (3.0.1)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->contributor-breadth-worker==0.0.0) (2021.10.8)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->contributor-breadth-worker==0.0.0) (2.0.12)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->contributor-breadth-worker==0.0.0) (3.3)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->contributor-breadth-worker==0.0.0) (1.26.9)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->contributor-breadth-worker==0.0.0) (2.1.1)
Installing collected packages: contributor-breadth-worker
  Attempting uninstall: contributor-breadth-worker
    Found existing installation: contributor-breadth-worker 0.0.0
    Uninstalling contributor-breadth-worker-0.0.0:
      Successfully uninstalled contributor-breadth-worker-0.0.0
  Running setup.py develop for contributor-breadth-worker
Successfully installed contributor-breadth-worker-0.0.0

**********************************
Installing contributor_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/contributor_worker
  Preparing metadata (setup.py) ... done
WARNING: contributor-worker 1.0.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-worker==1.0.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-worker==1.0.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-worker==1.0.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-worker==1.0.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-worker==1.0.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-worker==1.0.0) (2.9.3)
Requirement already satisfied: click==8.0.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-worker==1.0.0) (8.0.3)
Requirement already satisfied: scipy==1.7.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-worker==1.0.0) (1.7.3)
Requirement already satisfied: sklearn==0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from contributor-worker==1.0.0) (0.0)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->contributor-worker==1.0.0) (2.0.1)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->contributor-worker==1.0.0) (3.0.2)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->contributor-worker==1.0.0) (2.1.1)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->contributor-worker==1.0.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->contributor-worker==1.0.0) (3.0.1)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->contributor-worker==1.0.0) (2021.10.8)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->contributor-worker==1.0.0) (2.0.12)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->contributor-worker==1.0.0) (3.3)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->contributor-worker==1.0.0) (1.26.9)
Requirement already satisfied: numpy<1.23.0,>=1.16.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scipy==1.7.3->contributor-worker==1.0.0) (1.21.0)
Requirement already satisfied: scikit-learn in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sklearn==0.0->contributor-worker==1.0.0) (1.0.2)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->contributor-worker==1.0.0) (2.1.1)
Requirement already satisfied: threadpoolctl>=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scikit-learn->sklearn==0.0->contributor-worker==1.0.0) (3.1.0)
Requirement already satisfied: joblib>=0.11 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scikit-learn->sklearn==0.0->contributor-worker==1.0.0) (1.0.1)
Installing collected packages: contributor-worker
  Attempting uninstall: contributor-worker
    Found existing installation: contributor-worker 1.0.0
    Uninstalling contributor-worker-1.0.0:
      Successfully uninstalled contributor-worker-1.0.0
  Running setup.py develop for contributor-worker
Successfully installed contributor-worker-1.0.0

**********************************
Installing deps_libyear_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/deps_libyear_worker
  Preparing metadata (setup.py) ... done
WARNING: deps-libyear-worker 1.0.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from deps-libyear-worker==1.0.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from deps-libyear-worker==1.0.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from deps-libyear-worker==1.0.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from deps-libyear-worker==1.0.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from deps-libyear-worker==1.0.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from deps-libyear-worker==1.0.0) (2.9.3)
Requirement already satisfied: toml in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from deps-libyear-worker==1.0.0) (0.10.2)
Requirement already satisfied: pyYaml in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from deps-libyear-worker==1.0.0) (6.0)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->deps-libyear-worker==1.0.0) (2.1.1)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->deps-libyear-worker==1.0.0) (2.0.1)
Requirement already satisfied: click>=7.1.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->deps-libyear-worker==1.0.0) (8.0.3)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->deps-libyear-worker==1.0.0) (3.0.2)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->deps-libyear-worker==1.0.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->deps-libyear-worker==1.0.0) (3.0.1)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->deps-libyear-worker==1.0.0) (2021.10.8)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->deps-libyear-worker==1.0.0) (2.0.12)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->deps-libyear-worker==1.0.0) (1.26.9)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->deps-libyear-worker==1.0.0) (3.3)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->deps-libyear-worker==1.0.0) (2.1.1)
Installing collected packages: deps-libyear-worker
  Attempting uninstall: deps-libyear-worker
    Found existing installation: deps-libyear-worker 1.0.0
    Uninstalling deps-libyear-worker-1.0.0:
      Successfully uninstalled deps-libyear-worker-1.0.0
  Running setup.py develop for deps-libyear-worker
Successfully installed deps-libyear-worker-1.0.0

**********************************
Installing deps_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/deps_worker
  Preparing metadata (setup.py) ... done
WARNING: deps-worker 1.0.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from deps-worker==1.0.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from deps-worker==1.0.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from deps-worker==1.0.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from deps-worker==1.0.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from deps-worker==1.0.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from deps-worker==1.0.0) (2.9.3)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->deps-worker==1.0.0) (2.0.1)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->deps-worker==1.0.0) (2.1.1)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->deps-worker==1.0.0) (3.0.2)
Requirement already satisfied: click>=7.1.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->deps-worker==1.0.0) (8.0.3)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->deps-worker==1.0.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->deps-worker==1.0.0) (3.0.1)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->deps-worker==1.0.0) (2021.10.8)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->deps-worker==1.0.0) (3.3)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->deps-worker==1.0.0) (2.0.12)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->deps-worker==1.0.0) (1.26.9)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->deps-worker==1.0.0) (2.1.1)
Installing collected packages: deps-worker
  Attempting uninstall: deps-worker
    Found existing installation: deps-worker 1.0.0
    Uninstalling deps-worker-1.0.0:
      Successfully uninstalled deps-worker-1.0.0
  Running setup.py develop for deps-worker
Successfully installed deps-worker-1.0.0

**********************************
Installing discourse_analysis_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/discourse_analysis_worker
  Preparing metadata (setup.py) ... done
WARNING: discourse-analysis-worker 0.0.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from discourse-analysis-worker==0.0.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from discourse-analysis-worker==0.0.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from discourse-analysis-worker==0.0.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from discourse-analysis-worker==0.0.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from discourse-analysis-worker==0.0.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from discourse-analysis-worker==0.0.0) (2.9.3)
Requirement already satisfied: click==8.0.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from discourse-analysis-worker==0.0.0) (8.0.3)
Requirement already satisfied: scipy==1.7.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from discourse-analysis-worker==0.0.0) (1.7.3)
Requirement already satisfied: nltk==3.6.6 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from discourse-analysis-worker==0.0.0) (3.6.6)
Requirement already satisfied: pandas==1.3.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from discourse-analysis-worker==0.0.0) (1.3.5)
Requirement already satisfied: scikit-learn==1.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from discourse-analysis-worker==0.0.0) (1.0.2)
Requirement already satisfied: textblob==0.15.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from discourse-analysis-worker==0.0.0) (0.15.3)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->discourse-analysis-worker==0.0.0) (2.0.1)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->discourse-analysis-worker==0.0.0) (3.0.2)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->discourse-analysis-worker==0.0.0) (2.1.1)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->discourse-analysis-worker==0.0.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->discourse-analysis-worker==0.0.0) (3.0.1)
Requirement already satisfied: joblib in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from nltk==3.6.6->discourse-analysis-worker==0.0.0) (1.0.1)
Requirement already satisfied: regex>=2021.8.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from nltk==3.6.6->discourse-analysis-worker==0.0.0) (2022.3.15)
Requirement already satisfied: tqdm in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from nltk==3.6.6->discourse-analysis-worker==0.0.0) (4.64.0)
Requirement already satisfied: numpy>=1.17.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pandas==1.3.5->discourse-analysis-worker==0.0.0) (1.21.0)
Requirement already satisfied: pytz>=2017.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pandas==1.3.5->discourse-analysis-worker==0.0.0) (2022.1)
Requirement already satisfied: python-dateutil>=2.7.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pandas==1.3.5->discourse-analysis-worker==0.0.0) (2.8.2)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->discourse-analysis-worker==0.0.0) (2021.10.8)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->discourse-analysis-worker==0.0.0) (3.3)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->discourse-analysis-worker==0.0.0) (2.0.12)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->discourse-analysis-worker==0.0.0) (1.26.9)
Requirement already satisfied: threadpoolctl>=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scikit-learn==1.0.2->discourse-analysis-worker==0.0.0) (3.1.0)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->discourse-analysis-worker==0.0.0) (2.1.1)
Installing collected packages: discourse-analysis-worker
  Attempting uninstall: discourse-analysis-worker
    Found existing installation: discourse-analysis-worker 0.0.0
    Uninstalling discourse-analysis-worker-0.0.0:
      Successfully uninstalled discourse-analysis-worker-0.0.0
  Running setup.py develop for discourse-analysis-worker
Successfully installed discourse-analysis-worker-0.0.0

**********************************
Installing facade_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/facade_worker
  Preparing metadata (setup.py) ... done
WARNING: facade-worker 1.2.4 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from facade-worker==1.2.4) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from facade-worker==1.2.4) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from facade-worker==1.2.4) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from facade-worker==1.2.4) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from facade-worker==1.2.4) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from facade-worker==1.2.4) (2.9.3)
Requirement already satisfied: click==8.0.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from facade-worker==1.2.4) (8.0.3)
Requirement already satisfied: XlsxWriter==1.3.7 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from facade-worker==1.2.4) (1.3.7)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->facade-worker==1.2.4) (2.1.1)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->facade-worker==1.2.4) (3.0.2)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->facade-worker==1.2.4) (2.0.1)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->facade-worker==1.2.4) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->facade-worker==1.2.4) (3.0.1)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->facade-worker==1.2.4) (2021.10.8)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->facade-worker==1.2.4) (2.0.12)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->facade-worker==1.2.4) (3.3)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->facade-worker==1.2.4) (1.26.9)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->facade-worker==1.2.4) (2.1.1)
Installing collected packages: facade-worker
  Attempting uninstall: facade-worker
    Found existing installation: facade-worker 1.2.4
    Uninstalling facade-worker-1.2.4:
      Successfully uninstalled facade-worker-1.2.4
  Running setup.py develop for facade-worker
Successfully installed facade-worker-1.2.4

**********************************
Installing github_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/github_worker
  Preparing metadata (setup.py) ... done
WARNING: github-worker 1.0.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from github-worker==1.0.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from github-worker==1.0.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from github-worker==1.0.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from github-worker==1.0.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from github-worker==1.0.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from github-worker==1.0.0) (2.9.3)
Requirement already satisfied: click==8.0.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from github-worker==1.0.0) (8.0.3)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->github-worker==1.0.0) (3.0.2)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->github-worker==1.0.0) (2.0.1)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->github-worker==1.0.0) (2.1.1)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->github-worker==1.0.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->github-worker==1.0.0) (3.0.1)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->github-worker==1.0.0) (1.26.9)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->github-worker==1.0.0) (3.3)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->github-worker==1.0.0) (2.0.12)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->github-worker==1.0.0) (2021.10.8)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->github-worker==1.0.0) (2.1.1)
Installing collected packages: github-worker
  Attempting uninstall: github-worker
    Found existing installation: github-worker 1.0.0
    Uninstalling github-worker-1.0.0:
      Successfully uninstalled github-worker-1.0.0
  Running setup.py develop for github-worker
Successfully installed github-worker-1.0.0

**********************************
Installing gitlab_issues_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/gitlab_issues_worker
  Preparing metadata (setup.py) ... done
WARNING: gitlab-issues-worker 0.0.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gitlab-issues-worker==0.0.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gitlab-issues-worker==0.0.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gitlab-issues-worker==0.0.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gitlab-issues-worker==0.0.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gitlab-issues-worker==0.0.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gitlab-issues-worker==0.0.0) (2.9.3)
Requirement already satisfied: click==8.0.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gitlab-issues-worker==0.0.0) (8.0.3)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->gitlab-issues-worker==0.0.0) (2.1.1)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->gitlab-issues-worker==0.0.0) (3.0.2)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->gitlab-issues-worker==0.0.0) (2.0.1)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->gitlab-issues-worker==0.0.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->gitlab-issues-worker==0.0.0) (3.0.1)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->gitlab-issues-worker==0.0.0) (1.26.9)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->gitlab-issues-worker==0.0.0) (3.3)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->gitlab-issues-worker==0.0.0) (2.0.12)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->gitlab-issues-worker==0.0.0) (2021.10.8)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->gitlab-issues-worker==0.0.0) (2.1.1)
Installing collected packages: gitlab-issues-worker
  Attempting uninstall: gitlab-issues-worker
    Found existing installation: gitlab-issues-worker 0.0.0
    Uninstalling gitlab-issues-worker-0.0.0:
      Successfully uninstalled gitlab-issues-worker-0.0.0
  Running setup.py develop for gitlab-issues-worker
Successfully installed gitlab-issues-worker-0.0.0

**********************************
Installing gitlab_merge_request_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/gitlab_merge_request_worker
  Preparing metadata (setup.py) ... done
WARNING: gitlab-merge-request-worker 0.0.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gitlab-merge-request-worker==0.0.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gitlab-merge-request-worker==0.0.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gitlab-merge-request-worker==0.0.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gitlab-merge-request-worker==0.0.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gitlab-merge-request-worker==0.0.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gitlab-merge-request-worker==0.0.0) (2.9.3)
Requirement already satisfied: click==8.0.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gitlab-merge-request-worker==0.0.0) (8.0.3)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->gitlab-merge-request-worker==0.0.0) (2.1.1)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->gitlab-merge-request-worker==0.0.0) (2.0.1)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->gitlab-merge-request-worker==0.0.0) (3.0.2)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->gitlab-merge-request-worker==0.0.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->gitlab-merge-request-worker==0.0.0) (3.0.1)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->gitlab-merge-request-worker==0.0.0) (2.0.12)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->gitlab-merge-request-worker==0.0.0) (2021.10.8)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->gitlab-merge-request-worker==0.0.0) (3.3)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->gitlab-merge-request-worker==0.0.0) (1.26.9)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->gitlab-merge-request-worker==0.0.0) (2.1.1)
Installing collected packages: gitlab-merge-request-worker
  Attempting uninstall: gitlab-merge-request-worker
    Found existing installation: gitlab-merge-request-worker 0.0.0
    Uninstalling gitlab-merge-request-worker-0.0.0:
      Successfully uninstalled gitlab-merge-request-worker-0.0.0
  Running setup.py develop for gitlab-merge-request-worker
Successfully installed gitlab-merge-request-worker-0.0.0

**********************************
Installing insight_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/insight_worker
  Preparing metadata (setup.py) ... done
WARNING: insight-worker 1.0.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from insight-worker==1.0.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from insight-worker==1.0.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from insight-worker==1.0.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from insight-worker==1.0.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from insight-worker==1.0.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from insight-worker==1.0.0) (2.9.3)
Requirement already satisfied: click==8.0.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from insight-worker==1.0.0) (8.0.3)
Requirement already satisfied: scipy>=1.7.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from insight-worker==1.0.0) (1.7.3)
Requirement already satisfied: sklearn==0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from insight-worker==1.0.0) (0.0)
Requirement already satisfied: numpy>=1.21.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from insight-worker==1.0.0) (1.21.0)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->insight-worker==1.0.0) (2.1.1)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->insight-worker==1.0.0) (3.0.2)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->insight-worker==1.0.0) (2.0.1)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->insight-worker==1.0.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->insight-worker==1.0.0) (3.0.1)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->insight-worker==1.0.0) (3.3)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->insight-worker==1.0.0) (2021.10.8)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->insight-worker==1.0.0) (1.26.9)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->insight-worker==1.0.0) (2.0.12)
Requirement already satisfied: scikit-learn in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sklearn==0.0->insight-worker==1.0.0) (1.0.2)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->insight-worker==1.0.0) (2.1.1)
Requirement already satisfied: joblib>=0.11 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scikit-learn->sklearn==0.0->insight-worker==1.0.0) (1.0.1)
Requirement already satisfied: threadpoolctl>=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scikit-learn->sklearn==0.0->insight-worker==1.0.0) (3.1.0)
Installing collected packages: insight-worker
  Attempting uninstall: insight-worker
    Found existing installation: insight-worker 1.0.0
    Uninstalling insight-worker-1.0.0:
      Successfully uninstalled insight-worker-1.0.0
  Running setup.py develop for insight-worker
Successfully installed insight-worker-1.0.0

**********************************
Installing linux_badge_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/linux_badge_worker
  Preparing metadata (setup.py) ... done
WARNING: linux-badge-worker 1.0.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from linux-badge-worker==1.0.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from linux-badge-worker==1.0.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from linux-badge-worker==1.0.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from linux-badge-worker==1.0.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from linux-badge-worker==1.0.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from linux-badge-worker==1.0.0) (2.9.3)
Requirement already satisfied: click==8.0.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from linux-badge-worker==1.0.0) (8.0.3)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->linux-badge-worker==1.0.0) (3.0.2)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->linux-badge-worker==1.0.0) (2.1.1)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->linux-badge-worker==1.0.0) (2.0.1)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->linux-badge-worker==1.0.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->linux-badge-worker==1.0.0) (3.0.1)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->linux-badge-worker==1.0.0) (1.26.9)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->linux-badge-worker==1.0.0) (3.3)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->linux-badge-worker==1.0.0) (2021.10.8)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->linux-badge-worker==1.0.0) (2.0.12)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->linux-badge-worker==1.0.0) (2.1.1)
Installing collected packages: linux-badge-worker
  Attempting uninstall: linux-badge-worker
    Found existing installation: linux-badge-worker 1.0.0
    Uninstalling linux-badge-worker-1.0.0:
      Successfully uninstalled linux-badge-worker-1.0.0
  Running setup.py develop for linux-badge-worker
Successfully installed linux-badge-worker-1.0.0

**********************************
Installing message_insights_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/message_insights_worker
  Preparing metadata (setup.py) ... done
WARNING: message-insights-worker 0.2.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (2.9.3)
Requirement already satisfied: click==8.0.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (8.0.3)
Requirement already satisfied: scipy==1.7.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (1.7.3)
Requirement already satisfied: sklearn==0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (0.0)
Requirement already satisfied: numpy==1.21.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (1.21.0)
Requirement already satisfied: nltk==3.6.6 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (3.6.6)
Requirement already satisfied: pandas==1.3.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (1.3.5)
Requirement already satisfied: gensim==4.1.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (4.1.2)
Requirement already satisfied: emoji==1.2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (1.2.0)
Requirement already satisfied: Keras>=2.8.0rc0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (2.8.0)
Requirement already satisfied: Keras-Preprocessing==1.1.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (1.1.2)
Requirement already satisfied: tensorflow==2.8.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (2.8.0)
Requirement already satisfied: h5py~=3.6.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (3.6.0)
Requirement already satisfied: scikit-image==0.19.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (0.19.1)
Requirement already satisfied: joblib==1.0.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (1.0.1)
Requirement already satisfied: xgboost in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (1.4.2)
Requirement already satisfied: bs4==0.0.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (0.0.1)
Requirement already satisfied: xlrd==2.0.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from message-insights-worker==0.2.0) (2.0.1)
Requirement already satisfied: beautifulsoup4 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from bs4==0.0.1->message-insights-worker==0.2.0) (4.11.1)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->message-insights-worker==0.2.0) (3.0.2)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->message-insights-worker==0.2.0) (2.1.1)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->message-insights-worker==0.2.0) (2.0.1)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->message-insights-worker==0.2.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->message-insights-worker==0.2.0) (3.0.1)
Requirement already satisfied: smart-open>=1.8.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gensim==4.1.2->message-insights-worker==0.2.0) (5.2.1)
Requirement already satisfied: tqdm in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from nltk==3.6.6->message-insights-worker==0.2.0) (4.64.0)
Requirement already satisfied: regex>=2021.8.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from nltk==3.6.6->message-insights-worker==0.2.0) (2022.3.15)
Requirement already satisfied: pytz>=2017.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pandas==1.3.5->message-insights-worker==0.2.0) (2022.1)
Requirement already satisfied: python-dateutil>=2.7.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pandas==1.3.5->message-insights-worker==0.2.0) (2.8.2)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->message-insights-worker==0.2.0) (2021.10.8)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->message-insights-worker==0.2.0) (2.0.12)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->message-insights-worker==0.2.0) (1.26.9)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->message-insights-worker==0.2.0) (3.3)
Requirement already satisfied: packaging>=20.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scikit-image==0.19.1->message-insights-worker==0.2.0) (21.3)
Requirement already satisfied: imageio>=2.4.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scikit-image==0.19.1->message-insights-worker==0.2.0) (2.16.2)
Requirement already satisfied: networkx>=2.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scikit-image==0.19.1->message-insights-worker==0.2.0) (2.8)
Requirement already satisfied: PyWavelets>=1.1.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scikit-image==0.19.1->message-insights-worker==0.2.0) (1.3.0)
Requirement already satisfied: tifffile>=2019.7.26 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scikit-image==0.19.1->message-insights-worker==0.2.0) (2022.4.8)
Requirement already satisfied: pillow!=7.1.0,!=7.1.1,!=8.3.0,>=6.1.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scikit-image==0.19.1->message-insights-worker==0.2.0) (9.1.0)
Requirement already satisfied: scikit-learn in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sklearn==0.0->message-insights-worker==0.2.0) (1.0.2)
Requirement already satisfied: flatbuffers>=1.12 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (2.0)
Requirement already satisfied: astunparse>=1.6.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (1.6.3)
Requirement already satisfied: tensorboard<2.9,>=2.8 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (2.8.0)
Requirement already satisfied: wrapt>=1.11.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (1.14.0)
Requirement already satisfied: absl-py>=0.4.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (1.0.0)
Requirement already satisfied: opt-einsum>=2.3.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (3.3.0)
Requirement already satisfied: termcolor>=1.1.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (1.1.0)
Requirement already satisfied: google-pasta>=0.1.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (0.2.0)
Requirement already satisfied: setuptools in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (49.2.1)
Requirement already satisfied: protobuf>=3.9.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (3.20.0)
Requirement already satisfied: grpcio<2.0,>=1.24.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (1.44.0)
Requirement already satisfied: gast>=0.2.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (0.5.3)
Requirement already satisfied: tensorflow-io-gcs-filesystem>=0.23.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (0.24.0)
Requirement already satisfied: libclang>=9.0.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (13.0.0)
Requirement already satisfied: tf-estimator-nightly==2.8.0.dev2021122109 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (2.8.0.dev2021122109)
Requirement already satisfied: typing-extensions>=3.6.6 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorflow==2.8.0->message-insights-worker==0.2.0) (4.1.1)
Requirement already satisfied: wheel<1.0,>=0.23.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from astunparse>=1.6.0->tensorflow==2.8.0->message-insights-worker==0.2.0) (0.37.1)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->message-insights-worker==0.2.0) (2.1.1)
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from packaging>=20.0->scikit-image==0.19.1->message-insights-worker==0.2.0) (3.0.8)
Requirement already satisfied: google-auth<3,>=1.6.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorboard<2.9,>=2.8->tensorflow==2.8.0->message-insights-worker==0.2.0) (2.6.3)
Requirement already satisfied: tensorboard-data-server<0.7.0,>=0.6.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorboard<2.9,>=2.8->tensorflow==2.8.0->message-insights-worker==0.2.0) (0.6.1)
Requirement already satisfied: markdown>=2.6.8 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorboard<2.9,>=2.8->tensorflow==2.8.0->message-insights-worker==0.2.0) (3.3.6)
Requirement already satisfied: google-auth-oauthlib<0.5,>=0.4.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorboard<2.9,>=2.8->tensorflow==2.8.0->message-insights-worker==0.2.0) (0.4.6)
Requirement already satisfied: tensorboard-plugin-wit>=1.6.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from tensorboard<2.9,>=2.8->tensorflow==2.8.0->message-insights-worker==0.2.0) (1.8.1)
Requirement already satisfied: soupsieve>1.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from beautifulsoup4->bs4==0.0.1->message-insights-worker==0.2.0) (2.3.2)
Requirement already satisfied: threadpoolctl>=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scikit-learn->sklearn==0.0->message-insights-worker==0.2.0) (3.1.0)
Requirement already satisfied: rsa<5,>=3.1.4 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from google-auth<3,>=1.6.3->tensorboard<2.9,>=2.8->tensorflow==2.8.0->message-insights-worker==0.2.0) (4.8)
Requirement already satisfied: cachetools<6.0,>=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from google-auth<3,>=1.6.3->tensorboard<2.9,>=2.8->tensorflow==2.8.0->message-insights-worker==0.2.0) (5.0.0)
Requirement already satisfied: pyasn1-modules>=0.2.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from google-auth<3,>=1.6.3->tensorboard<2.9,>=2.8->tensorflow==2.8.0->message-insights-worker==0.2.0) (0.2.8)
Requirement already satisfied: requests-oauthlib>=0.7.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.9,>=2.8->tensorflow==2.8.0->message-insights-worker==0.2.0) (1.3.1)
Requirement already satisfied: importlib-metadata>=4.4 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from markdown>=2.6.8->tensorboard<2.9,>=2.8->tensorflow==2.8.0->message-insights-worker==0.2.0) (4.11.3)
Requirement already satisfied: zipp>=0.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from importlib-metadata>=4.4->markdown>=2.6.8->tensorboard<2.9,>=2.8->tensorflow==2.8.0->message-insights-worker==0.2.0) (3.8.0)
Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard<2.9,>=2.8->tensorflow==2.8.0->message-insights-worker==0.2.0) (0.4.8)
Requirement already satisfied: oauthlib>=3.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.9,>=2.8->tensorflow==2.8.0->message-insights-worker==0.2.0) (3.2.0)
Installing collected packages: message-insights-worker
  Attempting uninstall: message-insights-worker
    Found existing installation: message-insights-worker 0.2.0
    Uninstalling message-insights-worker-0.2.0:
      Successfully uninstalled message-insights-worker-0.2.0
  Running setup.py develop for message-insights-worker
Successfully installed message-insights-worker-0.2.0

**********************************
Installing pull_request_analysis_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/pull_request_analysis_worker
  Preparing metadata (setup.py) ... done
WARNING: pull-request-analysis-worker 0.0.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (2.9.3)
Requirement already satisfied: sklearn==0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (0.0)
Requirement already satisfied: nltk==3.6.6 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (3.6.6)
Requirement already satisfied: numpy==1.21.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (1.21.0)
Requirement already satisfied: pandas==1.3.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (1.3.5)
Requirement already satisfied: gensim==4.1.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (4.1.2)
Requirement already satisfied: emoji==1.2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (1.2.0)
Requirement already satisfied: joblib==1.0.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (1.0.1)
Requirement already satisfied: xgboost==1.4.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (1.4.2)
Requirement already satisfied: scipy==1.7.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-analysis-worker==0.0.0) (1.7.3)
Requirement already satisfied: click>=7.1.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->pull-request-analysis-worker==0.0.0) (8.0.3)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->pull-request-analysis-worker==0.0.0) (3.0.2)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->pull-request-analysis-worker==0.0.0) (2.0.1)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->pull-request-analysis-worker==0.0.0) (2.1.1)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->pull-request-analysis-worker==0.0.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->pull-request-analysis-worker==0.0.0) (3.0.1)
Requirement already satisfied: smart-open>=1.8.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from gensim==4.1.2->pull-request-analysis-worker==0.0.0) (5.2.1)
Requirement already satisfied: tqdm in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from nltk==3.6.6->pull-request-analysis-worker==0.0.0) (4.64.0)
Requirement already satisfied: regex>=2021.8.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from nltk==3.6.6->pull-request-analysis-worker==0.0.0) (2022.3.15)
Requirement already satisfied: python-dateutil>=2.7.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pandas==1.3.5->pull-request-analysis-worker==0.0.0) (2.8.2)
Requirement already satisfied: pytz>=2017.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pandas==1.3.5->pull-request-analysis-worker==0.0.0) (2022.1)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->pull-request-analysis-worker==0.0.0) (2021.10.8)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->pull-request-analysis-worker==0.0.0) (3.3)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->pull-request-analysis-worker==0.0.0) (1.26.9)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->pull-request-analysis-worker==0.0.0) (2.0.12)
Requirement already satisfied: scikit-learn in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from sklearn==0.0->pull-request-analysis-worker==0.0.0) (1.0.2)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->pull-request-analysis-worker==0.0.0) (2.1.1)
Requirement already satisfied: threadpoolctl>=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from scikit-learn->sklearn==0.0->pull-request-analysis-worker==0.0.0) (3.1.0)
Installing collected packages: pull-request-analysis-worker
  Attempting uninstall: pull-request-analysis-worker
    Found existing installation: pull-request-analysis-worker 0.0.0
    Uninstalling pull-request-analysis-worker-0.0.0:
      Successfully uninstalled pull-request-analysis-worker-0.0.0
  Running setup.py develop for pull-request-analysis-worker
Successfully installed pull-request-analysis-worker-0.0.0

**********************************
Installing pull_request_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/pull_request_worker
  Preparing metadata (setup.py) ... done
WARNING: pull-request-worker 1.2.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-worker==1.2.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-worker==1.2.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-worker==1.2.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-worker==1.2.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-worker==1.2.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-worker==1.2.0) (2.9.3)
Requirement already satisfied: click==8.0.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from pull-request-worker==1.2.0) (8.0.3)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->pull-request-worker==1.2.0) (3.0.2)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->pull-request-worker==1.2.0) (2.1.1)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->pull-request-worker==1.2.0) (2.0.1)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->pull-request-worker==1.2.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->pull-request-worker==1.2.0) (3.0.1)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->pull-request-worker==1.2.0) (2021.10.8)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->pull-request-worker==1.2.0) (1.26.9)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->pull-request-worker==1.2.0) (2.0.12)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->pull-request-worker==1.2.0) (3.3)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->pull-request-worker==1.2.0) (2.1.1)
Installing collected packages: pull-request-worker
  Attempting uninstall: pull-request-worker
    Found existing installation: pull-request-worker 1.2.0
    Uninstalling pull-request-worker-1.2.0:
      Successfully uninstalled pull-request-worker-1.2.0
  Running setup.py develop for pull-request-worker
Successfully installed pull-request-worker-1.2.0

**********************************
Installing release_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/release_worker
  Preparing metadata (setup.py) ... done
WARNING: release-worker 1.0.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from release-worker==1.0.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from release-worker==1.0.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from release-worker==1.0.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from release-worker==1.0.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from release-worker==1.0.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from release-worker==1.0.0) (2.9.3)
Requirement already satisfied: click==8.0.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from release-worker==1.0.0) (8.0.3)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->release-worker==1.0.0) (2.0.1)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->release-worker==1.0.0) (2.1.1)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->release-worker==1.0.0) (3.0.2)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->release-worker==1.0.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->release-worker==1.0.0) (3.0.1)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->release-worker==1.0.0) (3.3)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->release-worker==1.0.0) (2.0.12)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->release-worker==1.0.0) (1.26.9)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->release-worker==1.0.0) (2021.10.8)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->release-worker==1.0.0) (2.1.1)
Installing collected packages: release-worker
  Attempting uninstall: release-worker
    Found existing installation: release-worker 1.0.0
    Uninstalling release-worker-1.0.0:
      Successfully uninstalled release-worker-1.0.0
  Running setup.py develop for release-worker
Successfully installed release-worker-1.0.0

**********************************
Installing repo_info_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/repo_info_worker
  Preparing metadata (setup.py) ... done
WARNING: repo-info-worker 1.0.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from repo-info-worker==1.0.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from repo-info-worker==1.0.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from repo-info-worker==1.0.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from repo-info-worker==1.0.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from repo-info-worker==1.0.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from repo-info-worker==1.0.0) (2.9.3)
Requirement already satisfied: click>=7.1.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->repo-info-worker==1.0.0) (8.0.3)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->repo-info-worker==1.0.0) (3.0.2)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->repo-info-worker==1.0.0) (2.0.1)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->repo-info-worker==1.0.0) (2.1.1)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->repo-info-worker==1.0.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->repo-info-worker==1.0.0) (3.0.1)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->repo-info-worker==1.0.0) (2.0.12)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->repo-info-worker==1.0.0) (3.3)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->repo-info-worker==1.0.0) (2021.10.8)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->repo-info-worker==1.0.0) (1.26.9)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->repo-info-worker==1.0.0) (2.1.1)
Installing collected packages: repo-info-worker
  Attempting uninstall: repo-info-worker
    Found existing installation: repo-info-worker 1.0.0
    Uninstalling repo-info-worker-1.0.0:
      Successfully uninstalled repo-info-worker-1.0.0
  Running setup.py develop for repo-info-worker
Successfully installed repo-info-worker-1.0.0

**********************************
Installing value_worker...
**********************************

Obtaining file:///Users/dmiller/augur/workers/value_worker
  Preparing metadata (setup.py) ... done
WARNING: value-worker 1.0.0 does not provide the extra 'dev'
Requirement already satisfied: Flask==2.0.2 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from value-worker==1.0.0) (2.0.2)
Requirement already satisfied: Flask-Cors==3.0.10 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from value-worker==1.0.0) (3.0.10)
Requirement already satisfied: Flask-Login==0.5.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from value-worker==1.0.0) (0.5.0)
Requirement already satisfied: Flask-WTF==1.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from value-worker==1.0.0) (1.0.0)
Requirement already satisfied: requests==2.27.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from value-worker==1.0.0) (2.27.1)
Requirement already satisfied: psycopg2-binary==2.9.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from value-worker==1.0.0) (2.9.3)
Requirement already satisfied: click==8.0.3 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from value-worker==1.0.0) (8.0.3)
Requirement already satisfied: Jinja2>=3.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->value-worker==1.0.0) (3.0.2)
Requirement already satisfied: itsdangerous>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->value-worker==1.0.0) (2.0.1)
Requirement already satisfied: Werkzeug>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask==2.0.2->value-worker==1.0.0) (2.1.1)
Requirement already satisfied: Six in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-Cors==3.0.10->value-worker==1.0.0) (1.15.0)
Requirement already satisfied: WTForms in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Flask-WTF==1.0.0->value-worker==1.0.0) (3.0.1)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->value-worker==1.0.0) (2.0.12)
Requirement already satisfied: certifi>=2017.4.17 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->value-worker==1.0.0) (2021.10.8)
Requirement already satisfied: idna<4,>=2.5 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->value-worker==1.0.0) (3.3)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from requests==2.27.1->value-worker==1.0.0) (1.26.9)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/dmiller/.virtualenvs/augur_env/lib/python3.8/site-packages (from Jinja2>=3.0->Flask==2.0.2->value-worker==1.0.0) (2.1.1)
Installing collected packages: value-worker
  Attempting uninstall: value-worker
    Found existing installation: value-worker 1.0.0
    Uninstalling value-worker-1.0.0:
      Successfully uninstalled value-worker-1.0.0
  Running setup.py develop for value-worker
Successfully installed value-worker-1.0.0
 Scorecard already exists, skipping cloning ...

Checking database version...
CLI: [db.check_pgpass_credentials] [INFO] Credentials found in $HOME/.pgpass
CLI: [db.check_for_upgrade] [INFO] Database is already up to date.
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ ls
auggie			detailed-installation	docker			quick-start.rst		schema
conf.py			development-guide	index.rst		rest-api		web-server-config
(augur_env) (base) mu-581988:source dmiller$ make docs-view
make: *** No rule to make target `docs-view'.  Stop.
(augur_env) (base) mu-581988:source dmiller$ make docs
make: *** No rule to make target `docs'.  Stop.
(augur_env) (base) mu-581988:source dmiller$ ls
auggie			detailed-installation	docker			quick-start.rst		schema
conf.py			development-guide	index.rst		rest-api		web-server-config
(augur_env) (base) mu-581988:source dmiller$ cd ..
(augur_env) (base) mu-581988:docs dmiller$ make docs
Running Sphinx v4.2.0

Sphinx error:
Builder name docs not registered or available through entry point
make: *** [docs] Error 2
(augur_env) (base) mu-581988:docs dmiller$ ls
Makefile			augur.0.21.0.release-notes.md	fedora-install.md		pull_request_template.md	source
(augur_env) (base) mu-581988:docs dmiller$ cd ..
(augur_env) (base) mu-581988:augur dmiller$ make docs
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ ls
auggie			detailed-installation	docker			quick-start.rst		schema
conf.py			development-guide	index.rst		rest-api		web-server-config
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ cd ../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ l
-bash: l: command not found
(augur_env) (base) mu-581988:augur dmiller$ 
(augur_env) (base) mu-581988:augur dmiller$ 
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ ls
auggie			detailed-installation	docker			quick-start.rst		schema
conf.py			development-guide	index.rst		rest-api		web-server-config
(augur_env) (base) mu-581988:source dmiller$ cd detailed-installation/
(augur_env) (base) mu-581988:detailed-installation dmiller$ ls
collecting-data.rst	command-line-interface	database.rst		frontend.rst		images			installation.rst	toc.rst
(augur_env) (base) mu-581988:detailed-installation dmiller$ vim  database.rst 
(augur_env) (base) mu-581988:detailed-installation dmiller$ vim installation.rst 
(augur_env) (base) mu-581988:detailed-installation dmiller$ ls
collecting-data.rst	command-line-interface	database.rst		frontend.rst		images			installation.rst	toc.rst
(augur_env) (base) mu-581988:detailed-installation dmiller$ vim installation.rst 
(augur_env) (base) mu-581988:detailed-installation dmiller$ pwd
/Users/dmiller/augur/docs/source/detailed-installation
(augur_env) (base) mu-581988:detailed-installation dmiller$ ls
collecting-data.rst	command-line-interface	database.rst		frontend.rst		images			installation.rst	toc.rst
(augur_env) (base) mu-581988:detailed-installation dmiller$ vim installation.rst 
(augur_env) (base) mu-581988:detailed-installation dmiller$ cd ../../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/detailed-installation/
(augur_env) (base) mu-581988:detailed-installation dmiller$ ls
collecting-data.rst	command-line-interface	database.rst		frontend.rst		images			installation.rst	toc.rst
(augur_env) (base) mu-581988:detailed-installation dmiller$ vim installation.rst 
(augur_env) (base) mu-581988:detailed-installation dmiller$ cd ../../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ ls
CODE_OF_CONDUCT.md	README.md		augur.egg-info		database-compose.yml	frontend-compose.yml	readthedocs.yml		setup.py		workers
CONTRIBUTING.md		SECURITY.md		augur_service.md	docker-compose.yml	lib-0.16.1.md		repos			ssl
LICENSE			Vagrantfile		augur_service.sh	docker-setup.sh		log_analysis		runtime			tests
MANIFEST.in		augur			augurface		docs			logs			schema			tox.ini
Makefile		augur.config.json	conftest.py		frontend		metadata.py		scripts			util
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ ls
auggie			detailed-installation	docker			quick-start.rst		schema
conf.py			development-guide	index.rst		rest-api		web-server-config
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ cd ../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ ls
CODE_OF_CONDUCT.md	README.md		augur.egg-info		database-compose.yml	frontend-compose.yml	readthedocs.yml		setup.py		workers
CONTRIBUTING.md		SECURITY.md		augur_service.md	docker-compose.yml	lib-0.16.1.md		repos			ssl
LICENSE			Vagrantfile		augur_service.sh	docker-setup.sh		log_analysis		runtime			tests
MANIFEST.in		augur			augurface		docs			logs			schema			tox.ini
Makefile		augur.config.json	conftest.py		frontend		metadata.py		scripts			util
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ vim quick-start.rst 
(augur_env) (base) mu-581988:source dmiller$ cd ../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ ls
CODE_OF_CONDUCT.md	README.md		augur.egg-info		database-compose.yml	frontend-compose.yml	readthedocs.yml		setup.py		workers
CONTRIBUTING.md		SECURITY.md		augur_service.md	docker-compose.yml	lib-0.16.1.md		repos			ssl
LICENSE			Vagrantfile		augur_service.sh	docker-setup.sh		log_analysis		runtime			tests
MANIFEST.in		augur			augurface		docs			logs			schema			tox.ini
Makefile		augur.config.json	conftest.py		frontend		metadata.py		scripts			util
(augur_env) (base) mu-581988:augur dmiller$ ls
CODE_OF_CONDUCT.md	README.md		augur.egg-info		database-compose.yml	frontend-compose.yml	readthedocs.yml		setup.py		workers
CONTRIBUTING.md		SECURITY.md		augur_service.md	docker-compose.yml	lib-0.16.1.md		repos			ssl
LICENSE			Vagrantfile		augur_service.sh	docker-setup.sh		log_analysis		runtime			tests
MANIFEST.in		augur			augurface		docs			logs			schema			tox.ini
Makefile		augur.config.json	conftest.py		frontend		metadata.py		scripts			util
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ cd ../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ cd ../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ cd ../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ cd ../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ cd ../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ cd ../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ ls
auggie			detailed-installation	docker			quick-start.rst		schema
conf.py			development-guide	index.rst		rest-api		web-server-config
(augur_env) (base) mu-581988:source dmiller$ vim quick-start.rst 
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ cd ../.. 
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ vim index.rst 
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ ls
auggie			detailed-installation	docker			quick-start.rst		schema
conf.py			development-guide	index.rst		rest-api		web-server-config
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ vim quick-start.rst 
(augur_env) (base) mu-581988:source dmiller$ cd ../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ cd ../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 
(augur_env) (base) mu-581988:source dmiller$ ls
auggie			detailed-installation	docker			quick-start.rst		schema
conf.py			development-guide	index.rst		rest-api		web-server-config
(augur_env) (base) mu-581988:source dmiller$ cd detailed-installation/
(augur_env) (base) mu-581988:detailed-installation dmiller$ vim installation.rst 
(augur_env) (base) mu-581988:detailed-installation dmiller$ cd ../../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/detailed-installation/
(augur_env) (base) mu-581988:detailed-installation dmiller$ ls
collecting-data.rst	command-line-interface	database.rst		frontend.rst		images			installation.rst	toc.rst
(augur_env) (base) mu-581988:detailed-installation dmiller$ vim installation.rst 
(augur_env) (base) mu-581988:detailed-installation dmiller$ cd ../../..
(augur_env) (base) mu-581988:augur dmiller$ make docs-view
Running Sphinx v4.2.0
making output directory... done
[autosummary] generating autosummary for: detailed-installation/collecting-data.rst, detailed-installation/command-line-interface/backend.rst, detailed-installation/command-line-interface/configure.rst, detailed-installation/command-line-interface/db.rst, detailed-installation/command-line-interface/logging.rst, detailed-installation/command-line-interface/toc.rst, detailed-installation/database.rst, detailed-installation/frontend.rst, detailed-installation/installation.rst, detailed-installation/toc.rst, ..., schema/commits.rst, schema/contributors.rst, schema/dependencies.rst, schema/issues.rst, schema/overview.rst, schema/pull-requests.rst, schema/toc.rst, web-server-config/nginx-configuration.rst, web-server-config/server-deployment.rst, web-server-config/toc.rst
loading intersphinx inventory from https://docs.python.org/objects.inv...
intersphinx inventory has moved: https://docs.python.org/objects.inv -> https://docs.python.org/3/objects.inv
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 51 source files that are out of date
updating environment: [new config] 51 added, 0 changed, 0 removed
reading sources... [100%] web-server-config/toc                                                                                                                                                             
/Users/dmiller/augur/docs/source/detailed-installation/toc.rst:1: WARNING: Title overline too short.

==================
Detailed Installation
==================
looking for now-outdated files... none found
pickling environment... done
checking consistency... /Users/dmiller/augur/docs/source/web-server-config/server-deployment.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] web-server-config/toc                                                                                                                                                              
generating indices... genindex http-routingtable done
writing additional pages... search done
copying images... [100%] schema/images/20211011-pull-requests-augur-schema-v0.21.1.png                                                                                                                      
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in build/html.
(augur_env) (base) mu-581988:augur dmiller$ ls
CODE_OF_CONDUCT.md	README.md		augur.egg-info		database-compose.yml	frontend-compose.yml	readthedocs.yml		setup.py		workers
CONTRIBUTING.md		SECURITY.md		augur_service.md	docker-compose.yml	lib-0.16.1.md		repos			ssl
LICENSE			Vagrantfile		augur_service.sh	docker-setup.sh		log_analysis		runtime			tests
MANIFEST.in		augur			augurface		docs			logs			schema			tox.ini
Makefile		augur.config.json	conftest.py		frontend		metadata.py		scripts			util
(augur_env) (base) mu-581988:augur dmiller$ cd docs/source/
(augur_env) (base) mu-581988:source dmiller$ ls
auggie			detailed-installation	docker			quick-start.rst		schema
conf.py			development-guide	index.rst		rest-api		web-server-config
(augur_env) (base) mu-581988:source dmiller$ vim index.rst 

.. image:: development-guide/images/augur-architecture.png
  :width: 700
  :alt: Development guide image overview of augur

Current maintainers
--------------------
- `Derek Howard <https://github.com/howderek>`_
- `Sean P. Goggins <http://www.seangoggins.net>`_
- `Matt Snell <https://github.com/Nebrethar>`_
- `Andrew Brain <https://github.com/ABrain7710>`_


Former maintainers
--------------------
- `Christian Cmehil-Warn <https://github.com/christiancme>`_
- `Jonah Zukosky <https://github.com/jonahz5222>`_
- `Carolyn Perniciaro <https://github.com/CMPerniciaro>`_
- `Elita Nelson <https://github.com/ElitaNelson>`_
- `Michael Woodruff <https://github.com/michaelwoodruffdev/>`_
- `Max Balk <https://github.com/maxbalk/>`_

Contributors
--------------------
- `Dawn Foster <https://github.com/geekygirldawn/>`_
- `Ivana Atanasova <https://github.com/ivanayov/>`_
- `Georg J.P. Link <https://github.com/GeorgLink/>`_

GSoC 2020 participants
-----------------------
- `Akshara P <https://github.com/aksh555/>`_
- `Tianyi Zhou <https://github.com/tianyichow/>`_
- `Pratik Mishra <https://github.com/pratikmishra356/>`_
- `Sarit Adhikari <https://github.com/sarit-adh/>`_
- `Saicharan Reddy <https://github.com/mrsaicharan1/>`_
- `Abhinav Bajpai <https://github.com/abhinavbajpai2012/>`_

GSoC 2019 participants
-----------------------
- `Bingwen Ma <https://github.com/bing0n3/>`_
- `Parth Sharma <https://github.com/parthsharma2/>`_

GSoC 2018 participants
-----------------------
- `Keanu Nichols <https://github.com/kmn5409/>`_

.. toctree::
   :hidden:
   :maxdepth: 2

   web-server-config/toc
   quick-start
   detailed-installation/toc
   development-guide/toc
   rest-api/api
   docker/toc
   schema/toc
..
  library-documentation/toc
..
  deployment/toc
..
  schema/toc
