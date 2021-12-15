import requests

def get_packagist_data(package):
    url = "https://repo.packagist.org/packages/%s.json" % package
    r = requests.get(url)
    if r.status_code < 400:
        return r.json()
    return {}


def clean_version(version):
    version = [v for v in version if v.isdigit() or v == '.']
    return ''.join(version)


def get_packagist_release_date(data, version):
    pass


def get_latest_packagist_patch(version, data):
    versions = data['versions']
    try:
        index = list(versions.keys()).index(version)
    except:
        #NOTE Add error logging here. 
        pass
    if len(version.split('.')) < 3:
        version = version + '.0'
    major,minor,patch = version.split('.')
    consider_version = version


def get_lastest_packagist_minor():
    pass


def get_packagist_latest_version(data):
    pass


def get_packagist_current_version(data, requirement):
    if requirement[0] == '~':
        return get_latest_packagist_patch(clean_version(requirement), data)
    elif requirement[0] == '^':
        return get_lastest_packagist_minor(clean_version(requirement), data)
    