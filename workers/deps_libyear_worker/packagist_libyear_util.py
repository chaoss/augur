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