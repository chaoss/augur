import json

def map_dependencies(dict, key, type):
    deps = list()
    if key in dict:
        if not dict[key]:
            return deps
        for name, requirement in dict[key].items():
            Dict = {'name': name, 'requirement': requirement, 'type': type, 'package': 'packagist'}
            deps.append(Dict)
        return deps
    return deps


def parse_compose(file_handle):
    manifest= json.load(file_handle)
    return map_dependencies(manifest, 'require', 'runtime') + map_dependencies(manifest, 'require-dev', 'development')