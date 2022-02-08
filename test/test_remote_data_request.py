"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergeAccountingClient
from MergeAccountingClient.model.remote_data_request import RemoteDataRequest
from MergeAccountingClient.api_client import ApiClient


class TestRemoteDataRequest(unittest.TestCase):
    """RemoteDataRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRemoteDataRequest(self):
        """Test RemoteDataRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RemoteDataRequest()  # noqa: E501

        """
        No test json responses were defined for RemoteDataRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (RemoteDataRequest,), False)

        assert deserialized is not None

        assert deserialized.path is not None


if __name__ == '__main__':
    unittest.main()
