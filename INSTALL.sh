#!/bin/bash
## Back End
rm -rf build/*; rm $VIRTUAL_ENV/bin/*worker*; 
pip install pipreqs sphinx; 
pip install -e .; pip install ipykernel; pip install xlsxwriter; python -m ipykernel install --user --name augur --display-name "Python (augur)"; 
python setup.py install;

## Front End 
cd frontend/;
yarn install;
yarn global add apidoc brunch newman @vue/cli; 
yarn run build;
cd ../;

## Workers
cd workers/;

cd ./facade_worker;
rm -rf build/*;
rm -rf dist/*;
python setup.py install;
pip install -e .; 

cd ../github_worker;
rm -rf build/*;
rm -rf dist/*;
python setup.py install; 
pip install -e a;.

cd ../insight_worker; 
rm -rf build/*;
rm -rf dist/*;
python setup.py install;
pip install -e .;

cd ../linux_badge_worker;
rm -rf build/*;
rm -rf dist/*; 
python setup.py install;
pip install -e .;

cd ../pull_request_worker; 
rm -rf build/*;
rm -rf dist/*; 
python setup.py install;
pip install -e .; 

cd ../repo_info_worker;
rm -rf build/*;
rm -rf dist/*; 
python setup.py install;
pip install -e .;
cd ../..;

## API Docs
cd docs && apidoc --debug -f "\.py" -i ../augur/ -o api/; rm -rf ../frontend/public/api_docs; mv api ../frontend/public/api_docs;
