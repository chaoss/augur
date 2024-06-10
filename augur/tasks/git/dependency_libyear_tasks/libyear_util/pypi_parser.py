import re, os
import json
import toml 
import logging
import yaml


#Files that would be parsed should be added here.
file_list = [
    'Requirement.txt',
    'setup.py',
    'Pipfile',
    'Pipfile.lock',
    'pyproject.toml',
    'poetry.lock',
    'environment.yml',
    'environment.yaml',
    'environment.yml.lock',
    'environment.yaml.lock'
]


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


INSTALL_REGEXP = r'install_requires\s*=\s*\[([\s\S]*?)\]'
REQUIRE_REGEXP = r'([a-zA-Z0-9]+[a-zA-Z0-9\-_\.]+)([><=\w\.,]+)?'
REQUIREMENTS_REGEXP = '^#{REQUIRE_REGEXP}'
MANIFEST_REGEXP = r'.*require[^\/]*(\/)?[^\/]*\.(txt|pip)$'

install_regrex = re.compile(INSTALL_REGEXP)
require_regrex = re.compile(REQUIRE_REGEXP)
requirement_regrex = re.compile(REQUIREMENTS_REGEXP)


def parse_requirement_txt(file_handle):

    try:
        manifest= file_handle.read()
    except UnicodeDecodeError:
        #Try UTF-16 as a shot in the dark
        manifest = file_handle.read().decode("utf-16")

    deps=list()
    for line in manifest.split('\n'):
        matches = require_regrex.search(line.replace("'",""))
        if not matches:
            continue
        Dict = {'name': matches[1], 'requirement': matches[2], 'type': 'runtime', 'package': 'PYPI'}
        deps.append(Dict)  
    return deps


def map_dependencies(info):
    if type(info) is dict:

        if "version" in info:
            return info['version']
        elif 'git' in info:
            return info['git']+'#'+info['ref']
    else:            
        return info


def map_dependencies_pipfile(packages, type):
    deps = list()
    if not packages:
        return []
    for name, info in packages.items():
        Dict = {'name': name, 'requirement': map_dependencies(info), 'type': type, 'package': 'PYPI'}
        deps.append(Dict)
    return deps 


def parse_pipfile(file_handle):
    manifest = toml.load(file_handle)
    return map_dependencies_pipfile(manifest['packages'],'runtime') + map_dependencies_pipfile(manifest['dev-packages'], 'develop')


def parse_pipfile_lock(file_object):
    manifest = json.load(file_object)
    deps = list()
    for group,dependencies in manifest.items():
        
        if group == "_meta":
            continue
        if group == 'default':
            group = 'runtime'
        for name,info in dependencies.items():
            
            Dict = {'name': name, 'requirement': map_dependencies(info), 'type': group, 'package': 'PYPI'}
            deps.append(Dict)
    return deps         


def parse_setup_py(file_handle):
    manifest= file_handle.read()

    deps = list()

    # for single_line in manifest:
    # matchh = re.match(INSTALL_REGEXP, manifest)
    matchh = install_regrex.search(manifest)

    if not matchh:
        return deps

    
    for line in re.sub(r"',(\s)?'", r"\n", matchh[1]).split("\n"):
        
        if re.search(r'^#', line):
            continue
        matchhh = re.search(REQUIRE_REGEXP,line)
    
        if not matchhh:
            continue
        
        Dict = {'name': matchhh[1], 'requirement': matchhh[2], 'type': 'runtime', 'package': 'PYPI'}
        deps.append(Dict)
    return deps


def parse_poetry(file_handle):
    manifest = toml.load(file_handle)
    
    # manifest = toml.load(file_handle)['tool']['poetry']
    try:
        return map_dependencies_pipfile(manifest['dependencies'], 'runtime') + map_dependencies_pipfile(manifest['dev-dependencies'], 'develop')
    except Exception as e:
        logging.error(e)
        return []


