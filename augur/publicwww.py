"""
PublicWWW is a class for making API requests to https://publicwww.com/ a
search engine for the source of websites
"""
import sys
import pandas as pd
if sys.version_info > (3, 0):
    import urllib.parse as url
else:
    import urllib as url


class PublicWWW(object):
    """
    PublicWWW is a class for making API requests to https://publicwww.com/ a
    search engine for the source of websites
    """

    def __init__(self, api_key):
        """
        Initalizes a PublicWWW instance

        :param api_key: The API key for PublicWWW. This is required to get the full names of more results
        """
        self.__api_key = api_key

    def linking_websites(self, owner, repo):
        """
        Finds the repo's popularity on the internet

        :param owner: The username of a project's owner
        :param repo: The name of the repository
        :return: DataFrame with the issues' id the date it was
                 opened, and the date it was first responded to
        """

        # Find websites that link to that repo
        repo_url = "https://github.com/{owner}/{repo}".format(owner=owner, repo=repo)
        query = '<a+href%3D"{repourl}"'.format(repourl=url.quote_plus(repo_url))
        req = 'https://publicwww.com/websites/{query}/?export=csv&apikey={apikey}'
        req.format(query=query, apikey=self.__api_key)
        result = pd.read_csv(req, delimiter=';', header=None, names=['url', 'rank'])
        return result
