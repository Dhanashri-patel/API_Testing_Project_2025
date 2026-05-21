from os.path import exists

import requests

from utils.configReader import ReadConfig
from routes.routes import Routes
import os
import logging
import pytest


Log_File= os.path.abspath(os.path.join(os.path.dirname(__file__),"../logs/test_logging.log"))

os.makedirs(os.path.dirname(Log_File),exist_ok=True)
#create logger object
logger = logging.getLogger("api_logger")
#set logging level
logger.setLevel(logging.DEBUG)
#prevent adding multiple handler again and again
if not logger.handlers:
    file_handler = logging.FileHandler(Log_File,mode="a")
    formatter= logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    #set log format
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def log_request_response(response:requests.Response):
    req= response.request

    logger.info(f"Request : {req.method} {req.url}")
    logger.info(f"Request Header: {req.headers}")

    if req.body:
        logger.info(f"Request Body: {req.body}")

    logger.info(f"Response Status: {response.status_code}")
    logger.info(f"Response Headers: {response.headers}")

    try:
        logger.info(f"Response Body: {response.json()}")
    except Exception:
        logger.info(f"Response Body: {response.text}")


@pytest.fixture(scope="class")
def setup():
    #base_url=Routes.base_url
    original_request = requests.Session.request

    def custom_request(self,method,url,**kwargs):
        response = original_request(self,method,url,**kwargs)
        log_request_response(response)
        return response

    requests.Session.request = custom_request

    yield {"base_url": Routes.Base_url, "config_reader": ReadConfig}
