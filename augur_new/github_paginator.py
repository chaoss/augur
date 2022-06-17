from urllib.parse import urlencode, urlparse, parse_qs
import collections
import httpx
import time
import json
import asyncio
from .random_key_auth import RandomKeyAuth

# from oauth_key_manager import OauthKeyManager

from urllib.parse import parse_qs, urlparse, urlencode, urlunparse


class GithubPaginator(collections.abc.Sequence):
    def __init__(self, url: str, key_manager: RandomKeyAuth, logger, from_datetime=None, to_datetime=None):

        remove_fields = ["per_page", "page"]
        url = clean_url(url, remove_fields)

        # we need to add query params directly to the url, instead of passing the param to the httpx.Client.request
        # this is because github will only append specified params to the links in the headers if they are a part of the url, and not the params with the request
        params = {"per_page": 100}
        url = add_query_params(url, params)

        self.url = url
        self.key_manager = key_manager
        self.logger = logger

        # get the logger from the key manager
        # self.logger = key_manager.logger

        self.from_datetime = from_datetime
        self.to_datetime = to_datetime

    def __getitem__(self, index: int) -> dict:

        # get the page the item is on
        items_page = (index // 100) + 1

        # create url to query
        params = {"page": items_page}
        url = add_query_params(self.url, params)

        data, _ = self.retrieve_data(url)

        if data is None:
            return None

        # get the position of data on the page
        page_index = index % 100

        try:
            return data[page_index]
        except KeyError:
            return None

    def __len__(self) -> int:

        num_pages = self.get_last_page_number(self.url)

        self.logger.info(f"Num pages: {num_pages}")

        params = {"page": num_pages}
        url = add_query_params(self.url, params)

        # get the amount of data on last page
        data, _ = self.retrieve_data(url)

        last_page_data_count = len(data)

        data_length = (100 * (num_pages - 1)) + last_page_data_count

        return data_length
        

    def __iter__(self):

        data_list, response = self.retrieve_data(self.url)

        if data_list is None:
            yield None
            return 

        for data in data_list:
            yield data

        while 'next' in response.links.keys():
            next_page = response.links['next']['url']

            # Here we don't need to pass in params with the page, or the default params because the url from the headers already has those values
            data_list, response = self.retrieve_data(next_page)

            if data_list is None:
                return

            for data in data_list:
                yield data

    def hit_api(self, url: str, method='GET') -> httpx.Response:

        self.logger.info(f"Hitting endpoint with {method} request: {url}...\n")

        with httpx.Client() as client:

            try:
                response = client.request(
                    method=method, url=url, auth=self.key_manager)

            except TimeoutError:
                self.logger.info("Request timed out. Sleeping 10 seconds and trying again...\n")
                time.sleep(10)
                return None
            except httpx.TimeoutException:
                self.logger.info("httpx.ReadTimeout. Sleeping 10 seconds and trying again...\n")
                time.sleep(10)
                return None

        return response 

    def retrieve_data(self, url: str):

        num_attempts = 0
        while num_attempts < 10:

            response = self.hit_api(url)

            # increment attempts
            if response is None:
                continue
            # update rate limit here

            try:
                page_data = response.json()
            except:
                page_data = json.loads(json.dumps(response.text))

            if type(page_data) == list:
                return page_data, response

            elif type(page_data) == dict:
                result = process_dict_response(response, page_data)

                if result == "break":
                    break
                elif result == "decrease_attempts":
                    num_attempts -= 1

            elif type(page_data) == str:
                result, data_loaded = process_str_response(response, page_data)

                if data_loaded:
                    return result, response

            num_attempts += 1

        return None, None

    async def __aiter__(self):
        
        last_page_num = self.get_last_page_number(self.url)


        if last_page_num == 1:

            params = {"page": 1}
            url = add_query_params(self.url, params)

            data_list, _ = self.retrieve_data(url)

            for data in data_list:
                yield data

            return
        
        async with httpx.AsyncClient() as client:
            tasks = []
            for page_num in range(1, last_page_num + 1):

                params = {"page": page_num}
                url = add_query_params(self.url, params)

                tasks.append(asyncio.ensure_future(
                    self.async_retrieve_data(client, url)))
 
            index = 1
            while len(tasks) > 0:

                self.logger.info(f"Batch {index}")
                data_list = await asyncio.gather(*tasks[:1])
            
                del tasks[:1]

                for data in data_list:
                    yield data

    async def async_hit_api(self, client, url, method='GET'):
        # self.logger.info(f"Hitting endpoint with {method} request: {url}...\n")

        try:
            response = await client.request(method=method, url=url, auth=self.key_manager)

        except TimeoutError:
            self.logger.info("Request timed out. Sleeping 10 seconds and trying again...\n")
            time.sleep(10)
            return None

        self.logger.info(url)

        return response


    async def async_retrieve_data(self, client: httpx.Client, url: str):

        num_attempts = 0
        while num_attempts < 10:

            response = await self.async_hit_api(client, url)
            if response is None:
                continue
            # update rate limit here

            try:
                page_data = response.json()
            except:
                page_data = json.loads(json.dumps(response.text))

            if type(page_data) == list:
                return page_data, response

            elif type(page_data) == dict:
                result = process_dict_response(response, page_data)

                if result == "break":
                    break
                elif result == "decrease_attempts":
                    num_attempts -= 1

            elif type(page_data) == str:
                result, data_loaded = process_str_response(response, page_data)

                if data_loaded:
                    return result, response

            num_attempts += 1

        return None, None

    def get_last_page_number(self, url: str):

        num_attempts = 0
        while num_attempts < 10:
            r = self.hit_api(url, method="HEAD")

            if r:
                break

        else:
            return None

        if 'last' not in r.links.keys():
            return 1
        else:
            # get the last url from header
            last_page_url = r.links['last']['url']

            parsed_url = urlparse(last_page_url)
            num_pages = int(parse_qs(parsed_url.query)['page'][0])

            return num_pages


################################################################################

# Url Helper Method to remove query paramaters from the url
def clean_url(url, remove_fields: [str]):

    u = urlparse(url)
    query = parse_qs(u.query, keep_blank_values=True)

    for field in remove_fields:
        query.pop(field, None)

    u = u._replace(query=urlencode(query, True))
    clean_url = urlunparse(u)

    return clean_url


def add_query_params(url: str, additional_params: dict) -> str:
    url_components = urlparse(url)
    original_params = parse_qs(url_components.query)
    # Before Python 3.5 you could update original_params with
    # additional_params, but here all the variables are immutable.
    merged_params = {**original_params, **additional_params}
    updated_query = urlencode(merged_params, doseq=True)
    # _replace() is how you can create a new NamedTuple with a changed field
    return url_components._replace(query=updated_query).geturl()

################################################################################

# Methods to process api responses

def process_dict_response(response: httpx.Response, page_data: dict):
    
    self.logger.info("Request returned a dict: {}\n".format(page_data))
    if page_data['message'] == "Not Found":
        self.logger.info(
            "Github repo was not found or does not exist for endpoint: "
            f"{response.url}\n"
        )
        return "break"

    if "You have exceeded a secondary rate limit. Please wait a few minutes before you try again" in page_data['message']:
        self.logger.info('\n\n\n\nSleeping for 100 seconds due to secondary rate limit issue.\n\n\n\n')
        time.sleep(100)

        return "decrease_attempts"

    if "You have triggered an abuse detection mechanism." in page_data['message']:
        #self.update_rate_limit(response, temporarily_disable=True,platform=platform)

        return "decrease_attempts"

    if page_data['message'] == "Bad credentials":
        self.logger.info("\n\n\n\n\n\n\n POSSIBLY BAD TOKEN \n\n\n\n\n\n\n")
        #self.update_rate_limit(response, bad_credentials=True, platform=platform)
        return "bad_credentials"

def process_str_response(response: httpx.Response, page_data: str):
        self.logger.info(f"Warning! page_data was string: {page_data}\n")
        if "<!DOCTYPE html>" in page_data:
            self.logger.info("HTML was returned, trying again...\n")
            return "html_response", False
        elif len(page_data) == 0:
            self.logger.info("Empty string, trying again...\n")
            return "empty_string", False
        else:
            try:
                page_data = json.loads(page_data)
                return page_data, True
            except:
                pass


################################################################################

# determines if all the rate limit is used up on a key, and it is depleted
def is_key_depleted(response):

    rate_limit_header_key = "X-RateLimit-Remaining"

    rate_limit = int(response.headers[rate_limit_header_key])

    return rate_limit == 0


################################################################################
