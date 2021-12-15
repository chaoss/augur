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
    consider_version = version
    try:
        if len(version.split('.')) < 3:
            version = version + '.0'

        #This is for weird inconsistency in packagist as versions can be either as v1.1.1 or 1.1.1 
        version_string = 'v'+ version
        if version_string in list(versions.keys()):
            index = list(reversed(list(versions.keys()))).index(version_string)
        else:
            index = list(reversed(list(versions.keys()))).index(version)

        major,minor,patch = version.split('.')
        for v in list(reversed(list(versions.keys())))[index:]:
            if not 'dev' in v:
                v=clean_version(v)
                if v.split('.')[0]==major:
                    if v.split('.')[1]== minor:
                        if v.split('.')[2]>patch:
                            consider_version = v
    except:
        #NOTE Add error logging here. 
        pass
    
    return consider_version


def get_lastest_packagist_minor(version, data):

    versions = data['package']['versions']
    try:
        if len(version.split('.')) < 3:
            version = version + '.0'

        #This is for weird inconsistency in packagist as versions can be either as v1.1.1 or 1.1.1 
        version_string = 'v'+ version
        if version_string in list(versions.keys()):
            index = list(reversed(list(versions.keys()))).index(version_string)
        else:
            index = list(reversed(list(versions.keys()))).index(version)

        major,minor,patch = version.split('.')
        consider_version = get_latest_packagist_patch(version, data)
        for v in list(reversed(list(versions.keys())))[index:]:
            if not 'dev' in v:
                v=clean_version(v)
                if v.split('.')[0]==major:
                    if v.split('.')[1]>minor:
                        consider_version = v
    except:
        #NOTE: Add error logging here
        pass

    return consider_version


def get_packagist_latest_version(data):
    try:
        versions = data['package']['versions']
        for version in list(versions.keys()):
            #getting the lastes STABLE version
            if not 'dev' in version:
                if not 'alpha' in version:
                    if not 'beta' in version:
                        return version
    except:
        #NOTE: Add error logs 
        return None



def get_packagist_current_version(data, requirement):
    if requirement[0] == '~':
        return get_latest_packagist_patch(clean_version(requirement), data)
    elif requirement[0] == '^':
        return get_lastest_packagist_minor(clean_version(requirement), data)
    