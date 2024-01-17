# coding=utf-8
# !/usr/bin/env python
#########################################################
# Python Imports
import requests
import json

# Flask Imports

# Third-Party Imports

# App Imports
from app.exceptions import ExternalAPIError


class RequestFile:

    @staticmethod
    def request_get(url, headers):
        try:
            response = requests.get(url, headers=headers)
            return response
        except Exception as e:
            raise ExternalAPIError(message=str(e))

    @staticmethod
    def request_post(url, payload, headers):
        try:
            response = requests.post(url, json=payload, headers=headers)
            return response
        except Exception as e:
            raise ExternalAPIError(message=str(e))

    @staticmethod
    def request_put(url, payload, headers):
        try:
            response = requests.put(url, json=payload, headers=headers)
            return response
        except Exception as e:
            raise ExternalAPIError(message=str(e))

    @staticmethod
    def request_delete(url, headers):
        try:
            result = requests.delete(url, headers=headers)
            return result
        except Exception as e:
            raise ExternalAPIError(message=str(e))