def parse_poetry_lock(file_handle):
    manifest = toml.load(file_handle)
    deps = list()
    group = 'runtime'
    for package in manifest['package']:
        req = None
        if package['category'] == 'main':
            group = 'runtime'
        if package['category'] == 'dev':
            group = 'develop'
        if 'version' in package:
            req = package['version']
        elif 'git' in package:
            req = package['git']+'#'+package['ref']
        Dict = {'name': package['name'], 'requirement': req, 'type': group, 'package': 'PYPI'}

        deps.append(Dict)
    return deps 

# Pip dependencies can be embedded in conda environment files
def parse_conda(file_handle):
    contents = yaml.safe_load(file_handle)
    deps = list()
    pip = None
    if not contents:
        return []
    #dependencies = contents['dependencies']
    dependencies = contents.get('dependencies', [])
    
    if not dependencies:
        print("No dependencies found.")
        return []
    else:
        print("Dependencies found.")
    for dep in dependencies:
        if (type(dep) is dict) and dep['pip']:
            pip = dep
    if not pip:
        return []
    # parse_requirement_txt(pip["pip"].join("\n"))
    # requirement_txt_parsable = ''  
    for pip_dependency in pip['pip']:
        matches = require_regrex.search(pip_dependency.replace("'",""))
        if not matches:
            continue
        Dict = {'name': matches[1], 'requirement': matches[2], 'type': 'runtime', 'package': 'PYPI'}
        deps.append(Dict)  
    return deps    


# def get_parsed_deps(path):

#     deps_file = None
#     dependency_list = list()

#     for f in file_list:
#         deps_file = find(f, path)
#         if not deps_file:
#             continue
#         file_handle= open(deps_file)

#         if f == 'Requirement.txt':
#             dependency_list = parse_requirement_txt(file_handle)

#         elif f == 'setup.py':
#             dependency_list = parse_setup_py(file_handle)

#         elif f == 'Pipfile':
#             dependency_list = parse_pipfile(file_handle)

#         elif f == 'Pipfile.lock':
#             dependency_list = parse_pipfile_lock(file_handle)

#         elif f == 'pyproject.toml':
#             dependency_list = parse_poetry(file_handle)

#         elif f == 'poetry.lock':
#             dependency_list = parse_poetry_lock(file_handle)

#         elif f == 'environment.yml':
#             dependency_list = parse_conda(file_handle)

#         elif f == 'environment.yaml':
#             dependency_list = parse_conda(file_handle)

#         elif f == 'environment.yml.lock':
#             dependency_list = parse_conda(file_handle)

#         elif f == 'environment.yaml.lock':
#             dependency_list = parse_conda(file_handle)                
#         return dependency_list



# def get_deps_libyear_data(path):
#     current_release_date = None
#     libyear = None

#     dependencies = get_parsed_deps(path)
#     if dependencies:
#         for dependency in dependencies:
#             data = get_pypi_data(dependency['name'])
#             current_version = sort_dependency_requirement(dependency,data)
#             latest_version = get_latest_version(data)
#             latest_release_date = get_release_date(data, latest_version)
#             if current_version:
#                 current_release_date = get_release_date(data, current_version)
#             libyear = get_libyear(current_version, current_release_date, latest_version, latest_release_date)
#             if not latest_release_date:
#                 latest_release_date = dateutil.parser.parse('1970-01-01 00:00:00')
#                 libyear = -1

#             if not latest_version:
#                 latest_version = 'unspecified'     

#             if not current_version:
#                 current_version = latest_version
#                 current_release_date = latest_release_date

#             if not dependency['requirement']:
#                 dependency['requirement'] = 'unspecified'    

#             dependency['current_version'] = current_version    
#             dependency['latest_version'] = latest_version
#             dependency['current_release_date'] = current_release_date
#             dependency['latest_release_date'] = latest_release_date
#             dependency['libyear'] = libyear

#         return dependencies    